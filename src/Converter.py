import sys
from Antlr.ShellGrammarLexer import ShellGrammarLexer
from Antlr.ShellGrammarParser import ShellGrammarParser
from Antlr.ShellGrammarVisitor import ShellGrammarVisitor
from Applications import *
from antlr4 import *

class Converter(ShellGrammarVisitor):

    def __init__(self):
        super().__init__()

    def visitCommand(self, ctx:ShellGrammarParser.CommandContext):

        if ctx.call():
            return self.visit(ctx.call())
        elif ctx.pipe():
            return self.visit(ctx.pipe())
        elif ctx.getChildCount() == 0:
            return None
        else:
            return Seq(self.visit(ctx.command(0)), self.visit(ctx.command(1)))
            
    def visitPipe(self, ctx:ShellGrammarParser.PipeContext):
        if ctx.pipe():
            return Pipe(self.visit(ctx.pipe()), self.visit(ctx.call(0)))
        return Pipe(self.visit(ctx.call(0)), self.visit(ctx.call(1)))
    
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        arguments = ctx.argument()
        return Call([c.getText() if not c.quoted() else self.visit(c.quoted(0)) for c in arguments ])

    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)

    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        if ctx.SINGLE_QUOTED():
            return SingleQuoted(ctx.getText()[1:-1])
        elif ctx.DOUBLE_QUOTED():
            return DoubleQuoted(ctx.getText()[1:-1])
        elif ctx.BACK_QUOTED():
            return BackQuoted(ctx.getText())
    
if __name__ == "__main__":

    def parse_tree_output(cmdline:str):
        input_stream = InputStream(cmdline)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        tree = parser.command()
        command = tree.accept(Converter())
        return command

    def eval(cmd_str: str):  # function to call eval() and incorporate error handling
        try:
            print(parse_tree_output(cmd_str))
        except ValueError as e:
            print(e)

    while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            eval(cmdline)
