# Generated from src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellGrammarParser import ShellGrammarParser
else:
    from ShellGrammarParser import ShellGrammarParser

# This class defines a complete listener for a parse tree produced by ShellGrammarParser.
class ShellGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ShellGrammarParser#s.
    def enterS(self, ctx:ShellGrammarParser.SContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#s.
    def exitS(self, ctx:ShellGrammarParser.SContext):
        pass


    # Enter a parse tree produced by ShellGrammarParser#command.
    def enterCommand(self, ctx:ShellGrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#command.
    def exitCommand(self, ctx:ShellGrammarParser.CommandContext):
        pass


    # Enter a parse tree produced by ShellGrammarParser#redirection.
    def enterRedirection(self, ctx:ShellGrammarParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#redirection.
    def exitRedirection(self, ctx:ShellGrammarParser.RedirectionContext):
        pass


    # Enter a parse tree produced by ShellGrammarParser#pipe.
    def enterPipe(self, ctx:ShellGrammarParser.PipeContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#pipe.
    def exitPipe(self, ctx:ShellGrammarParser.PipeContext):
        pass


    # Enter a parse tree produced by ShellGrammarParser#call.
    def enterCall(self, ctx:ShellGrammarParser.CallContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#call.
    def exitCall(self, ctx:ShellGrammarParser.CallContext):
        pass


    # Enter a parse tree produced by ShellGrammarParser#argument.
    def enterArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#argument.
    def exitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ShellGrammarParser#quoted.
    def enterQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        pass

    # Exit a parse tree produced by ShellGrammarParser#quoted.
    def exitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        pass



del ShellGrammarParser