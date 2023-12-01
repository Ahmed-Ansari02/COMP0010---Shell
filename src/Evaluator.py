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
            if not isinstance(arg, str) and not isinstance(arg, io.StringIO):
                arg = arg.accept(self)

        for arg in call.arguments:
            # if isinstance(arg, Pattern):
            #     for x in arg.accept(self).split():
            #         arguments.append(x) 
            if not isinstance(arg, str) and not isinstance(arg, io.StringIO):
                arguments.append(arg.accept(self))
            else:
                arguments.append(arg)


        if not isinstance(app, str):
            app = app.accept(self)
        if app in APPLICATIONS.keys():
            return APPLICATIONS[app]().run(arguments)
        else:
            return " ".join([app] + arguments)
    
    def visit_argument(self, argument):
        to_return = "".join([element.accept(self) if (type(element) != str and type(element) != io.StringIO) else element for element in argument.argument_list])
        return to_return

    def visit_redirection(self, redirection):
        arrow = redirection.arrow
        call_object = redirection.call_object
        io_file = redirection.io_file.accept(self)
        if arrow == ">":
            stdout = call_object.accept(self)
            with open(io_file, 'w') as file:
                file.write(stdout)
        elif arrow == "<":
            try:
                with open(io_file,'r') as file:
                    file_content = file.read()
            except FileNotFoundError:
                return FileNotFoundError(f"file {io_file} not found")
            stdin = io.StringIO(file_content)
            call_object.arguments.append(stdin)  
            return call_object.accept(self)
        return ""

    def visit_seq(self, seq):
        left = seq.left
        right = seq.right
        if not self.backtick_root:
            try:
                accepted_left = left.accept(self)
                accepted_right = right.accept(self)
                return f"{accepted_left}\n{accepted_right}"
                # return f"{left.accept(self)}\n{right.accept(self)}"
            except:
                return f""
        else:
            try:
                accepted_left = left.accept(self)
                accepted_right = right.accept(self)
                return f"{left.accept(self)} {right.accept(self)}"
                # return f"{left.accept(self)} {right.accept(self)}"
            except:
                return f""

    def visit_single_quoted(self, quoted):
        return quoted.value[1:-1]
    
    def visit_double_quoted(self, quoted):
        value = quoted.value[1:-1].replace("\"", "")
        tokens = re.findall(r'[^`]+|`[^`]+`', value)
        return ''.join([token if (token[0] != '`' and token[-1] != '`') else evaluate(convert(token[1:-1])) for token in tokens])

    def visit_back_quoted(self, backquoted):
        return evaluate(convert((backquoted.value[1:-1])))

    def visit_pipe(self, pipe):
        try:
            left_result = pipe.left.accept(self)
            stdin = io.StringIO(left_result)
            pipe.right.arguments.append(stdin)
            return pipe.right.accept(self)          
        except:
            return ""

    def visit_pattern(self, pattern):
        return ' '.join(pattern.files)
