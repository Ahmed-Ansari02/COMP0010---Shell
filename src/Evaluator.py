from Applications import *
from Visitor import Visitor
from antlr4 import *
from Antlr.ShellGrammarLexer import ShellGrammarLexer
from Antlr.ShellGrammarParser import ShellGrammarParser
from Converter import Converter
import io
def convert(cmdline:str):
    input_stream = InputStream(cmdline)
    lexer = ShellGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ShellGrammarParser(stream)
    tree = parser.command()
    command = tree.accept(Converter())

    return command

def evaluate(e):
    return e.accept(Evaluator(backtick_root=True))


class Evaluator(Visitor):

    def __init__(self, backtick_root = False) -> None:
        self.backtick_root = backtick_root
        super().__init__()
    
    def visit_call(self, call):
        app = call.application
        arguments = []
        for arg in call.arguments:
            if isinstance(arg, Quoted) or isinstance(arg, DoubleQuoted) or isinstance(arg, SingleQuoted) or isinstance(arg, BackQuoted):
                arguments.append(arg.accept(self))
            else:
                arguments.append(arg)
        if app in APPLICATIONS.keys():
            return APPLICATIONS[app]().run(arguments)
        else:
            return " ".join([app] + arguments)
    def visit_redirection(self, redirection):
        arrow = redirection.arrow
        call_arr = redirection.call_arr
        io_file = redirection.io_file
        if arrow == ">":
            stdout = evaluate(Call(call_arr))
            with open(io_file, 'w') as file:
                file.write(stdout)
        elif arrow == "<":
            
            with open(io_file, 'r') as file:
                arguments = file.read()
            call_arr.append(arguments)
            
            
            return evaluate(Call(call_arr))
            

        return ""

    def visit_seq(self, seq):
        left = seq.left
        right = seq.right
        if not self.backtick_root:
            return f"{left.accept(self)}\n{right.accept(self)}"
        else:
            return f"{left.accept(self)} {right.accept(self)}"

    def visit_single_quoted(self, quoted):
        return quoted.value[1:-1]
    
    def visit_double_quoted(self, quoted):
        return quoted.value[1:-1]

    def visit_back_quoted(self, backquoted):
        return evaluate(convert((backquoted.value[1:-1])))

    def visit_pipe(self, pipe):
        left_result = pipe.left.accept(self)
        pipe.right.arguments.append(left_result)
        return pipe.right.accept(self)        