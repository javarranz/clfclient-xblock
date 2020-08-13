'''
Created on 17 jul. 2020

@author: javi
'''
import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope

class Clf(XBlock):
    '''
    classdoc
    '''
    x = 68
        
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
    
    def increment(self):
        self.x += 1
