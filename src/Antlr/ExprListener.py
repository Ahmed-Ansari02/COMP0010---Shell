# Generated from src/Antlr/Expr.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ExprParser#whitespace.
    def enterWhitespace(self, ctx:ExprParser.WhitespaceContext):
        pass

    # Exit a parse tree produced by ExprParser#whitespace.
    def exitWhitespace(self, ctx:ExprParser.WhitespaceContext):
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


    # Enter a parse tree produced by ExprParser#redirection.
    def enterRedirection(self, ctx:ExprParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ExprParser#redirection.
    def exitRedirection(self, ctx:ExprParser.RedirectionContext):
        pass


    # Enter a parse tree produced by ExprParser#quoted.
    def enterQuoted(self, ctx:ExprParser.QuotedContext):
        pass

    # Exit a parse tree produced by ExprParser#quoted.
    def exitQuoted(self, ctx:ExprParser.QuotedContext):
        pass


    # Enter a parse tree produced by ExprParser#singlequoted.
    def enterSinglequoted(self, ctx:ExprParser.SinglequotedContext):
        pass

    # Exit a parse tree produced by ExprParser#singlequoted.
    def exitSinglequoted(self, ctx:ExprParser.SinglequotedContext):
        pass


    # Enter a parse tree produced by ExprParser#doublequoted.
    def enterDoublequoted(self, ctx:ExprParser.DoublequotedContext):
        pass

    # Exit a parse tree produced by ExprParser#doublequoted.
    def exitDoublequoted(self, ctx:ExprParser.DoublequotedContext):
        pass


    # Enter a parse tree produced by ExprParser#doublequotecontent.
    def enterDoublequotecontent(self, ctx:ExprParser.DoublequotecontentContext):
        pass

    # Exit a parse tree produced by ExprParser#doublequotecontent.
    def exitDoublequotecontent(self, ctx:ExprParser.DoublequotecontentContext):
        pass


    # Enter a parse tree produced by ExprParser#backquoted.
    def enterBackquoted(self, ctx:ExprParser.BackquotedContext):
        pass

    # Exit a parse tree produced by ExprParser#backquoted.
    def exitBackquoted(self, ctx:ExprParser.BackquotedContext):
        pass


    # Enter a parse tree produced by ExprParser#unquoted.
    def enterUnquoted(self, ctx:ExprParser.UnquotedContext):
        pass

    # Exit a parse tree produced by ExprParser#unquoted.
    def exitUnquoted(self, ctx:ExprParser.UnquotedContext):
        pass


    # Enter a parse tree produced by ExprParser#application.
    def enterApplication(self, ctx:ExprParser.ApplicationContext):
        pass

    # Exit a parse tree produced by ExprParser#application.
    def exitApplication(self, ctx:ExprParser.ApplicationContext):
        pass



del ExprParser