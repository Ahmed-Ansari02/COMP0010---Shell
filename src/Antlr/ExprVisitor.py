# Generated from src/Antlr/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#command.
    def visitCommand(self, ctx:ExprParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pipe.
    def visitPipe(self, ctx:ExprParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#call.
    def visitCall(self, ctx:ExprParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atom.
    def visitAtom(self, ctx:ExprParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#argument.
    def visitArgument(self, ctx:ExprParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#redirection.
    def visitRedirection(self, ctx:ExprParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#quoted.
    def visitQuoted(self, ctx:ExprParser.QuotedContext):
        return self.visitChildren(ctx)



del ExprParser