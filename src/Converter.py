from Antlr.ShellGrammarVisitor import ShellGrammarVisitor
from Antlr.ShellGrammarParser import ShellGrammarParser
from Applications import *


class Converter(ShellGrammarVisitor):

    def __init__(self):
        super().__init__()

    def visitCommand(self, ctx:ShellGrammarParser.CommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#call.
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#atom.
    def visitAtom(self, ctx:ShellGrammarParser.AtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#argument.
    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#quoted.
    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        return self.visitChildren(ctx)