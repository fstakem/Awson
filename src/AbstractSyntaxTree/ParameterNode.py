#  ---------------------------------------------------------------------------
#                                                                           
#                         P A R A M E T E R  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class ParameterNode(AbstractSyntaxTree):
    """This class represents a parameter in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('ParameterNode')
    
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