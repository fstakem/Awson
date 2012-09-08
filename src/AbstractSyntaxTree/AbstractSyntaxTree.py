#  ---------------------------------------------------------------------------
#                                                                           
#                      A B S T R A C T  S Y N T A X  T R E E                               
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.6.12

# Libraries
import logging

# Classes
import Utilities

class AbstractSyntaxTree(object):
    """This class represents a base object in a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('AbstractSyntaxTree')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, start_position, end_position):
        self.start_position = start_position
        self.end_position = end_position