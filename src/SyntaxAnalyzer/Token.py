#  ---------------------------------------------------------------------------
#                                                                           
#                                 T O K E N                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.4.12

# Libraries
import logging

# Classes
import Utilities
from TokenType import TokenType

class Token(object):
    """This class represents a token that is found in a scanned file."""
       
    # Setup logging
    logger = Utilities.getLogger('Token')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, type=TokenType.NONE, data=None, start_position=-1, end_position=-1):
        self.type = type
        self.data = data
        self.start_position = start_position
        self.end_position = end_position
        
    def __str__(self):
        return 'Type: %s Data: %s Line: %s' % (TokenType.prettyPrint(self.type), self.data, str(self.position[0]))