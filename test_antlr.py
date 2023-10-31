import sys
from antlr4 import *
from Antlr.ExprLexer import ExprLexer
from Antlr.ExprParser import ExprParser
from Antlr.ExprVisitor import ExprVisitor


class ShellVisitor(ExprVisitor):

    def visitSimpleCommand(self, ctx: ExprParser.SimpleCommandContext):
        command = ctx.CMD().pop()
        arguments = ""
        if len(ctx.arg()) != 0:
            for argument in ctx.arg():
                arguments += self.visitArg(argument) + " "
        print(f"command is {command} with arguments {arguments}")

    def visitArg(self, ctx:ExprParser.ArgContext)->str:
        if ctx.UNQUOTED_STRING():
            return ctx.UNQUOTED_STRING().__str__()
        else:
            return ctx.STRING().__str__()



def main(argv):

    command = input("Enter your command here: ")
    input_stream = InputStream(command)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    visitor = ShellVisitor()
    visitor.visitProgram(tree)


if __name__ == '__main__':
    main(sys.argv)
