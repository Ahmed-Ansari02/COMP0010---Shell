import sys
from Antlr.ShellGrammarLexer import ShellGrammarLexer
from Antlr.ShellGrammarParser import ShellGrammarParser
from Antlr.ShellGrammarVisitor import ShellGrammarVisitor
from Applications import *
from antlr4 import *

class Converter(ShellGrammarVisitor):

    def __init__(self):
        super().__init__()
# Seq(Call(echo [hell, world]), Call(echo [hello, world]))
# echo hell world ; echo hello world
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
            if argument.quoted():
                call_arr.append(self.visit(argument.quoted(0)))
            else:
                call_arr.append(argument.getText())
        if ctx.redirection():
            redirections = ctx.redirection()
            if len(redirections)>1:
                raise ValueError("Only one redirection may be used")
            for i in redirections:
                
                redirection_arr.append(i.getText()[0])
                redirection_arr.append(i.argument().getText())
            return Redirection(Call(call_arr),redirection_arr[0],redirection_arr[1])
        return Call(call_arr)
    
        # arguments = [argument.getText() if argument.getChildCount() == 0 else ''.join(argument) for argument in arguments]
        # print(arguments)
        # for argument in arguments:
        #     if argument.getChildCount() == 0:
        #         return Call([argument.getText()])

        # if len(arguments) == 1 and arguments[0].quoted():
        #     return self.visitQuoted(arguments[0].quoted(0))
        # return Call([argument.getText() if not argument.quoted() else self.visit(argument.quoted(0)) for argument in arguments])

    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)

    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        if ctx.SINGLE_QUOTED():
            return SingleQuoted(ctx.getText())
        elif ctx.DOUBLE_QUOTED():
            return DoubleQuoted(ctx.getText())
        elif ctx.BACK_QUOTED():
            return BackQuoted(ctx.getText())


