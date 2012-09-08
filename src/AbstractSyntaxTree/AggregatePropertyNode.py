#  ---------------------------------------------------------------------------
#                                                                           
#                  A G G R E G A T E  P R O P E R T Y  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from PropertyNode import PropertyNode

class AggregatePropertyNode(PropertyNode):
    """This class represents an aggregate property in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('AggregatePropertyNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, name='Aggregate Generic Property', start_position, end_position):
        super(AggregatePropertyNode, self).__init__(start_position, end_position)