# Generated from src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,118,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        4,4,43,8,4,11,4,12,4,44,1,5,4,5,48,8,5,11,5,12,5,49,1,6,4,6,53,8,
        6,11,6,12,6,54,1,7,4,7,58,8,7,11,7,12,7,59,1,8,4,8,63,8,8,11,8,12,
        8,64,1,9,4,9,68,8,9,11,9,12,9,69,1,10,4,10,73,8,10,11,10,12,10,74,
        1,11,1,11,1,11,3,11,80,8,11,1,12,1,12,1,12,5,12,85,8,12,10,12,12,
        12,88,9,12,1,12,1,12,1,13,1,13,1,13,5,13,95,8,13,10,13,12,13,98,
        9,13,1,13,1,13,1,14,1,14,1,14,5,14,105,8,14,10,14,12,14,108,9,14,
        1,14,1,14,1,15,4,15,113,8,15,11,15,12,15,114,1,15,1,15,0,0,16,1,
        1,3,2,5,3,7,4,9,5,11,6,13,0,15,0,17,0,19,0,21,0,23,0,25,7,27,8,29,
        9,31,10,1,0,8,2,0,9,9,32,32,9,0,9,10,13,13,32,32,34,34,39,39,59,
        60,62,62,96,96,124,124,4,0,10,10,34,34,39,39,96,96,2,0,10,10,39,
        39,2,0,10,10,34,34,2,0,10,10,96,96,3,0,10,10,34,34,96,96,3,0,9,10,
        13,13,32,32,127,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,0,0,5,37,1,0,0,0,7,39,1,0,0,0,
        9,42,1,0,0,0,11,47,1,0,0,0,13,52,1,0,0,0,15,57,1,0,0,0,17,62,1,0,
        0,0,19,67,1,0,0,0,21,72,1,0,0,0,23,79,1,0,0,0,25,81,1,0,0,0,27,91,
        1,0,0,0,29,101,1,0,0,0,31,112,1,0,0,0,33,34,5,59,0,0,34,2,1,0,0,
        0,35,36,5,60,0,0,36,4,1,0,0,0,37,38,5,62,0,0,38,6,1,0,0,0,39,40,
        5,124,0,0,40,8,1,0,0,0,41,43,7,0,0,0,42,41,1,0,0,0,43,44,1,0,0,0,
        44,42,1,0,0,0,44,45,1,0,0,0,45,10,1,0,0,0,46,48,8,1,0,0,47,46,1,
        0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,12,1,0,0,0,51,
        53,8,2,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,
        0,55,14,1,0,0,0,56,58,8,3,0,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,
        1,0,0,0,59,60,1,0,0,0,60,16,1,0,0,0,61,63,8,4,0,0,62,61,1,0,0,0,
        63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,18,1,0,0,0,66,68,8,
        5,0,0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        20,1,0,0,0,71,73,8,6,0,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,
        0,74,75,1,0,0,0,75,22,1,0,0,0,76,80,3,25,12,0,77,80,3,27,13,0,78,
        80,3,29,14,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,24,1,0,
        0,0,81,86,5,39,0,0,82,85,3,25,12,0,83,85,3,15,7,0,84,82,1,0,0,0,
        84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,
        0,0,0,88,86,1,0,0,0,89,90,5,39,0,0,90,26,1,0,0,0,91,96,5,34,0,0,
        92,95,3,27,13,0,93,95,3,17,8,0,94,92,1,0,0,0,94,93,1,0,0,0,95,98,
        1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,
        99,100,5,34,0,0,100,28,1,0,0,0,101,106,5,96,0,0,102,105,3,29,14,
        0,103,105,3,19,9,0,104,102,1,0,0,0,104,103,1,0,0,0,105,108,1,0,0,
        0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,0,
        0,109,110,5,96,0,0,110,30,1,0,0,0,111,113,7,7,0,0,112,111,1,0,0,
        0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,
        0,116,117,6,15,0,0,117,32,1,0,0,0,16,0,44,49,54,59,64,69,74,79,84,
        86,94,96,104,106,114,1,6,0,0
    ]

class ShellGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    WHITESPACE = 5
    UNQUOTED = 6
    SINGLE_QUOTED = 7
    DOUBLE_QUOTED = 8
    BACK_QUOTED = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'<'", "'>'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "WHITESPACE", "UNQUOTED", "SINGLE_QUOTED", "DOUBLE_QUOTED", 
            "BACK_QUOTED", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "WHITESPACE", "UNQUOTED", 
                  "NOT_QUOTED", "NOT_SINGLE_QUOTED", "NOT_DOUBLE_QUOTED", 
                  "NOT_BACK_QUOTED", "NOT_DOUBLE_BACK_QUOTED", "QUOTED", 
                  "SINGLE_QUOTED", "DOUBLE_QUOTED", "BACK_QUOTED", "WS" ]

    grammarFileName = "ShellGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


