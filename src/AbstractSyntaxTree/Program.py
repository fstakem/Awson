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
    def __init__(self, name='Generic Program', objNodes=[], start_position, end_position):
        super(Program, self).__init__(start_position, end_position)
        self.name = name
        self.objNodes= objNodes