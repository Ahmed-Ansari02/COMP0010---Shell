# Generated from src/Antlr/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#redirection.
    def enterRedirection(self, ctx:ExprParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ExprParser#redirection.
    def exitRedirection(self, ctx:ExprParser.RedirectionContext):
        pass


    # Enter a parse tree produced by ExprParser#command.
    def enterCommand(self, ctx:ExprParser.CommandContext):
        pass

    # Exit a parse tree produced by ExprParser#command.
    def exitCommand(self, ctx:ExprParser.CommandContext):
        pass


    # Enter a parse tree produced by ExprParser#pipe.
    def enterPipe(self, ctx:ExprParser.PipeContext):
        pass

    # Exit a parse tree produced by ExprParser#pipe.
    def exitPipe(self, ctx:ExprParser.PipeContext):
        pass


    # Enter a parse tree produced by ExprParser#call.
    def enterCall(self, ctx:ExprParser.CallContext):
        pass

    # Exit a parse tree produced by ExprParser#call.
    def exitCall(self, ctx:ExprParser.CallContext):
        pass


    # Enter a parse tree produced by ExprParser#atom.
    def enterAtom(self, ctx:ExprParser.AtomContext):
        pass

    # Exit a parse tree produced by ExprParser#atom.
    def exitAtom(self, ctx:ExprParser.AtomContext):
        pass


    # Enter a parse tree produced by ExprParser#argument.
    def enterArgument(self, ctx:ExprParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ExprParser#argument.
    def exitArgument(self, ctx:ExprParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ExprParser#quoted.
    def enterQuoted(self, ctx:ExprParser.QuotedContext):
        pass

    # Exit a parse tree produced by ExprParser#quoted.
    def exitQuoted(self, ctx:ExprParser.QuotedContext):
        pass



del ExprParser