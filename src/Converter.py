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
            return Pipe(left=self.visit(ctx.pipe()), right=self.visit(ctx.call(0)))
        return Pipe(left=self.visit(ctx.call(0)), right=self.visit(ctx.call(1)))
    
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        call_arr=[]
        redirection_arr = []
        arguments = ctx.argument()

        for argument in arguments:
            call_arr.append(self.visit(argument))

        # Takes care of redirection. Separate from arguments.
        if ctx.redirection():
            redirections = ctx.redirection()
            if len(redirections)>1:
                raise ValueError("Only one redirection may be used")
            for i in redirections:
                redirection_arr.append(i.getText()[0])
                redirection_arr.append(self.visit(i.argument()))
            return Redirection(Call(call_arr),redirection_arr[0],redirection_arr[1])
        
        return Call(call_arr)

    def visitRedirection(self, ctx: ShellGrammarParser.RedirectionContext):
        return super().visitRedirection(ctx)
    
    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        argument_arr = []
        if ctx.quoted() or ctx.UNQUOTED():
            for element in ctx.getChildren():
                if type(element) == ShellGrammarParser.QuotedContext:
                    argument_arr.append(self.visit(element))
                elif "*" in element.getText() or "?" in element.getText() or "[" in element.getText():
                    argument_arr.append(Pattern(element.getText()))
                else:
                    argument_arr.append(element.getText())
            return Argument(argument_arr)

    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        if ctx.SINGLE_QUOTED():
            return SingleQuoted(ctx.getText())
        elif ctx.DOUBLE_QUOTED():
            return DoubleQuoted(ctx.getText())
        elif ctx.BACK_QUOTED():
            return BackQuoted(ctx.getText())


