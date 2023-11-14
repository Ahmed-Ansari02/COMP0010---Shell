from Applications import *
from Visitor import Visitor
import io

class Evaluator(Visitor):

    def __init__(self) -> None:
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
            return APPLICATIONS[app]().run(argument=arguments)
        else:
            return " ".join([app] + arguments)

    def visit_seq(self, seq):
        left = seq.left
        right = seq.right
        return f"{left.accept(self)}\n{right.accept(self)}"

    def visit_quoted(self, quoted):
        return quoted.value
    


    def visit_pipe(self, pipe):
        left_result = pipe.left.accept(self)
        stdin = io.StringIO(left_result)
        pipe.right.arguments.append(stdin)
        return pipe.right.accept(self)        