#  ---------------------------------------------------------------------------
#                                                                           
#                               F L O A T  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from PropertyData import PropertyData

class FloatNode(PropertyData):
    """This class represents a float in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('FloatNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, data, start_position, end_position):
        super(FloatNode, self).__init__(data, start_position, end_position)