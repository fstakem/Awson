#  ---------------------------------------------------------------------------
#                                                                           
#                                  P A R S E R                                
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.5.12

# Libraries
import logging

# Classes
import Utilities
from Token import Token
from TokenType import TokenType
from Scanner import Scanner
from ParseException import ParseException
from AbstractSyntaxTree import Program
from AbstractSyntaxTree import ObjectNode
from AbstractSyntaxTree import ParameterNode
from AbstractSyntaxTree import AggregateParameterNode
from AbstractSyntaxTree import CodeNode
from AbstractSyntaxTree import FloatNode
from AbstractSyntaxTree import IntegerNode
from AbstractSyntaxTree import ListNode
from AbstractSyntaxTree import StringNode

class Parser(object):
    """This class represents a parser for parsing tokens and output a AST."""
       
    # Setup logging
    logger = Utilities.getLogger('Parser')
    
    # Class constants
    
    # -----------------------------------------------------------------------
    #       Class Functions
    # -----------------------------------------------------------------------
    # None
    
    
    # -----------------------------------------------------------------------
    #       Instance Functions
    # -----------------------------------------------------------------------
    def __init__(self, scanner, source):
        self.scanner = scanner
        self.source = source
        self.current_token = None
        self.start_position = None
        self.end_position = None
    
    def parseProgram(self):
        program = Program(self.source.name)
        self.current_token, self.start_position, self.end_position = self.scanner.scan(self.source)
        
        while self.current_token != None:
            objNode = self.parseObject()
            program.objNodes.append(objNode)

    def parseObject(self):
        if self.current_token.type == TokenType.OBJECT:
            objNode = ObjectNode(self.current_token.data, self.start_position, self.end_position)
            self.current_token, self.start_position, self.end_position = self.scanner.scan(self.source)
            while self.current_token != TokenType.OBJECT and self.current_token != TokenType.NONE:
                if self.current_token == TokenType.PROPERTY:
                    pass
                elif self.current_token == TokenType.AGGREGATE_PROPERTY:
                    pass
                else:
                    pass
                
                self.current_token, self.start_position, self.end_position = self.scanner.scan(self.source)
                
            return objNode
        else:
            pass
    
    def parseProperty(self):
        pass
    
    def parseAggregateProperty(self):
        pass
    
    def parseInteger(self):
        pass
    
    def parseFloat(self):
        pass
    
    def parseBoolean(self):
        pass
    
    def parseString(self):
        pass
    
    def parseCode(self):
        pass
    
    def parseList(self):
        pass
    
    
    
    