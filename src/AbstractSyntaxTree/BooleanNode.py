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
from AbstractSyntaxTree import AbstractSyntaxTree

class BooleanNode(AbstractSyntaxTree):
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
    def __init__(self):
        pass