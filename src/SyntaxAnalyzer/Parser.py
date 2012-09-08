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
from AbstractSyntaxTree import BooleanNode
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
        
        pos_str = self.positionToString(self.current_token)
        raise ParseException('Error parsing object token at %s.' % (pos_str) )
    
    def parseProperty(self):
        prop_node = PropertyNode(self.current_token.data, self.start_position, self.end_position)
        prop_node.data = self.parseValue()
        
        return prop_node
    
    def parseAggregateProperty(self):
        agg_prop_node = AggregatePropertyNode(self.current_token.data, self.start_position, self.end_position)
        agg_prop_node.data = self.parseValue()
        
        return agg_prop_node
    
    def parseValue(self):
        self.current_token = self.scanner.scan(self.source)
        
        if self.current_token == TokenType.INT:
            return self.parseInteger()
        elif self.current_token == TokenType.FLOAT:
            return self.parseFloat()
        elif self.current_token == TokenType.BOOL_TRUE or self.current_token == TokenType.BOOL_FALSE:
            return self.parseBoolean()
        elif self.current_token == TokenType.STRING:
            return self.parseString()
        elif self.current_token == TokenType.CODE:
            return self.parseCode()
        elif self.current_token == TokenType.LEFT_BRACE:
            return self.parseList()
        
        pos_str = self.positionToString(self.current_token)
        raise ParseException('Error parsing value token at %s.' % (pos_str) )
            
    def parseInteger(self):
        return IntegerNode(self.current_token.data, self.start_position, self.end_position)
    
    def parseFloat(self):
        return FloatNode(self.current_token.data, self.start_position, self.end_position)
    
    def parseBoolean(self):
        return BooleanNode(self.current_token.data, self.start_position, self.end_position)
    
    def parseString(self):
        return StringNode(self.current_token.data, self.start_position, self.end_position)
    
    def parseCode(self):
        return CodeNode(self.current_token.data, self.start_position, self.end_position)
    
    def parseList(self):
        list_node = ListNode(self.start_position, self.end_position)
        self.current_token = self.scanner.scan(self.source)
        
        while self.current_token != TokenType.RIGHT_BRACE or self.current_token != TokenType.NONE:
            pass
        
        if self.current_token == TokenType.RIGHT_BRACE:
            pass
        else:
            pass
    
    def positionToString(self, token):
        return 'line %s position %s' % (str(token.start_position), str(token.end_position))
    
    
    
    