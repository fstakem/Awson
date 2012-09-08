#  ---------------------------------------------------------------------------
#                                                                           
#                           P A R S E  E X C E P T I O N                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.5.12

# Libraries
import sys

# Classes

class ParseException(Exception):
    """This class represents an exception caused when parsing."""
    
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.wrapped_exc = sys.exc_info( )
       

