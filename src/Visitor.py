class Visitor():

    def visit_call(self, call):
        return None
    
    def visit_argument(self, argument):
        return None

    def visit_redirection(self, redirection):
        return None

    def visit_seq(self, seq):
        return None

    def visit_single_quoted(self, quoted):
        return None

    def visit_double_quoted(self, quoted):
        return None

    def visit_back_quoted(self, backquoted):
        return None

    def visit_pipe(self, pipe):
        return None    
    
    def visit_pattern(self, pattern):
        return None