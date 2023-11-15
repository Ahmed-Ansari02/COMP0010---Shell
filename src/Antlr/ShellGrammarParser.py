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
        4,1,11,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,1,1,5,1,26,8,1,10,1,
        12,1,29,9,1,1,2,1,2,3,2,33,8,2,1,2,1,2,1,2,3,2,38,8,2,1,2,3,2,41,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,
        1,4,3,4,57,8,4,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,4,1,4,1,
        4,1,4,3,4,71,8,4,5,4,73,8,4,10,4,12,4,76,9,4,1,4,3,4,79,8,4,1,5,
        1,5,1,5,4,5,84,8,5,11,5,12,5,85,1,6,1,6,1,6,0,2,2,6,7,0,2,4,6,8,
        10,12,0,1,1,0,8,10,96,0,14,1,0,0,0,2,20,1,0,0,0,4,40,1,0,0,0,6,42,
        1,0,0,0,8,56,1,0,0,0,10,83,1,0,0,0,12,87,1,0,0,0,14,15,3,2,1,0,15,
        16,5,0,0,1,16,1,1,0,0,0,17,18,6,1,-1,0,18,21,3,6,3,0,19,21,3,8,4,
        0,20,17,1,0,0,0,20,19,1,0,0,0,21,27,1,0,0,0,22,23,10,2,0,0,23,24,
        5,1,0,0,24,26,3,2,1,3,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,3,1,0,0,0,29,27,1,0,0,0,30,32,5,2,0,0,31,33,5,5,
        0,0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,41,3,10,5,0,35,
        37,5,3,0,0,36,38,5,5,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,
        0,39,41,3,10,5,0,40,30,1,0,0,0,40,35,1,0,0,0,41,5,1,0,0,0,42,43,
        6,3,-1,0,43,44,3,8,4,0,44,45,5,4,0,0,45,46,3,8,4,0,46,52,1,0,0,0,
        47,48,10,1,0,0,48,49,5,4,0,0,49,51,3,8,4,0,50,47,1,0,0,0,51,54,1,
        0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,7,1,0,0,0,54,52,1,0,0,0,55,
        57,5,5,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,63,1,0,0,0,58,59,3,4,2,
        0,59,60,5,5,0,0,60,62,1,0,0,0,61,58,1,0,0,0,62,65,1,0,0,0,63,61,
        1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,74,3,10,5,0,
        67,70,5,5,0,0,68,71,3,4,2,0,69,71,3,10,5,0,70,68,1,0,0,0,70,69,1,
        0,0,0,71,73,1,0,0,0,72,67,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,
        75,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,77,79,5,5,0,0,78,77,1,0,0,
        0,78,79,1,0,0,0,79,9,1,0,0,0,80,84,5,6,0,0,81,84,5,7,0,0,82,84,3,
        12,6,0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,85,1,0,0,0,85,
        83,1,0,0,0,85,86,1,0,0,0,86,11,1,0,0,0,87,88,7,0,0,0,88,13,1,0,0,
        0,13,20,27,32,37,40,52,56,63,70,74,78,83,85
    ]

class ShellGrammarParser ( Parser ):

    grammarFileName = "ShellGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'<'", "'>'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WHITESPACE", "APPLICATION", "UNQUOTED", 
                      "SINGLE_QUOTED", "DOUBLE_QUOTED", "BACK_QUOTED", "WS" ]

    RULE_s = 0
    RULE_command = 1
    RULE_redirection = 2
    RULE_pipe = 3
    RULE_call = 4
    RULE_argument = 5
    RULE_quoted = 6

    ruleNames =  [ "s", "command", "redirection", "pipe", "call", "argument", 
                   "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WHITESPACE=5
    APPLICATION=6
    UNQUOTED=7
    SINGLE_QUOTED=8
    DOUBLE_QUOTED=9
    BACK_QUOTED=10
    WS=11

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
            self.state = 14
            self.command(0)
            self.state = 15
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
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 19
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ShellGrammarParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 22
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 23
                    self.match(ShellGrammarParser.T__0)
                    self.state = 24
                    self.command(3) 
                self.state = 29
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(ShellGrammarParser.T__1)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 31
                    self.match(ShellGrammarParser.WHITESPACE)


                self.state = 34
                self.argument()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(ShellGrammarParser.T__2)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 36
                    self.match(ShellGrammarParser.WHITESPACE)


                self.state = 39
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
            self.state = 43
            self.call()
            self.state = 44
            self.match(ShellGrammarParser.T__3)
            self.state = 45
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ShellGrammarParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 47
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 48
                    self.match(ShellGrammarParser.T__3)
                    self.state = 49
                    self.call() 
                self.state = 54
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
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 55
                self.match(ShellGrammarParser.WHITESPACE)


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 58
                self.redirection()
                self.state = 59
                self.match(ShellGrammarParser.WHITESPACE)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.argument()
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self.match(ShellGrammarParser.WHITESPACE)
                    self.state = 70
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2, 3]:
                        self.state = 68
                        self.redirection()
                        pass
                    elif token in [6, 7, 8, 9, 10]:
                        self.state = 69
                        self.argument()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 77
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
            self.state = 83 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 83
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6]:
                        self.state = 80
                        self.match(ShellGrammarParser.APPLICATION)
                        pass
                    elif token in [7]:
                        self.state = 81
                        self.match(ShellGrammarParser.UNQUOTED)
                        pass
                    elif token in [8, 9, 10]:
                        self.state = 82
                        self.quoted()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 85 
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

        def SINGLE_QUOTED(self):
            return self.getToken(ShellGrammarParser.SINGLE_QUOTED, 0)

        def BACK_QUOTED(self):
            return self.getToken(ShellGrammarParser.BACK_QUOTED, 0)

        def DOUBLE_QUOTED(self):
            return self.getToken(ShellGrammarParser.DOUBLE_QUOTED, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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
         




