# Generated from src/Antlr/Expr.g4 by ANTLR 4.13.1
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
        4,1,10,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,1,0,1,0,1,0,3,0,22,8,0,1,0,3,0,25,8,0,1,1,1,
        1,1,1,3,1,30,8,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,3,3,54,8,
        3,1,3,1,3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,3,1,3,1,3,5,3,67,8,3,
        10,3,12,3,70,9,3,1,3,3,3,73,8,3,1,4,1,4,3,4,77,8,4,1,5,1,5,5,5,81,
        8,5,10,5,12,5,84,9,5,1,6,1,6,1,6,0,2,2,4,7,0,2,4,6,8,10,12,0,1,1,
        0,7,9,93,0,24,1,0,0,0,2,29,1,0,0,0,4,39,1,0,0,0,6,53,1,0,0,0,8,76,
        1,0,0,0,10,82,1,0,0,0,12,85,1,0,0,0,14,16,5,1,0,0,15,17,5,5,0,0,
        16,15,1,0,0,0,16,17,1,0,0,0,17,18,1,0,0,0,18,25,3,10,5,0,19,21,5,
        2,0,0,20,22,5,5,0,0,21,20,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,
        25,3,10,5,0,24,14,1,0,0,0,24,19,1,0,0,0,25,1,1,0,0,0,26,27,6,1,-1,
        0,27,30,3,4,2,0,28,30,3,6,3,0,29,26,1,0,0,0,29,28,1,0,0,0,30,36,
        1,0,0,0,31,32,10,2,0,0,32,33,5,3,0,0,33,35,3,2,1,3,34,31,1,0,0,0,
        35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,36,1,0,
        0,0,39,40,6,2,-1,0,40,41,3,6,3,0,41,42,5,4,0,0,42,43,3,6,3,0,43,
        49,1,0,0,0,44,45,10,1,0,0,45,46,5,4,0,0,46,48,3,6,3,0,47,44,1,0,
        0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,49,
        1,0,0,0,52,54,5,5,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,60,1,0,0,0,
        55,56,3,0,0,0,56,57,5,5,0,0,57,59,1,0,0,0,58,55,1,0,0,0,59,62,1,
        0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,
        68,3,10,5,0,64,65,5,5,0,0,65,67,3,8,4,0,66,64,1,0,0,0,67,70,1,0,
        0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,71,73,
        5,5,0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,7,1,0,0,0,74,77,3,0,0,0,75,
        77,3,10,5,0,76,74,1,0,0,0,76,75,1,0,0,0,77,9,1,0,0,0,78,81,3,12,
        6,0,79,81,5,6,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,
        1,0,0,0,82,83,1,0,0,0,83,11,1,0,0,0,84,82,1,0,0,0,85,86,7,0,0,0,
        86,13,1,0,0,0,13,16,21,24,29,36,49,53,60,68,72,76,80,82
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "';'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WHITESPACE", "UNQUOTED", "SINGLE_QUOTED", 
                      "DOUBLE_QUOTED", "BACK_QUOTED", "WS" ]

    RULE_redirection = 0
    RULE_command = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_atom = 4
    RULE_argument = 5
    RULE_quoted = 6

    ruleNames =  [ "redirection", "command", "pipe", "call", "atom", "argument", 
                   "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WHITESPACE=5
    UNQUOTED=6
    SINGLE_QUOTED=7
    DOUBLE_QUOTED=8
    BACK_QUOTED=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ExprParser.ArgumentContext,0)


        def WHITESPACE(self):
            return self.getToken(ExprParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_redirection

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

        localctx = ExprParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_redirection)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(ExprParser.T__0)
                self.state = 16
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 15
                    self.match(ExprParser.WHITESPACE)


                self.state = 18
                self.argument()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(ExprParser.T__1)
                self.state = 21
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.match(ExprParser.WHITESPACE)


                self.state = 23
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


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(ExprParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(ExprParser.CallContext,0)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CommandContext)
            else:
                return self.getTypedRuleContext(ExprParser.CommandContext,i)


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



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 27
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 28
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 31
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 32
                    self.match(ExprParser.T__2)
                    self.state = 33
                    self.command(3) 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CallContext)
            else:
                return self.getTypedRuleContext(ExprParser.CallContext,i)


        def pipe(self):
            return self.getTypedRuleContext(ExprParser.PipeContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_pipe

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
        localctx = ExprParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.call()
            self.state = 41
            self.match(ExprParser.T__3)
            self.state = 42
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 44
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 45
                    self.match(ExprParser.T__3)
                    self.state = 46
                    self.call() 
                self.state = 51
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

        def argument(self):
            return self.getTypedRuleContext(ExprParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.WHITESPACE)
            else:
                return self.getToken(ExprParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ExprParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AtomContext)
            else:
                return self.getTypedRuleContext(ExprParser.AtomContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_call

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

        localctx = ExprParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 52
                self.match(ExprParser.WHITESPACE)


            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self.redirection()
                    self.state = 56
                    self.match(ExprParser.WHITESPACE) 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 63
            self.argument()
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.match(ExprParser.WHITESPACE)
                    self.state = 65
                    self.atom() 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(ExprParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(ExprParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(ExprParser.ArgumentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.redirection()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.argument()
                pass


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

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.QuotedContext)
            else:
                return self.getTypedRuleContext(ExprParser.QuotedContext,i)


        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.UNQUOTED)
            else:
                return self.getToken(ExprParser.UNQUOTED, i)

        def getRuleIndex(self):
            return ExprParser.RULE_argument

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

        localctx = ExprParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 8, 9]:
                        self.state = 78
                        self.quoted()
                        pass
                    elif token in [6]:
                        self.state = 79
                        self.match(ExprParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 84
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
            return self.getToken(ExprParser.SINGLE_QUOTED, 0)

        def DOUBLE_QUOTED(self):
            return self.getToken(ExprParser.DOUBLE_QUOTED, 0)

        def BACK_QUOTED(self):
            return self.getToken(ExprParser.BACK_QUOTED, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_quoted

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

        localctx = ExprParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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
        self._predicates[2] = self.pipe_sempred
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
         




