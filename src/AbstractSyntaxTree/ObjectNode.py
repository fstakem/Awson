#  ---------------------------------------------------------------------------
#                                                                           
#                             O B J E C T  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class ObjectNode(AbstractSyntaxTree):
    """This class represents an object in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('ObjectNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, name='Generic Object', start_position, end_position):
        super(ObjectNode, self).__init__(start_position, end_position)
        self.name = name
        self.properties = []
        self.aggregate_properties = []