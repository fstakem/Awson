#  ---------------------------------------------------------------------------
#                                                                           
#                                 S C A N N E R                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.4.12

# Libraries
import logging
from copy import deepcopy

# Classes
import Utilities
from Symbol import Symbol
from Token import Token
from TokenType import TokenType
from LanguageSource import LanguageSource
from ScanException import ScanException

class Scanner(object):
    """This class represents a scanner that scans a file outputting tokens."""
       
    # Setup logging
    logger = Utilities.getLogger('Scanner')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self):
        self.current_symbol = None
        self.start_position = None
        self.current_position = None
        self.symbol_buffer = None
        
    def scan(self, source):
        self.current_symbol, self.current_position = source.getNextSymbol()
        self.start_position = deepcopy( self.current_position )
        
        while True:
            if Symbol.isComment(self.current_symbol):
                self.scanComment(source)
            elif Symbol.isSeparator(self.current_symbol):
                self.scanSeperator(source)
            elif Symbol.isEof(self.current_symbol):
                return None
            else:
                return (self.scanToken(source), self.start_position, self.current_position)
       
    def scanComment(self, source):
        while not Symbol.isEol(self.current_symbol):
            self.current_symbol, self.current_position = source.getNextSymbol()
            
        self.current_symbol, self.current_position = source.getNextSymbol()
    
    def scanSeperator(self, source):
        while Symbol.isSeparator(self.current_symbol):
            self.current_symbol, self.current_position = source.getNextSymbol()
    
    def scanToken(self, source):
        self.symbol_buffer = ''
        
        if Symbol.isTilda(self.current_symbol):
            return self.scanAggregateProperty(source)
        elif Symbol.isSingleQuote(self.current_symbol):
            return self.scanString(Symbol.SINGLE_QUOTE[0])
        elif Symbol.isDoubleQuote(self.current_symbol):
            return self.scanString(Symbol.DOUBLE_QUOTE[0])
        elif Symbol.isLeftCurlyBrace(self.current_symbol):
            return self.scanCode(source)
        elif Symbol.isLeftBrace(self.current_symbol):
            return self.scanLeftBrace(source)
        elif Symbol.isRightBrace(self.current_symbol):
            return self.scanRightBrace(source)
        elif Symbol.isDash(self.current_symbol):
            return self.scanDash(source)
        elif Symbol.isDigit(self.current_symbol):
            return self.scanDigit(source)
        elif Symbol.isCharacter(self.current_symbol):
            return self.scanChar(source)
        else:
            pos_str = self.positionToString(self.current_position)
            raise ScanException('Error scanning token at %s.' % (pos_str) )
        
    def scanDash(self, source):
        self.acceptSymbol(source)
        if Symbol.isCharacter(self.current_symbol):
            return self.scanObject(source)
        elif Symbol.isDigit(self.current_symbol):
            return self.scanDigit(source)
        elif Symbol.isDecimalPoint(self.current_symbol):
            return self.scanFloat(source)
        else:
            pos_str = self.positionToString(self.current_position)
            raise ScanException('Error scanning dash at %s.' % (pos_str) )
    
    def scanChar(self, source):
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol(source)
            
        if Symbol.isColon(self.current_symbol):
            return self.scanProperty(source)
        elif Symbol.isSeparator(self.current_symbol):
            return self.scanBool(source)
        else:
            pos_str = self.positionToString(self.current_position)
            raise ScanException('Error scanning character at %s.' % (pos_str) )
    
    def scanDigit(self, source):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol(source)
            
        if Symbol.isDecimalPoint(self.current_symbol):
            return self.scanFloat(source)
        elif Symbol.isSeparator(self.current_symbol):
            return self.scanInt(source)
        else:
            pos_str = self.positionToString(self.current_position)
            raise ScanException('Error scanning digit at %s.' % (pos_str) )
    
    def scanObject(self, source):
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol(source)
            
        if Symbol.isSeparator(self.current_symbol):
            return Token(TokenType.OBJECT, self.symbol_buffer, self.start_position)
        
        pos_str = self.positionToString(self.current_position)
        raise ScanException('Error scanning object at %s.' % (pos_str) )
    
    def scanProperty(self, source):
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol(source)
            
        if Symbol.isColon(self.current_symbol):
            return Token(TokenType.PROPERTY, self.symbol_buffer, self.start_position)
        
        pos_str = self.positionToString(self.current_position)
        raise ScanException('Error scanning property at %s.' % (pos_str) )
    
    def scanAggregateProperty(self, source):
        self.acceptSymbol(source)
        while Symbol.isCharacter(self.current_symbol):
            self.acceptSymbol(source)
            
        if Symbol.isColon(self.current_symbol):
            return Token(TokenType.AGGREGATE_PROPERTY, self.symbol_buffer, self.start_position)
        
        pos_str = self.positionToString(self.current_position)
        raise ScanException('Error scanning aggregate property at %s.' % (pos_str) )
          
    def scanInt(self, source):
        return Token(TokenType.INT, self.symbol_buffer, self.start_position)
    
    def scanFloat(self, source):
        while Symbol.isDigit(self.current_symbol):
            self.acceptSymbol(source)
            
        if Symbol.isSeparator(self.current_symbol):
            return Token(TokenType.FLOAT, self.symbol_buffer, self.start_position)
        elif Symbol.isExponent(self.current_symbol):
            self.acceptSymbol(source)
            if Symbol.isDash(self.current_symbol):
                self.acceptSymbol(source)
                
                while Symbol.isDigit(self.current_symbol):
                    self.acceptSymbol(source)
                    
                if Symbol.isSeparator(self.current_symbol):
                    return Token(TokenType.FLOAT, self.symbol_buffer, self.start_position)
                
        pos_str = self.positionToString(self.current_position)
        raise ScanException('Error scanning float at %s.' % (pos_str) )
    
    def scanBool(self, source):
        if Symbol.isBooleanTrue(self.symbol_buffer):
            return Token(TokenType.BOOL_TRUE, self.symbol_buffer, self.start_position)
        elif Symbol.isBooleanFalse(self.symbol_buffer):
            return Token(TokenType.BOOL_FALSE, self.symbol_buffer, self.start_position)
        
        pos_str = self.positionToString(self.current_position)
        raise ScanException('Error scanning boolean at %s.' % (pos_str) )
    
    def scanString(self, source, start_symbol):
        self.acceptSymbol(source)
        
        while not Symbol.isQuote(self.current_symbol, start_symbol):
            self.acceptSymbol(source)
            self.testForEof()
            
        self.acceptSymbol(source)
        
        return Token(TokenType.STRING, self.symbol_buffer, self.start_position)
    
    def scanLeftBrace(self, source):
        self.acceptSymbol(source)
        return Token(TokenType.LEFT_BRACE, self.symbol_buffer, self.start_position)
    
    def scanRightBrace(self, source):
        self.acceptSymbol(source)
        return Token(TokenType.RIGHT_BRACE, self.symbol_buffer, self.start_position)
               
    def scanCode(self, source):
        self.acceptSymbol(source)
        
        while not Symbol.isRightCurlyBrace(self.current_symbol):
            self.acceptSymbol(source)
            self.testForEof()
            
        self.acceptSymbol(source)
        
        return Token(TokenType.CODE, self.symbol_buffer, self.start_position)
    
    def acceptSymbol(self, source):
        self.symbol_buffer += self.current_symbol
        self.current_symbol, self.current_position = source.getNextSymbol()
            
    def positionToString(self, position):
        return 'line %s position %s' % (str(position[0]), str(position[1]))
    
    def testForEof(self):
        if Symbol.isEof(self.current_symbol):
            pos_str = self.positionToString(self.current_position)
            raise ScanException('Error scanning at %s.' % (pos_str) )
    
    
    
    