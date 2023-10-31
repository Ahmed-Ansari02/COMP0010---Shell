# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#command.
    def visitCommand(self, ctx:ExprParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#simpleCommand.
    def visitSimpleCommand(self, ctx:ExprParser.SimpleCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arg.
    def visitArg(self, ctx:ExprParser.ArgContext):
        return self.visitChildren(ctx)



del ExprParser