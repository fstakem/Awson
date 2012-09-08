#  ---------------------------------------------------------------------------
#                                                                           
#                               T O K E N  T Y P E                                 
#                                                                           
#  ---------------------------------------------------------------------------

#  By: Fred Stakem 
#  Date: 9.4.12

# Libraries
import logging

# Classes
import Utilities

class TokenType(object):
    """This class represents a token type that is found in a scanned file."""
       
    # Setup logging
    logger = Utilities.getLogger('TokenType')
    
    # Class constants
    NONE = 0
    OBJECT = 1
    PROPERTY = 2
    AGGREGATE_PROPERTY = 3
    INT = 4
    FLOAT = 5
    STRING = 6
    BOOL_TRUE = 7
    BOOL_FALSE = 8
    CODE = 9
    LEFT_BRACE = 10
    RIGHT_BRACE = 11
    
    readable_name = {
                     TokenType.NONE:                'None',
                     TokenType.OBJECT:              'Object',
                     TokenType.PROPERTY:            'Property',
                     TokenType.AGGREGATE_PROPERTY:  'Aggregate Property',
                     TokenType.INT:                 'Integer',
                     TokenType.FLOAT:               'Float',
                     TokenType.STRING:              'String',
                     TokenType.BOOL_TRUE:           'Boolean True',
                     TokenType.BOOL_FALSE:          'Boolean False',
                     TokenType.CODE:                'Code',
                     TokenType.LEFT_BRACE:          'Left Brace',
                     TokenType.RIGHT_BRACE:         'Right Brace',
                    }
    
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
    def prettyPrint(cls, type):
        return cls.readable_name[type]
    
    
    
    