#  ---------------------------------------------------------------------------
#                                                                           
#                             I N T E G E R  N O D E                              
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class IntegerNode(AbstractSyntaxTree):
    """This class represents a integer in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('IntegerNode')
    
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