# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#command.
    def enterCommand(self, ctx:ExprParser.CommandContext):
        pass

    # Exit a parse tree produced by ExprParser#command.
    def exitCommand(self, ctx:ExprParser.CommandContext):
        pass


    # Enter a parse tree produced by ExprParser#simpleCommand.
    def enterSimpleCommand(self, ctx:ExprParser.SimpleCommandContext):
        pass

    # Exit a parse tree produced by ExprParser#simpleCommand.
    def exitSimpleCommand(self, ctx:ExprParser.SimpleCommandContext):
        pass


    # Enter a parse tree produced by ExprParser#arg.
    def enterArg(self, ctx:ExprParser.ArgContext):
        pass

    # Exit a parse tree produced by ExprParser#arg.
    def exitArg(self, ctx:ExprParser.ArgContext):
        pass



del ExprParser