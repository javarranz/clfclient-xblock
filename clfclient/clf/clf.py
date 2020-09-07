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
    name = String(default="New Collaborative Logical Framework", scope=Scope.content,
        help="The name of the Clf",
    )
    description = String(default="", scope=Scope.content,
        help="The description of the Clf",
    )
#     enabled = Boolean(default=False, scope=Scope.content,
#         help="The state (enabled/disabled) of the Clf",
#     )
#     proposedAnswer = Boolean(default=False, scope=Scope.content,
#         help="Value what represents if the proposed answer is enabled",
#     )
#     scheduleCalc = Boolean(default=False, scope=Scope.content,
#         help="Value what represents if the scheduled calculation is enabled",
#     )
#     moderatorCalc = Integer(default=0, scope=Scope.content,
#         help="The type of calculation for selecting the moderator of the Clf (automatic or manual)",
#     )
#     moderatorModel = String(default=0, scope=Scope.content,
#         help="The name of the Weka model file for moderator automatic calculations",
#     ) 
     
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
