#  ---------------------------------------------------------------------------
#                                                                           
#                               S T R I N G  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from PropertyData import PropertyData

class StringNode(PropertyData):
    """This class represents a string in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('StringNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, data, start_position, end_position):
        super(StringNode, self).__init__(data, start_position, end_position)