# Generated from src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellGrammarParser import ShellGrammarParser
else:
    from ShellGrammarParser import ShellGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ShellGrammarParser.

class ShellGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellGrammarParser#s.
    # def visitS(self, ctx:ShellGrammarParser.SContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#command.
    def visitCommand(self, ctx:ShellGrammarParser.CommandContext):
        return None


    # Visit a parse tree produced by ShellGrammarParser#redirection.
    def visitRedirection(self, ctx:ShellGrammarParser.RedirectionContext):
        return None


    # Visit a parse tree produced by ShellGrammarParser#pipe.
    def visitPipe(self, ctx:ShellGrammarParser.PipeContext):
        return None


    # Visit a parse tree produced by ShellGrammarParser#call.
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        return None


    # Visit a parse tree produced by ShellGrammarParser#argument.
    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return None


    # Visit a parse tree produced by ShellGrammarParser#quoted.
    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        return None


del ShellGrammarParser