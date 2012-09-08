#  ---------------------------------------------------------------------------
#                                                                           
#                          L A N G U A G E  S O U R C E                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.5.12

# Libraries
import logging

# Classes
import Utilities
from Symbol import Symbol

class LanguageSource(object):
    """This class represents a language source for giving symbols to the scanner."""
       
    # Setup logging
    logger = Utilities.getLogger('LanguageSource')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, symbols=''):
        self.symbols = symbols
        self.last_symbol = None
        self.current_position = -1
        self.current_line = 1
        self.current_line_position = -1
    
    def getNextSymbol(self):
        self.current_position += 1
        self.current_line_position += 1
        
        try:
            next_symbol = self.symbols[self.current_position]
            
            if self.last_symbol == Symbol.EOL:
                self.current_line += 1
                self.current_line_position = 0
    
            self.last_symbol = next_symbol
            
            return (next_symbol, (self.current_line, self.current_line_position))
        except IndexError:
            return Symbol.EOF
        
        
    
            