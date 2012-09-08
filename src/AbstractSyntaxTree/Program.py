#  ---------------------------------------------------------------------------
#                                                                           
#                                P R O G R A M                               
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities
from AbstractSyntaxTree import AbstractSyntaxTree

class Program(AbstractSyntaxTree):
    """This class represents a program object in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('Program')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, objNodes=[]):
        self.objNodes= objNodes