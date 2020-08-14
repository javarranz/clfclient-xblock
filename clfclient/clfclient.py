"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Boolean, String, Scope
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioContainerXBlockMixin, StudioEditableXBlockMixin

from .clf.clf import Clf

loader = ResourceLoader(__name__)

class CLFClientXBlock(StudioContainerXBlockMixin, StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    
    """ PACKAGE """
    display_name = String(default="Collaborative Logical Framework", scope=Scope.settings,
        help="Display name of the component"
    )
    packageUUID = Integer(default=0, scope=Scope.settings,
        help="Unique identifier for the package of the Clf in the database",
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
    serverIP = String(default="192.168.0.200", scope=Scope.settings,
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
        self.message = self.ugettext("AUTHOR")
        frag = Fragment()
        frag.add_content(loader.render_template(
            'templates/clfclient.html',
            {'self': self}
        ))
        frag.add_css(self.resource_string("static/css/clfclient.css"))
        frag.add_javascript(self.resource_string("static/js/src/clfclient.js"))
        frag.initialize_js('CLFClientXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The primary view of the CLFClientXBlock, shown to students
        when viewing courses.
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
      
    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        print("AAAAAAAAAAAAAAAAAAAAAAAAA", data)
        self.serverIP = data.get('serverIP')
    
        return {'result': 'success'}
        
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("CLFClientXBlock",
             """<clfclient/>
             """),
            ("Multiple CLFClientXBlock",
             """<vertical_demo>
                <clfclient/>
                <clfclient/>
                <clfclient/>
                </vertical_demo>
             """),
        ]