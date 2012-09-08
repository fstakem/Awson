#  ---------------------------------------------------------------------------
#                                                                           
#                         P R O P E R T Y  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class PropertyNode(AbstractSyntaxTree):
    """This class represents a property in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('PropertyNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, name='Generic Property', start_position, end_position):
        super(PropertyNode, self).__init__(start_position, end_position)
        self.name = name
        self.data = None