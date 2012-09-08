#  ---------------------------------------------------------------------------
#                                                                           
#                      S I M P L E  P R O P E R T Y  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.8.12

# Libraries
import logging

# Classes
import Utilities
from PropertyNode import PropertyNode

class SimplePropertyNode(PropertyNode):
    """This class represents a property in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('Simple PropertyNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, name='Simple Generic Property', start_position, end_position):
        super(SimplePropertyNode, self).__init__(start_position, end_position)