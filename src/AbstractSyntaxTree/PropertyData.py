#  ---------------------------------------------------------------------------
#                                                                           
#                            P R O P E R T Y  D A T A                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class PropertyData(AbstractSyntaxTree):
    """This class represents a property data type in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('PropertyData')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, data=None, start_position, end_position):
        super(PropertyData, self).__init__(start_position, end_position)
        self.data = data