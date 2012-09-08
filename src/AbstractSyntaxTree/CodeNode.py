#  ---------------------------------------------------------------------------
#                                                                           
#                               C O D E  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from PropertyData import PropertyData

class CodeNode(PropertyData):
    """This class represents a code in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('CodeNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, data, start_position, end_position):
        super(CodeNode, self).__init__(data, start_position, end_position)