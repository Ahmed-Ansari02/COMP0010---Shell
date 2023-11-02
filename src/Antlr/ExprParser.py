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
        4,1,15,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,1,1,1,1,1,3,1,40,8,1,
        1,1,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,3,3,64,8,3,1,3,1,3,1,3,5,
        3,69,8,3,10,3,12,3,72,9,3,1,3,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,
        9,3,1,3,3,3,84,8,3,1,4,1,4,1,5,1,5,3,5,90,8,5,1,6,1,6,4,6,94,8,6,
        11,6,12,6,95,1,7,1,7,3,7,100,8,7,1,7,1,7,1,7,3,7,105,8,7,1,7,3,7,
        108,8,7,1,8,1,8,1,8,3,8,113,8,8,1,9,1,9,5,9,117,8,9,10,9,12,9,120,
        9,9,1,9,1,9,1,10,1,10,1,10,5,10,127,8,10,10,10,12,10,130,9,10,1,
        10,1,10,1,11,1,11,1,12,1,12,5,12,138,8,12,10,12,12,12,141,9,12,1,
        12,1,12,1,13,4,13,146,8,13,11,13,12,13,147,1,14,1,14,1,14,0,2,2,
        4,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,4,1,0,6,7,1,0,7,9,
        2,0,1,2,4,11,1,0,12,15,157,0,33,1,0,0,0,2,39,1,0,0,0,4,49,1,0,0,
        0,6,63,1,0,0,0,8,85,1,0,0,0,10,89,1,0,0,0,12,93,1,0,0,0,14,107,1,
        0,0,0,16,112,1,0,0,0,18,114,1,0,0,0,20,123,1,0,0,0,22,133,1,0,0,
        0,24,135,1,0,0,0,26,145,1,0,0,0,28,149,1,0,0,0,30,32,3,2,1,0,31,
        30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,
        0,35,33,1,0,0,0,36,37,6,1,-1,0,37,40,3,4,2,0,38,40,3,6,3,0,39,36,
        1,0,0,0,39,38,1,0,0,0,40,46,1,0,0,0,41,42,10,2,0,0,42,43,5,1,0,0,
        43,45,3,2,1,3,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,
        0,0,0,47,3,1,0,0,0,48,46,1,0,0,0,49,50,6,2,-1,0,50,51,3,6,3,0,51,
        52,5,2,0,0,52,53,3,6,3,0,53,59,1,0,0,0,54,55,10,1,0,0,55,56,5,2,
        0,0,56,58,3,6,3,0,57,54,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,
        1,0,0,0,60,5,1,0,0,0,61,59,1,0,0,0,62,64,3,8,4,0,63,62,1,0,0,0,63,
        64,1,0,0,0,64,70,1,0,0,0,65,66,3,14,7,0,66,67,3,8,4,0,67,69,1,0,
        0,0,68,65,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,
        1,0,0,0,72,70,1,0,0,0,73,79,3,12,6,0,74,75,3,8,4,0,75,76,3,10,5,
        0,76,78,1,0,0,0,77,74,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,
        1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,82,84,3,8,4,0,83,82,1,0,0,0,
        83,84,1,0,0,0,84,7,1,0,0,0,85,86,5,3,0,0,86,9,1,0,0,0,87,90,3,14,
        7,0,88,90,3,12,6,0,89,87,1,0,0,0,89,88,1,0,0,0,90,11,1,0,0,0,91,
        94,3,16,8,0,92,94,3,26,13,0,93,91,1,0,0,0,93,92,1,0,0,0,94,95,1,
        0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,13,1,0,0,0,97,99,5,4,0,0,98,
        100,3,8,4,0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,108,
        3,12,6,0,102,104,5,5,0,0,103,105,3,8,4,0,104,103,1,0,0,0,104,105,
        1,0,0,0,105,106,1,0,0,0,106,108,3,12,6,0,107,97,1,0,0,0,107,102,
        1,0,0,0,108,15,1,0,0,0,109,113,3,18,9,0,110,113,3,20,10,0,111,113,
        3,24,12,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,17,
        1,0,0,0,114,118,5,6,0,0,115,117,8,0,0,0,116,115,1,0,0,0,117,120,
        1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,118,
        1,0,0,0,121,122,5,6,0,0,122,19,1,0,0,0,123,128,5,8,0,0,124,127,3,
        24,12,0,125,127,3,22,11,0,126,124,1,0,0,0,126,125,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,
        1,0,0,0,131,132,5,8,0,0,132,21,1,0,0,0,133,134,8,1,0,0,134,23,1,
        0,0,0,135,139,5,9,0,0,136,138,8,0,0,0,137,136,1,0,0,0,138,141,1,
        0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,
        0,0,0,142,143,5,9,0,0,143,25,1,0,0,0,144,146,8,2,0,0,145,144,1,0,
        0,0,146,147,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,27,1,0,0,
        0,149,150,7,3,0,0,150,29,1,0,0,0,20,33,39,46,59,63,70,79,83,89,93,
        95,99,104,107,112,118,126,128,139,147
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'|'", "'a'", "'<'", "'>'", "'''", 
                     "'\\n'", "'\"'", "'`'", "'\\t'", "'\\r'", "'echo'", 
                     "'ls'", "'grep'", "'cat'" ]

    symbolicNames = [  ]

    RULE_program = 0
    RULE_command = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_whitespace = 4
    RULE_atom = 5
    RULE_argument = 6
    RULE_redirection = 7
    RULE_quoted = 8
    RULE_singlequoted = 9
    RULE_doublequoted = 10
    RULE_doublequotecontent = 11
    RULE_backquoted = 12
    RULE_unquoted = 13
    RULE_application = 14

    ruleNames =  [ "program", "command", "pipe", "call", "whitespace", "atom", 
                   "argument", "redirection", "quoted", "singlequoted", 
                   "doublequoted", "doublequotecontent", "backquoted", "unquoted", 
                   "application" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15

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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62328) != 0):
                self.state = 30
                self.command(0)
                self.state = 35
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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 37
                self.pipe(0)
                pass

            elif la_ == 2:
                self.state = 38
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.CommandContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 41
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 42
                    self.match(ExprParser.T__0)
                    self.state = 43
                    self.command(3) 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 50
            self.call()
            self.state = 51
            self.match(ExprParser.T__1)
            self.state = 52
            self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.PipeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 54
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 55
                    self.match(ExprParser.T__1)
                    self.state = 56
                    self.call() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


        def whitespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.WhitespaceContext)
            else:
                return self.getTypedRuleContext(ExprParser.WhitespaceContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 62
                self.whitespace()


            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 65
                self.redirection()
                self.state = 66
                self.whitespace()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.argument()
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.whitespace()
                    self.state = 75
                    self.atom() 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 82
                self.whitespace()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhitespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_whitespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhitespace" ):
                listener.enterWhitespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhitespace" ):
                listener.exitWhitespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhitespace" ):
                return visitor.visitWhitespace(self)
            else:
                return visitor.visitChildren(self)




    def whitespace(self):

        localctx = ExprParser.WhitespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whitespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ExprParser.T__2)
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
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.redirection()
                pass
            elif token in [3, 6, 8, 9, 12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
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


        def unquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.UnquotedContext)
            else:
                return self.getTypedRuleContext(ExprParser.UnquotedContext,i)


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
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 93
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6, 8, 9]:
                        self.state = 91
                        self.quoted()
                        pass
                    elif token in [3, 12, 13, 14, 15]:
                        self.state = 92
                        self.unquoted()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 95 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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


        def whitespace(self):
            return self.getTypedRuleContext(ExprParser.WhitespaceContext,0)


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
        self.enterRule(localctx, 14, self.RULE_redirection)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(ExprParser.T__3)
                self.state = 99
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 98
                    self.whitespace()


                self.state = 101
                self.argument()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ExprParser.T__4)
                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.whitespace()


                self.state = 106
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

        def singlequoted(self):
            return self.getTypedRuleContext(ExprParser.SinglequotedContext,0)


        def doublequoted(self):
            return self.getTypedRuleContext(ExprParser.DoublequotedContext,0)


        def backquoted(self):
            return self.getTypedRuleContext(ExprParser.BackquotedContext,0)


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
        self.enterRule(localctx, 16, self.RULE_quoted)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.singlequoted()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.doublequoted()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.backquoted()
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


    class SinglequotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_singlequoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinglequoted" ):
                listener.enterSinglequoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinglequoted" ):
                listener.exitSinglequoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinglequoted" ):
                return visitor.visitSinglequoted(self)
            else:
                return visitor.visitChildren(self)




    def singlequoted(self):

        localctx = ExprParser.SinglequotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_singlequoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ExprParser.T__5)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 65342) != 0):
                self.state = 115
                _la = self._input.LA(1)
                if _la <= 0 or _la==6 or _la==7:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(ExprParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoublequotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def backquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BackquotedContext)
            else:
                return self.getTypedRuleContext(ExprParser.BackquotedContext,i)


        def doublequotecontent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DoublequotecontentContext)
            else:
                return self.getTypedRuleContext(ExprParser.DoublequotecontentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_doublequoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoublequoted" ):
                listener.enterDoublequoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoublequoted" ):
                listener.exitDoublequoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoublequoted" ):
                return visitor.visitDoublequoted(self)
            else:
                return visitor.visitChildren(self)




    def doublequoted(self):

        localctx = ExprParser.DoublequotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_doublequoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ExprParser.T__7)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 65150) != 0):
                self.state = 126
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9]:
                    self.state = 124
                    self.backquoted()
                    pass
                elif token in [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15]:
                    self.state = 125
                    self.doublequotecontent()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoublequotecontentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_doublequotecontent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoublequotecontent" ):
                listener.enterDoublequotecontent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoublequotecontent" ):
                listener.exitDoublequotecontent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoublequotecontent" ):
                return visitor.visitDoublequotecontent(self)
            else:
                return visitor.visitChildren(self)




    def doublequotecontent(self):

        localctx = ExprParser.DoublequotecontentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doublequotecontent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
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


    class BackquotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_backquoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackquoted" ):
                listener.enterBackquoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackquoted" ):
                listener.exitBackquoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackquoted" ):
                return visitor.visitBackquoted(self)
            else:
                return visitor.visitChildren(self)




    def backquoted(self):

        localctx = ExprParser.BackquotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_backquoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ExprParser.T__8)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 136
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==6 or _la==7:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 142
            self.match(ExprParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnquotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_unquoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnquoted" ):
                listener.enterUnquoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnquoted" ):
                listener.exitUnquoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnquoted" ):
                return visitor.visitUnquoted(self)
            else:
                return visitor.visitChildren(self)




    def unquoted(self):

        localctx = ExprParser.UnquotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unquoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 144
                    _la = self._input.LA(1)
                    if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 4086) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 147 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_application

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)




    def application(self):

        localctx = ExprParser.ApplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_application)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
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
         




