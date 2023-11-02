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
        4,1,10,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,3,0,18,8,0,1,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,2,
        3,2,42,8,2,1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,2,5,
        2,55,8,2,10,2,12,2,58,9,2,1,2,3,2,61,8,2,1,3,1,3,3,3,65,8,3,1,4,
        1,4,4,4,69,8,4,11,4,12,4,70,1,5,1,5,3,5,75,8,5,1,5,1,5,1,5,3,5,80,
        8,5,1,5,3,5,83,8,5,1,6,1,6,1,6,0,2,0,2,7,0,2,4,6,8,10,12,0,1,1,0,
        7,9,92,0,17,1,0,0,0,2,27,1,0,0,0,4,41,1,0,0,0,6,64,1,0,0,0,8,68,
        1,0,0,0,10,82,1,0,0,0,12,84,1,0,0,0,14,15,6,0,-1,0,15,18,3,2,1,0,
        16,18,3,4,2,0,17,14,1,0,0,0,17,16,1,0,0,0,18,24,1,0,0,0,19,20,10,
        2,0,0,20,21,5,1,0,0,21,23,3,0,0,3,22,19,1,0,0,0,23,26,1,0,0,0,24,
        22,1,0,0,0,24,25,1,0,0,0,25,1,1,0,0,0,26,24,1,0,0,0,27,28,6,1,-1,
        0,28,29,3,4,2,0,29,30,5,2,0,0,30,31,3,4,2,0,31,37,1,0,0,0,32,33,
        10,1,0,0,33,34,5,2,0,0,34,36,3,4,2,0,35,32,1,0,0,0,36,39,1,0,0,0,
        37,35,1,0,0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,37,1,0,0,0,40,42,5,5,
        0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,48,1,0,0,0,43,44,3,10,5,0,44,
        45,5,5,0,0,45,47,1,0,0,0,46,43,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,
        0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,56,3,8,4,0,52,53,
        5,5,0,0,53,55,3,6,3,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,
        56,57,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,59,61,5,5,0,0,60,59,1,
        0,0,0,60,61,1,0,0,0,61,5,1,0,0,0,62,65,3,10,5,0,63,65,3,8,4,0,64,
        62,1,0,0,0,64,63,1,0,0,0,65,7,1,0,0,0,66,69,3,12,6,0,67,69,5,6,0,
        0,68,66,1,0,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,9,1,0,0,0,72,74,5,3,0,0,73,75,5,5,0,0,74,73,1,0,0,0,74,
        75,1,0,0,0,75,76,1,0,0,0,76,83,3,8,4,0,77,79,5,4,0,0,78,80,5,5,0,
        0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,83,3,8,4,0,82,72,
        1,0,0,0,82,77,1,0,0,0,83,11,1,0,0,0,84,85,7,0,0,0,85,13,1,0,0,0,
        13,17,24,37,41,48,56,60,64,68,70,74,79,82
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'|'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WHITESPACE", "UNQUOTED", "SINGLE_QUOTED", 
                      "DOUBLEQUOTED", "BACKQUOTED", "WS" ]

    RULE_command = 0
    RULE_pipe = 1
    RULE_call = 2
    RULE_atom = 3
    RULE_argument = 4
    RULE_redirection = 5
    RULE_quoted = 6

    ruleNames =  [ "command", "pipe", "call", "atom", "argument", "redirection", 
                   "quoted" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WHITESPACE=5
    UNQUOTED=6
    SINGLE_QUOTED=7
    DOUBLEQUOTED=8
    BACKQUOTED=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 15
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 16
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 19
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 20
                    self.match(ExprParser.T__0)
                    self.state = 21
                    self.command(3) 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.call()
            self.state = 29
            self.match(ExprParser.T__1)
            self.state = 30
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 32
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 33
                    self.match(ExprParser.T__1)
                    self.state = 34
                    self.call() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 40
                self.match(ExprParser.WHITESPACE)


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 43
                self.redirection()
                self.state = 44
                self.match(ExprParser.WHITESPACE)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.argument()
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self.match(ExprParser.WHITESPACE)
                    self.state = 53
                    self.atom() 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 59
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
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.redirection()
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
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
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 68
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 8, 9]:
                        self.state = 66
                        self.quoted()
                        pass
                    elif token in [6]:
                        self.state = 67
                        self.match(ExprParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(ExprParser.T__2)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 73
                    self.match(ExprParser.WHITESPACE)


                self.state = 76
                self.argument()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(ExprParser.T__3)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 78
                    self.match(ExprParser.WHITESPACE)


                self.state = 81
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


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED(self):
            return self.getToken(ExprParser.SINGLE_QUOTED, 0)

        def DOUBLEQUOTED(self):
            return self.getToken(ExprParser.DOUBLEQUOTED, 0)

        def BACKQUOTED(self):
            return self.getToken(ExprParser.BACKQUOTED, 0)

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
            self.state = 84
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
        self._predicates[0] = self.command_sempred
        self._predicates[1] = self.pipe_sempred
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
         




