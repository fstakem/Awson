#  ---------------------------------------------------------------------------
#                                                                           
#                           S C A N  E X C E P T I O N                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.5.12

# Libraries
import sys

# Classes

class ScanException(Exception):
    """This class represents an exception caused when scanning."""
    
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.wrapped_exc = sys.exc_info( )
       

