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
        4,0,5,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,1,2,
        4,2,30,8,2,11,2,12,2,31,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,3,
        1,3,1,4,4,4,44,8,4,11,4,12,4,45,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,
        5,1,0,4,3,0,59,59,62,62,124,124,4,0,48,57,65,90,95,95,97,122,1,0,
        34,34,3,0,9,10,13,13,32,32,54,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,
        0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,26,1,0,0,0,5,29,1,0,0,0,
        7,33,1,0,0,0,9,43,1,0,0,0,11,12,7,0,0,0,12,2,1,0,0,0,13,14,5,101,
        0,0,14,15,5,99,0,0,15,16,5,104,0,0,16,27,5,111,0,0,17,18,5,108,0,
        0,18,27,5,115,0,0,19,20,5,103,0,0,20,21,5,114,0,0,21,22,5,101,0,
        0,22,27,5,112,0,0,23,24,5,99,0,0,24,25,5,97,0,0,25,27,5,116,0,0,
        26,13,1,0,0,0,26,17,1,0,0,0,26,19,1,0,0,0,26,23,1,0,0,0,27,4,1,0,
        0,0,28,30,7,1,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,6,1,0,0,0,33,37,5,34,0,0,34,36,8,2,0,0,35,34,1,0,0,0,
        36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,
        0,0,0,40,41,5,34,0,0,41,8,1,0,0,0,42,44,7,3,0,0,43,42,1,0,0,0,44,
        45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,6,4,0,
        0,48,10,1,0,0,0,5,0,26,31,37,45,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPERATOR = 1
    CMD = 2
    UNQUOTED_STRING = 3
    STRING = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "OPERATOR", "CMD", "UNQUOTED_STRING", "STRING", "WS" ]

    ruleNames = [ "OPERATOR", "CMD", "UNQUOTED_STRING", "STRING", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


