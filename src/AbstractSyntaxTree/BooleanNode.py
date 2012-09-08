#  ---------------------------------------------------------------------------
#                                                                           
#                             B O O L E A N  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.7.12

# Libraries
import logging

# Classes
import Utilities
from PropertyData import PropertyData

class BooleanNode(PropertyData):
    """This class represents an boolean in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('BooleanNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, data, start_position, end_position):
        super(BooleanNode, self).__init__(data, start_position, end_position)