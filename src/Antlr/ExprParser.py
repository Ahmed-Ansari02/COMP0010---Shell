# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,4,2,23,8,2,11,2,12,2,
        24,1,2,5,2,28,8,2,10,2,12,2,31,9,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,
        1,0,3,4,34,0,11,1,0,0,0,2,19,1,0,0,0,4,22,1,0,0,0,6,32,1,0,0,0,8,
        10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,
        12,1,1,0,0,0,13,11,1,0,0,0,14,20,3,4,2,0,15,16,3,4,2,0,16,17,5,1,
        0,0,17,18,3,2,1,0,18,20,1,0,0,0,19,14,1,0,0,0,19,15,1,0,0,0,20,3,
        1,0,0,0,21,23,5,2,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,
        24,25,1,0,0,0,25,29,1,0,0,0,26,28,3,6,3,0,27,26,1,0,0,0,28,31,1,
        0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,5,1,0,0,0,31,29,1,0,0,0,32,
        33,7,0,0,0,33,7,1,0,0,0,4,11,19,24,29
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "OPERATOR", "CMD", "UNQUOTED_STRING", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_command = 1
    RULE_simpleCommand = 2
    RULE_arg = 3

    ruleNames =  [ "program", "command", "simpleCommand", "arg" ]

    EOF = Token.EOF
    OPERATOR=1
    CMD=2
    UNQUOTED_STRING=3
    STRING=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CommandContext)
            else:
                return self.getTypedRuleContext(ExprParser.CommandContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 8
                self.command()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleCommand(self):
            return self.getTypedRuleContext(ExprParser.SimpleCommandContext,0)


        def OPERATOR(self):
            return self.getToken(ExprParser.OPERATOR, 0)

        def command(self):
            return self.getTypedRuleContext(ExprParser.CommandContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.simpleCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.simpleCommand()
                self.state = 16
                self.match(ExprParser.OPERATOR)
                self.state = 17
                self.command()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMD(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CMD)
            else:
                return self.getToken(ExprParser.CMD, i)

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArgContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArgContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_simpleCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleCommand" ):
                listener.enterSimpleCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleCommand" ):
                listener.exitSimpleCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleCommand" ):
                return visitor.visitSimpleCommand(self)
            else:
                return visitor.visitChildren(self)




    def simpleCommand(self):

        localctx = ExprParser.SimpleCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 21
                    self.match(ExprParser.CMD)

                else:
                    raise NoViableAltException(self)
                self.state = 24 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 26
                self.arg()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def UNQUOTED_STRING(self):
            return self.getToken(ExprParser.UNQUOTED_STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ExprParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





