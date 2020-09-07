"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xml.etree import ElementTree as ET
from collections import OrderedDict 
import requests
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Boolean, String, List, Dict, Scope, ScopeBase, UserScope, BlockScope
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioContainerXBlockMixin, StudioEditableXBlockMixin

from .clf.clf import Clf

loader = ResourceLoader(__name__)

@XBlock.needs("i18n")
class CLFClientXBlock(StudioContainerXBlockMixin, StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    
    """ PACKAGE """
    display_name = String(default="Collaborative Logical Framework", scope=Scope.settings,
        help="Display name of the component"
    )
    packageUUID = String(default='', scope=Scope.preferences,
        help="Unique identifier for the package of the Clf in the database",
    )
    packageId = String(default='', scope=Scope.preferences,
        help="Identifier for the package of the Clf in the database",
    )
    clfId = String(default='', scope=Scope.preferences,
        help="Identifier for the Clf in the database",
    )
    
    """ CLF COURSE DEFAULT DATA """
    numDaysAnswer = Integer(default=5, scope=Scope.settings,
        help=" The number of days for the student to answer the questions. By default when creating a phase",
    )
    numDaysConsensus = Integer(default=2, scope=Scope.settings,
        help="The number of days to create and send the consensus answer. By default when creating the phase",
    )
    numBestAnswers = Integer(default=2, scope=Scope.settings,
        help="The number of best answers to take into account when the moderator is entering in the agreement phase",
    )
    moderatorValue = Integer(default=30, scope=Scope.settings,
        help="Default value to decide when a student is candidate for moderator",
    )  
        
    """ CLF PACKAGE DEFAULT DATA """
    timeProfileCalculation = Integer(default=43200, scope=Scope.settings,
        help="Period of time between profile calculations",
    )  
    maxMembersGroup = Integer(default=6, scope=Scope.settings,
        help="Maximum number of students for a CLF group",
    )  
    answerRefreshTime = Integer(default=20, scope=Scope.settings,
        help="Period of refresh time in seconds for the CLF Answers view",
    ) 
       
    """ CLF SERVER CONNECTION """
    serverIP = String(default="192.168.0.100", scope=Scope.settings,
        help="IP of the CLF Server",
    )
    serverNSpace = String(default="http://services.clf", scope=Scope.settings,
        help="NSpace of the CLF Server",
    )
    serverPort = String(default="8080", scope=Scope.settings,
        help="Port of the CLF Server",
    )
    serverProtocol = String(default="http", scope=Scope.settings,
        help="Protocol for connecting web services from CLF Server. Typically http or https",
    )
    serverWSDLLocation = String(default="clf-server/services/Services?wsdl", scope=Scope.settings,
        help="Location of the WSDL into the CLF Server",
    )
    
    """ LOGICAL FRAMEWORK """
    numStakeholders = Integer(default=6, scope=Scope.settings,
        help="Maximum number of stakeholders for the first phase of the Collaborative Logical Framework",
    )
    influenceValues = String(default="Alta;Baja", scope=Scope.settings,
        help="List of values to determine the capacity of every stakeholder to satisfy the interest described",
    )
    impactValues = String(default="+;=+;=;=-;-;?", scope=Scope.settings,
        help="List of values for the impact of the project to the stakeholders",
    )
    importanceValues = String(default="Alta;Baja", scope=Scope.settings,
        help="List of values to describe the importance of every stakeholder",
    )
    numProblems = Integer(default=60, scope=Scope.settings,
        help="The maximum number of nodes in the problems tree",
    )
    numObjectives = Integer(default=60, scope=Scope.settings,
        help="The maximum number of objectives to include in the objectives tree",
    )
    qualitativeData = String(default="Alta;Medio/Alto;Medio;Medio/Bajo;Bajo", scope=Scope.settings,
        help="This values are used in the Alternative Analysis to evaluate the different criteria",
    )
    numCriterium = Integer(default=30, scope=Scope.settings,
        help="Maximum number of criterium to define in the Alternatives Phase",
    )
    numAlternatives = Integer(default=6, scope=Scope.settings,
        help="Maximum number of alternatives used in the Alternatives Phase",
    )
    quantitativeCriteria = String(default="1;2;3;4;5", scope=Scope.settings,
        help="The possible coefficient to assign to the Criteria",
    )
    quantitativeAlt = String(default="-1;0;1;2;3;4;5;6", scope=Scope.settings,
        help="The possible coefficient to assign to the alternatives",
    )
    
    clf_editable_fields = ('numDaysAnswer', 'numDaysConsensus', 'numBestAnswers', 'moderatorValue') 
    package_editable_fields = ('timeProfileCalculation', 'maxMembersGroup', 'answerRefreshTime')
    server_editable_fields = ('serverIP', 'serverNSpace', 'serverPort', 'serverProtocol', 'serverWSDLLocation')
    lf_editable_fields = ('numStakeholders', 'influenceValues', 'impactValues', 'importanceValues', 'numProblems',
        'numObjectives', 'qualitativeData', 'numCriterium', 'numAlternatives', 'quantitativeCriteria', 'quantitativeAlt') 
    editable_fields = clf_editable_fields + package_editable_fields + server_editable_fields + lf_editable_fields
          
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8") 

    def student_view(self, context=None):
        """
        The primary view of the CLFClientXBlock, shown to students
        when viewing courses.
        """
        self.message = self.ugettext("Welcome")
        frag = Fragment()
        frag.add_content(loader.render_template(
            'templates/clfclient.html',
            {'self': self}
        ))
        frag.add_css(self.resource_string("static/css/clfclient.css"))
        frag.add_javascript(self.resource_string("static/js/src/clfclient.js"))
        frag.initialize_js('CLFClientXBlock')
        return frag
    
    def author_view(self, context=None):
        """
        The primary view of the CLFClientXBlock, shown to students
        when viewing courses.
        """
        frag = Fragment()
        clf_info = {}
        if (self.clfId != ''):
            status, clf_info = self.consume_service('getClf', {'clfId': self.clfId})
        html_context = dict(
            self=self,
            clf_info = clf_info,
            back_icon=self.runtime.local_resource_url(self, 'static/icons/back-016.png'),
        )
        frag.add_content(loader.render_template(
            'templates/clfclient-author.html',
            html_context
        ))
        frag.add_css_url("https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css")
        frag.add_javascript(self.resource_string("static/js/src/clfclient-author.js"))       
        frag.initialize_js('CLFClientXBlock')
        return frag
      
    @XBlock.json_handler
    def register_on_server_submit(self, data, suffix=''):
        status, result = self.consume_service('createPackage')
        if (status['CodeMajor'] == 'Success'):
            self.packageUUID = result['return']
            data = {'packageUUID': self.packageUUID}
            status, result = self.consume_service('getServerPackageId', data)
            if (status['CodeMajor'] == 'Success'):
                self.packageId = result['return']
                data = OrderedDict([('packageId', self.packageId), ('name', 'New CLF'), 
                    ('description', 'New description'), ('enabled', 'false')]) 
                for field_name in self.lf_editable_fields:
                    field = self.fields[field_name]
                    data[field_name] = str(self._make_field_info(field_name, field)['value'])
                data['numDaysAnswer'] = self.numDaysAnswer
                data['numDaysConsensus'] = self.numDaysConsensus
                data['proposedAnswer'] = 'false'
                data['numBestAnswers'] = self.numBestAnswers
                data['scheduleCalc'] = 'false'
                data['moderatorValue'] = self.moderatorValue
                data['moderatorCalc'] = '1'
                data['moderatorModel'] = 'Moderator.model'
                status, result = self.consume_service('createClf', data)
                if (status['CodeMajor'] == 'Success'):
                    self.clfId = result['return']
        return {'result': 'success', 'xml_content': ''}
    
    def consume_service(self, serv_name, data = {}):
        url = self.serverProtocol + '://' + self.serverIP + ':' + self.serverPort 
        url += '/' + self.serverWSDLLocation
        wsschema = 'http://schemas.xmlsoap.org/soap/envelope/'
        nspace = self.serverNSpace
        root = ET.Element('soapenv:Envelope', 
            {'xmlns:soapenv': wsschema, 'xmlns:ser': nspace}
        )
        headUUID = ET.Element('ser:UUID')
        headUUID.text = self.packageUUID
        headAuth = ET.Element('ser:clfAuthentication')
        headAuth.append(headUUID)
        head = ET.Element('soapenv:Header')
        head.append(headAuth)
        root.append(head)
        bodyData = ET.Element('ser:' + serv_name)
        for key, val in data.items():
            e = ET.Element('ser:' + key)
            e.text = str(val)
            bodyData.append(e)        
        body = ET.Element('soapenv:Body')
        body.append(bodyData)
        root.append(body)
        print('SERVICE REQUEST: ', ET.tostring(root))
        headers = {'Content-Type':'text/xml'}
        try:
            response = requests.post(url, headers=headers, data=ET.tostring(root))
            root = ET.fromstring(response.content)
            print('SERVICE RESPONSE: ', response.content)
            status_root = root[0][0]
            status = {}
            for child in status_root:
                status[child.tag.split('}', 1)[1]] = child.text
            result_root = root[1][0][0]
            result = {}
            if (len(result_root) == 0):
                # single result
                result[result_root.tag.split('}', 1)[1]] = result_root.text 
            else:
                # structured result
                for child in result_root:
                    result[child.tag.split('}', 1)[1]] = child.text 
            print('SERVICE STATUS: ', status)
            print('SERVICE RESULT: ', result)
        except:
            print('SERVICE ERROR: Cannot connect to the CLF server')
        return status, result
        
    def studio_view(self, context=None):
        """
        The studio view of the CLFClientXBlock.
        """
        clf_fields = []
        for field_name in self.clf_editable_fields:
            field = self.fields[field_name]
            field_info = self._make_field_info(field_name, field)
            if field_info is not None:
                clf_fields.append(field_info)
        package_fields = []
        for field_name in self.package_editable_fields:
            field = self.fields[field_name]
            field_info = self._make_field_info(field_name, field)
            if field_info is not None:
                package_fields.append(field_info)
        server_fields = []
        for field_name in self.server_editable_fields:
            field = self.fields[field_name]
            field_info = self._make_field_info(field_name, field)
            if field_info is not None:
                server_fields.append(field_info)
        lf_fields = []
        for field_name in self.lf_editable_fields:
            field = self.fields[field_name]
            field_info = self._make_field_info(field_name, field)
            if field_info is not None:
                lf_fields.append(field_info)
        frag = Fragment()
        frag.add_content(loader.render_template(
            'templates/clfclient-studio.html',
            {'self': self, 'clf_fields': clf_fields, 'package_fields': package_fields, 'server_fields': server_fields, 'lf_fields': lf_fields}
        ))
        frag.add_javascript(self.resource_string("static/js/src/clfclient-studio.js"))
        frag.initialize_js('CLFClientXBlock')
        return frag
