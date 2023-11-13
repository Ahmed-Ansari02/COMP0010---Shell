# Generated from src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellGrammarParser import ShellGrammarParser
else:
    from ShellGrammarParser import ShellGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ShellGrammarParser.

class ShellGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellGrammarParser#s.
    def visitS(self, ctx:ShellGrammarParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#command.
    def visitCommand(self, ctx:ShellGrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#redirection.
    def visitRedirection(self, ctx:ShellGrammarParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#pipe.
    def visitPipe(self, ctx:ShellGrammarParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#call.
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#argument.
    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#quoted.
    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#single_quoted.
    def visitSingle_quoted(self, ctx:ShellGrammarParser.Single_quotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#double_quoted.
    def visitDouble_quoted(self, ctx:ShellGrammarParser.Double_quotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#back_quoted.
    def visitBack_quoted(self, ctx:ShellGrammarParser.Back_quotedContext):
        return self.visitChildren(ctx)



del ShellGrammarParser