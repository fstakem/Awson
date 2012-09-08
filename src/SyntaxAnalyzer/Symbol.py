#  ---------------------------------------------------------------------------
#                                                                           
#                                 S Y M B O L                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.4.12

# Libraries
import logging

# Classes
import Utilities

class Symbol(object):
    """This class represents a symbol for mapping characters to internal reprsentation."""
       
    # Setup logging
    logger = Utilities.getLogger('Symbol')
    
    # Class constants
    symbol_table = {
                    'separator':            [ ' ', '\t', '\n' ],
                    'comment':              [ '#' ],          
                    'eol':                  [ '\n' ],
                    'eof':                  [ 'eof' ],
                    'dash':                 [ '-' ],
                    'tilda':                [ '~' ],
                    'char':                 [],
                    'digit':                [],
                    'single quote':         [ "'" ],
                    'double quote':         [ '"' ],
                    'left curly brace':     [ '{' ],
                    'right curly brace':    [ '}' ],
                    'left brace':           [ '[' ],
                    'right brace':          [ ']' ],
                    'decimal point':        [ '.' ],
                    'colon':                [ ':' ],
                    'exponent':             [ 'e', 'E' ],
                    'bar':                  [ '|' ]
                   }
    
    keywords = {
                'boolean true':             [ 'true' ],
                'boolean false':            [ 'false' ]
               }
    
    SEPARATOR = Symbol.symbol_table['separator']
    COMMENT = Symbol.symbol_table['comment']
    EOL = Symbol.symbol_table['eol']
    EOF = Symbol.symbol_table['eof']
    DASH = Symbol.symbol_table['dash']
    TILDA = Symbol.symbol_table['tilda']
    CHAR = Symbol.symbol_table['char']
    DIGIT = Symbol.symbol_table['digit']
    SINGLE_QUOTE = Symbol.symbol_table['single quote']
    DOUBLE_QUOTE = Symbol.symbol_table['double quote']
    LEFT_CURLY_BRACE = Symbol.symbol_table['left curly brace']
    RIGHT_CURLY_BRACE = Symbol.symbol_table['right curly brace']
    LEFT_BRACE = Symbol.symbol_table['left brace']
    RIGHT_BRACE = Symbol.symbol_table['right brace']
    DECIMAL_POINT = Symbol.symbol_table['decimal point']
    COLON = Symbol.symbol_table['colon']
    EXPONENT = Symbol.symbol_table['exponent']
    BAR = Symbol.symbol_table['bar'] 
    
    BOOLEAN_TRUE = Symbol.keywords['boolean true']
    BOOLEAN_FALSE = Symbol.keywords['boolean false']
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self):
        pass
    
    @classmethod
    def isSeparator(cls, symbol):
        cls.isMatch(symbol, cls.SEPARATOR)
        
    @classmethod
    def isComment(cls, symbol):
        cls.isMatch(symbol, cls.COMMENT)
        
    @classmethod
    def isEol(cls, symbol):
        cls.isMatch(symbol, cls.EOL)
        
    @classmethod
    def isEof(cls, symbol):
        cls.isMatch(symbol, cls.EOF)
        
    @classmethod
    def isDash(cls, symbol):
        cls.isMatch(symbol, cls.DASH)
        
    @classmethod
    def isTilda(cls, symbol):
        cls.isMatch(symbol, cls.TILDA)
        
    @classmethod
    def isCharacter(cls, symbol):
        symbol.isalpha()
        
    @classmethod
    def isDigit(cls, symbol):
        symbol.isdigit()
        
    @classmethod
    def isQuote(cls, symbol, quote_type):
        cls.isMatch(symbol, quote_type)
        
    @classmethod
    def isSingleQuote(cls, symbol):
        cls.isMatch(symbol, cls.SINGLE_QUOTE)
        
    @classmethod
    def isDoubleQuote(cls, symbol):
        cls.isMatch(symbol, cls.DOUBLE_QUOTE)
        
    @classmethod
    def isLeftCurlyBrace(cls, symbol):
        cls.isMatch(symbol, cls.LEFT_CURLY_BRACE)
        
    @classmethod
    def isRightCurlyBrace(cls, symbol):
        cls.isMatch(symbol, cls.RIGHT_CURLY_BRACE)
        
    @classmethod
    def isLeftBrace(cls, symbol):
        cls.isMatch(symbol, cls.LEFT_BRACE)
        
    @classmethod
    def isRightBrace(cls, symbol):
        cls.isMatch(symbol, cls.RIGHT_BRACE)
        
    @classmethod
    def isDecimalPoint(cls, symbol):
        cls.isMatch(symbol, cls.DECIMAL_POINT)
        
    @classmethod
    def isColon(cls, symbol):
        cls.isMatch(symbol, cls.COLON)
        
    @classmethod
    def isExponent(cls, symbol):
        cls.isMatch(symbol, cls.EXPONENT)
        
    @classmethod
    def isBar(cls, symbol):
        cls.isMatch(symbol, cls.BAR)
        
    @classmethod
    def isBooleanTrue(cls, token):
        cls.isMatch(token, cls.BOOLEAN_TRUE)
        
    @classmethod
    def isBooleanFalse(cls, token):
        cls.isMatch(token, cls.BOOLEAN_FALSE)
    
    @classmethod 
    def isMatch(cls, value, value_list):
        result = False
        for other_value in value_list:
            if value == other_value:
                result = True
                break
            
        return result
            
    
    
    
    