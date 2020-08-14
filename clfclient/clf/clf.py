'''
Created on 17 jul. 2020

@author: javi
'''
import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, String, Boolean, Scope

class Clf(XBlock):
    '''
    classdoc
    '''
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
    x = 68
        
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
    
    def increment(self):
        self.x += 1
