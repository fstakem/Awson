#  ---------------------------------------------------------------------------
#                                                                           
#                               L I S T  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from PropertyData import PropertyData

class ListNode(PropertyData):
    """This class represents a list in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('ListNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, start_position, end_position):
        super(ListNode, self).__init__(data=[], start_position, end_position)