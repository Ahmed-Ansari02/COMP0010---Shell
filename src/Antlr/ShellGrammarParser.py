# Generated from src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
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
        4,1,12,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,1,1,3,1,27,8,1,1,1,
        1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,3,2,39,8,2,1,2,1,2,1,
        2,3,2,44,8,2,1,2,3,2,47,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        57,8,3,10,3,12,3,60,9,3,1,4,3,4,63,8,4,1,4,1,4,1,4,5,4,68,8,4,10,
        4,12,4,71,9,4,1,4,1,4,1,4,1,4,3,4,77,8,4,5,4,79,8,4,10,4,12,4,82,
        9,4,1,4,3,4,85,8,4,1,5,1,5,1,5,4,5,90,8,5,11,5,12,5,91,1,6,1,6,1,
        6,3,6,97,8,6,1,7,1,7,1,8,1,8,4,8,103,8,8,11,8,12,8,104,1,8,1,8,3,
        8,109,8,8,1,9,1,9,1,9,0,2,2,6,10,0,2,4,6,8,10,12,14,16,18,0,1,2,
        0,8,8,10,10,120,0,20,1,0,0,0,2,26,1,0,0,0,4,46,1,0,0,0,6,48,1,0,
        0,0,8,62,1,0,0,0,10,89,1,0,0,0,12,96,1,0,0,0,14,98,1,0,0,0,16,108,
        1,0,0,0,18,110,1,0,0,0,20,21,3,2,1,0,21,22,5,0,0,1,22,1,1,0,0,0,
        23,24,6,1,-1,0,24,27,3,6,3,0,25,27,3,8,4,0,26,23,1,0,0,0,26,25,1,
        0,0,0,27,33,1,0,0,0,28,29,10,2,0,0,29,30,5,1,0,0,30,32,3,2,1,3,31,
        28,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,
        0,35,33,1,0,0,0,36,38,5,2,0,0,37,39,5,6,0,0,38,37,1,0,0,0,38,39,
        1,0,0,0,39,40,1,0,0,0,40,47,3,10,5,0,41,43,5,3,0,0,42,44,5,6,0,0,
        43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,47,3,10,5,0,46,36,1,
        0,0,0,46,41,1,0,0,0,47,5,1,0,0,0,48,49,6,3,-1,0,49,50,3,8,4,0,50,
        51,5,4,0,0,51,52,3,8,4,0,52,58,1,0,0,0,53,54,10,1,0,0,54,55,5,4,
        0,0,55,57,3,8,4,0,56,53,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,7,1,0,0,0,60,58,1,0,0,0,61,63,5,6,0,0,62,61,1,0,0,0,62,
        63,1,0,0,0,63,69,1,0,0,0,64,65,3,4,2,0,65,66,5,6,0,0,66,68,1,0,0,
        0,67,64,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,
        1,0,0,0,71,69,1,0,0,0,72,80,3,10,5,0,73,76,5,6,0,0,74,77,3,4,2,0,
        75,77,3,10,5,0,76,74,1,0,0,0,76,75,1,0,0,0,77,79,1,0,0,0,78,73,1,
        0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,84,1,0,0,0,82,
        80,1,0,0,0,83,85,5,6,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,9,1,0,0,
        0,86,90,5,7,0,0,87,90,5,8,0,0,88,90,3,12,6,0,89,86,1,0,0,0,89,87,
        1,0,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,
        92,11,1,0,0,0,93,97,3,14,7,0,94,97,3,18,9,0,95,97,3,16,8,0,96,93,
        1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,13,1,0,0,0,98,99,5,9,0,0,
        99,15,1,0,0,0,100,102,5,5,0,0,101,103,7,0,0,0,102,101,1,0,0,0,103,
        104,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,
        109,5,5,0,0,107,109,5,10,0,0,108,100,1,0,0,0,108,107,1,0,0,0,109,
        17,1,0,0,0,110,111,5,11,0,0,111,19,1,0,0,0,16,26,33,38,43,46,58,
        62,69,76,80,84,89,91,96,104,108
    ]

class ShellGrammarParser ( Parser ):

    grammarFileName = "ShellGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'<'", "'>'", "'|'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WHITESPACE", "APPLICATION", 
                      "UNQUOTED", "SINGLE_QUOTED", "DOUBLE_QUOTED", "BACK_QUOTED", 
                      "WS" ]

    RULE_s = 0
    RULE_command = 1
    RULE_redirection = 2
    RULE_pipe = 3
    RULE_call = 4
    RULE_argument = 5
    RULE_quoted = 6
    RULE_single_quoted = 7
    RULE_double_quoted = 8
    RULE_back_quoted = 9

    ruleNames =  [ "s", "command", "redirection", "pipe", "call", "argument", 
                   "quoted", "single_quoted", "double_quoted", "back_quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    WHITESPACE=6
    APPLICATION=7
    UNQUOTED=8
    SINGLE_QUOTED=9
    DOUBLE_QUOTED=10
    BACK_QUOTED=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ShellGrammarParser.CommandContext,0)


        def EOF(self):
            return self.getToken(ShellGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = ShellGrammarParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.command(0)
            self.state = 21
            self.match(ShellGrammarParser.EOF)
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

        def pipe(self):
            return self.getTypedRuleContext(ShellGrammarParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(ShellGrammarParser.CallContext,0)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.CommandContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.CommandContext,i)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_command

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



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShellGrammarParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 24
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 25
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ShellGrammarParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 28
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 29
                    self.match(ShellGrammarParser.T__0)
                    self.state = 30
                    self.command(3) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ShellGrammarParser.ArgumentContext,0)


        def WHITESPACE(self):
            return self.getToken(ShellGrammarParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = ShellGrammarParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(ShellGrammarParser.T__1)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 37
                    self.match(ShellGrammarParser.WHITESPACE)


                self.state = 40
                self.argument()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(ShellGrammarParser.T__2)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 42
                    self.match(ShellGrammarParser.WHITESPACE)


                self.state = 45
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.CallContext,i)


        def pipe(self):
            return self.getTypedRuleContext(ShellGrammarParser.PipeContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShellGrammarParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.call()
            self.state = 50
            self.match(ShellGrammarParser.T__3)
            self.state = 51
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ShellGrammarParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 53
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 54
                    self.match(ShellGrammarParser.T__3)
                    self.state = 55
                    self.call() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.ArgumentContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WHITESPACE)
            else:
                return self.getToken(ShellGrammarParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.RedirectionContext,i)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ShellGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 61
                self.match(ShellGrammarParser.WHITESPACE)


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 64
                self.redirection()
                self.state = 65
                self.match(ShellGrammarParser.WHITESPACE)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.argument()
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 73
                    self.match(ShellGrammarParser.WHITESPACE)
                    self.state = 76
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2, 3]:
                        self.state = 74
                        self.redirection()
                        pass
                    elif token in [5, 7, 8, 9, 10, 11]:
                        self.state = 75
                        self.argument()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 83
                self.match(ShellGrammarParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APPLICATION(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.APPLICATION)
            else:
                return self.getToken(ShellGrammarParser.APPLICATION, i)

        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.UNQUOTED)
            else:
                return self.getToken(ShellGrammarParser.UNQUOTED, i)

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.QuotedContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.QuotedContext,i)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ShellGrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 86
                        self.match(ShellGrammarParser.APPLICATION)
                        pass
                    elif token in [8]:
                        self.state = 87
                        self.match(ShellGrammarParser.UNQUOTED)
                        pass
                    elif token in [5, 9, 10, 11]:
                        self.state = 88
                        self.quoted()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 91 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.Single_quotedContext,0)


        def back_quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.Back_quotedContext,0)


        def double_quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.Double_quotedContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = ShellGrammarParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quoted)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.single_quoted()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.back_quoted()
                pass
            elif token in [5, 10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.double_quoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED(self):
            return self.getToken(ShellGrammarParser.SINGLE_QUOTED, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_single_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_quoted" ):
                listener.enterSingle_quoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_quoted" ):
                listener.exitSingle_quoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_quoted" ):
                return visitor.visitSingle_quoted(self)
            else:
                return visitor.visitChildren(self)




    def single_quoted(self):

        localctx = ShellGrammarParser.Single_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_single_quoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ShellGrammarParser.SINGLE_QUOTED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Double_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.DOUBLE_QUOTED)
            else:
                return self.getToken(ShellGrammarParser.DOUBLE_QUOTED, i)

        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.UNQUOTED)
            else:
                return self.getToken(ShellGrammarParser.UNQUOTED, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_double_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble_quoted" ):
                listener.enterDouble_quoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble_quoted" ):
                listener.exitDouble_quoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble_quoted" ):
                return visitor.visitDouble_quoted(self)
            else:
                return visitor.visitChildren(self)




    def double_quoted(self):

        localctx = ShellGrammarParser.Double_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_double_quoted)
        self._la = 0 # Token type
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(ShellGrammarParser.T__4)
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 101
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 104 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==8 or _la==10):
                        break

                self.state = 106
                self.match(ShellGrammarParser.T__4)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(ShellGrammarParser.DOUBLE_QUOTED)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Back_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACK_QUOTED(self):
            return self.getToken(ShellGrammarParser.BACK_QUOTED, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_back_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBack_quoted" ):
                listener.enterBack_quoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBack_quoted" ):
                listener.exitBack_quoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBack_quoted" ):
                return visitor.visitBack_quoted(self)
            else:
                return visitor.visitChildren(self)




    def back_quoted(self):

        localctx = ShellGrammarParser.Back_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_back_quoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ShellGrammarParser.BACK_QUOTED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.command_sempred
        self._predicates[3] = self.pipe_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




