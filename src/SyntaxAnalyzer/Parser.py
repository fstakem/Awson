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
from AbstractSyntaxTree import PropertyNode
from AbstractSyntaxTree import AggregatePropertyNode
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
    
    def parseProgram(self):
        program = Program(self.source.name)
        self.current_token = self.scanner.scan(self.source)
        
        while self.current_token != None:
            obj_node = self.parseObject()
            program.objNodes.append(obj_node)

    def parseObject(self):
        if self.current_token.type == TokenType.OBJECT:
            obj_node = ObjectNode(self.current_token.data, self.start_position, self.end_position)
            self.current_token = self.scanner.scan(self.source)
            while self.current_token != TokenType.OBJECT and self.current_token != TokenType.NONE:
                if self.current_token == TokenType.PROPERTY:
                    prop_node = self.parseProperty()
                    obj_node.properties.append(prop_node)
                elif self.current_token == TokenType.AGGREGATE_PROPERTY:
                    agg_prop_node = self.parseAggregateProperty()
                    obj_node.aggregate_properties.append(agg_prop_node)
                else:
                    pos_str = self.positionToString(self.current_token)
                    raise ParseException('Error parsing object token at %s.' % (pos_str) )
                
                self.current_token = self.scanner.scan(self.source)
                
            return obj_node
        else:
            pos_str = self.positionToString(self.current_token)
            raise ParseException('Error parsing object token at %s.' % (pos_str) )
    
    def parseProperty(self):
        prop_node = PropertyNode(self.current_token.data, self.start_position, self.end_position)
        self.parsePropertyData(prop_node)
        
        return prop_node
    
    def parseAggregateProperty(self):
        agg_prop_node = AggregatePropertyNode(self.current_token.data, self.start_position, self.end_position)
        self.parsePropertyData(agg_prop_node)
        
        return agg_prop_node
    
    def parsePropertyData(self, property_node):
        self.current_token = self.scanner.scan(self.source)
        
        if self.current_token == TokenType.INT:
            int_node = self.parseInteger()
        elif self.current_token == TokenType.FLOAT:
            float_node = self.parseFloat()
        elif self.current_token == TokenType.BOOL_TRUE:
            bool_node = self.parseBooleanTrue()
        elif self.current_token == TokenType.BOOL_FALSE:
            bool_node = self.parseBooleanFalse()
        elif self.current_token == TokenType.STRING:
            str_node = self.parseString()
        elif self.current_token == TokenType.CODE:
            code_node = self.parseCode()
        elif self.current_token == TokenType.LEFT_BRACE:
            list_node = self.parseList()
        else:
            pos_str = self.positionToString(self.current_token)
            raise ParseException('Error parsing property data token at %s.' % (pos_str) )
    
    def parseInteger(self):
        int_node = IntegerNode()
    
    def parseFloat(self):
        pass
    
    def parseBooleanTrue(self):
        pass
    
    def parseBooleanFalse(self):
        pass
    
    def parseString(self):
        pass
    
    def parseCode(self):
        pass
    
    def parseList(self):
        pass
    
    def positionToString(self, token):
        return 'line %s position %s' % (str(token.start_position), str(token.end_position))
    
    
    
    