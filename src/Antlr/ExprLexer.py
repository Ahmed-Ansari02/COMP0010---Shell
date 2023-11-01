# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,64,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,31,8,1,1,2,4,2,34,8,2,11,2,12,2,35,1,3,4,3,39,8,3,11,3,12,
        3,40,1,3,1,3,4,3,45,8,3,11,3,12,3,46,1,4,1,4,5,4,51,8,4,10,4,12,
        4,54,9,4,1,4,1,4,1,5,4,5,59,8,5,11,5,12,5,60,1,5,1,5,0,0,6,1,1,3,
        2,5,3,7,4,9,5,11,6,1,0,4,3,0,59,59,62,62,124,124,4,0,48,57,65,90,
        95,95,97,122,1,0,34,34,3,0,9,10,13,13,32,32,72,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,
        0,0,3,30,1,0,0,0,5,33,1,0,0,0,7,38,1,0,0,0,9,48,1,0,0,0,11,58,1,
        0,0,0,13,14,7,0,0,0,14,2,1,0,0,0,15,16,5,101,0,0,16,17,5,99,0,0,
        17,18,5,104,0,0,18,31,5,111,0,0,19,20,5,108,0,0,20,31,5,115,0,0,
        21,22,5,103,0,0,22,23,5,114,0,0,23,24,5,101,0,0,24,31,5,112,0,0,
        25,26,5,99,0,0,26,27,5,97,0,0,27,31,5,116,0,0,28,29,5,99,0,0,29,
        31,5,100,0,0,30,15,1,0,0,0,30,19,1,0,0,0,30,21,1,0,0,0,30,25,1,0,
        0,0,30,28,1,0,0,0,31,4,1,0,0,0,32,34,7,1,0,0,33,32,1,0,0,0,34,35,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,6,1,0,0,0,37,39,7,1,0,0,38,
        37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,
        0,42,44,5,46,0,0,43,45,7,1,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,
        1,0,0,0,46,47,1,0,0,0,47,8,1,0,0,0,48,52,5,34,0,0,49,51,8,2,0,0,
        50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,
        0,0,0,54,52,1,0,0,0,55,56,5,34,0,0,56,10,1,0,0,0,57,59,7,3,0,0,58,
        57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,
        0,62,63,6,5,0,0,63,12,1,0,0,0,7,0,30,35,40,46,52,60,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPERATOR = 1
    CMD = 2
    UNQUOTED_STRING = 3
    FIlE = 4
    STRING = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "OPERATOR", "CMD", "UNQUOTED_STRING", "FIlE", "STRING", "WS" ]

    ruleNames = [ "OPERATOR", "CMD", "UNQUOTED_STRING", "FIlE", "STRING", 
                  "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


