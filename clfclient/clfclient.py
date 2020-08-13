"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Boolean, String, Scope

from .clf.clf import Clf

class CLFClientXBlock(XBlock):
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
    
    """ CLF COURSE DATA """
    name = String(default="", scope=Scope.settings,
        help="The name of the Clf",
    )
    description = String(default="", scope=Scope.settings,
        help="The description of the Clf",
    )
    enabled = Boolean(default=False, scope=Scope.settings,
        help="The state (enabled/disabled) of the Clf",
    )
    proposedAnswer = Boolean(default=False, scope=Scope.settings,
        help="Value what represents if the proposed answer is enabled",
    )
    scheduleCalc = Boolean(default=False, scope=Scope.settings,
        help="Value what represents if the scheduled calculation is enabled",
    )
    moderatorCalc = Integer(default=0, scope=Scope.settings,
        help="The type of calculation for selecting the moderator of the Clf (automatic or manual)",
    )
    moderatorModel = String(default=0, scope=Scope.settings,
        help="The name of the Weka model file for moderator automatic calculations",
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

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8") 

    def student_view(self, context=None):
        """
        The primary view of the CLFClientXBlock, shown to students
        when viewing courses.
        """
        _ = self.runtime.service(self, "i18n").ugettext
        self.message = _("Welcome!")
#         html = self.resource_string("static/html/clfclient.html")
#         frag = Fragment(html.format(self=self))
        frag = Fragment()
        frag.add_content(self.runtime.render_template(
            'clfclient.html',
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
#         html = self.resource_string("static/html/clfclient-studio.html")
#         frag = Fragment(html.format(self=self))
        frag = Fragment()
        frag.add_content(self.runtime.render_template(
            'clfclient-studio.html',
            {'self': self}
        ))
        frag.add_javascript(self.resource_string("static/js/src/clfclient-studio.js"))
        frag.initialize_js('CLFClientXBlock')
        return frag
     
    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.numStakeholders = data.get('numStakeholders')
    
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
