#  ---------------------------------------------------------------------------
#                                                                           
#                  A G G R E G A T E  P A R A M E T E R  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class AggregateParameterNode(AbstractSyntaxTree):
    """This class represents an aggregate parameter in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('AggregateParameterNode')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self):
        pass