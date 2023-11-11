from Applications import *
from Visitor import Visitor

class Evaluator(Visitor):

    def __init__(self) -> None:
        super().__init__()
    
    def visit_call(self, call):
        app = call.application
        arguments = call.arguments
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
        left = pipe.left
        right = pipe.right
        right.arguments += left.accept(self)
        right.accept(self)
