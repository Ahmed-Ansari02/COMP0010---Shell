from Applications import *
from Visitor import Visitor
from antlr4 import *
from Antlr.ShellGrammarLexer import ShellGrammarLexer
from Antlr.ShellGrammarParser import ShellGrammarParser
from Converter import Converter

def convert(cmdline:str):
    input_stream = InputStream(cmdline)
    lexer = ShellGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ShellGrammarParser(stream)
    tree = parser.command()
    command = tree.accept(Converter())
    # print(command)
    return command

def evaluate(e):
    return e.accept(Evaluator())


class Evaluator(Visitor):

    def __init__(self) -> None:
        super().__init__()
    
    def visit_call(self, call):
        app = call.application
        arguments = call.arguments

        app = app.accept(self) if isinstance(app, Quoted) else app
        arguments = [argument.accept(self) if isinstance(argument, Quoted) else argument for argument in arguments]
        
        if app in APPLICATIONS.keys():
            return APPLICATIONS[app]().run(argument=arguments)
        else:
            return " ".join([app] + arguments)

    def visit_seq(self, seq):
        left = seq.left
        right = seq.right
        return f"{left.accept(self)}\n{right.accept(self)}"

    def visit_single_quoted(self, quoted):
        return quoted.value[1:-1]
    
    def visit_double_quoted(self, quoted):
        return quoted.value[1:-1]

    def visit_back_quoted(self, backquoted):
        return evaluate(convert((backquoted.value[1:-1])))

    def visit_pipe(self, pipe):
        left = pipe.left
        right = pipe.right
        right.arguments += left.accept(self)
        right.accept(self)