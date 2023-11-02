import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob
from antlr4 import *

from Applications import *
import Antlr
from Antlr.ExprLexer import ExprLexer
from Antlr.ExprParser import ExprParser
from Antlr.ExprVisitor import ExprVisitor

class ShellVisitor(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.commands = []

    def visitProgram(self, ctx:ExprParser.ProgramContext):
        print(ctx.toStringTree(recog=ctx.parser))
        super().visitProgram(ctx)
        return self.commands

    def visitSimpleCommand(self, ctx: ExprParser.SimpleCommandContext):
        print(ctx.toStringTree(recog=ctx.parser))
        command = ctx.CMD().pop()
        arguments = ""
        if len(ctx.arg()) != 0:
            for argument in ctx.arg():
                arguments += self.visitArg(argument) + " "
        self.commands.append({"command": command.__str__(), "args": arguments})

    def visitArg(self, ctx:ExprParser.ArgContext)->str:
        print(ctx.toStringTree(recog=ctx.parser))
        if ctx.UNQUOTED_STRING():
            return ctx.UNQUOTED_STRING().__str__()
        else:
            return ctx.STRING().__str__()

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Tree(Left: {self.left}, Value: {self.value}, Right: {self.right})"

class Quoted(Node):
    def __init__(self, quoted_str: str) -> None:
        self.quoted_str = quoted_str

    def __str__(self) -> str:
        return self.quoted_str
        
    def parse(self, tokens: [str]) -> None:
        pass

APPLICATIONS = {
    "pwd": pwd,
    "cd": cd,
    "echo": echo,
    "ls": ls,
    "cat": cat,
    "head": head,
    "tail": tail,
    "grep": grep,
    "|": Pipe,
    ">": GreaterThan,
    ";": Semicolon
}

'''
def parse(cmdline: str):
    root = Node(None, None, None)
    pattern = r"([^;|>]*)([;|>])(.*)"
    match = re.match(pattern, cmdline)
    if match:
        quotes_surrounding_operator = (((match.group(1).count("'") % 2 != 0) and (match.group(1).count("'") == match.group(3).count("'"))) or ((match.group(1).count("\"") % 2 != 0) and (match.group(1).count("\"") == match.group(3).count("\""))))
        if quotes_surrounding_operator:
            root = Node(cmdline, None, None)
        else:
            s1 = parse(match.group(1))
            s2 = APPLICATIONS[match.group(2)]()
            s3 = parse(match.group(3))
            root = Node(s2, s1, s3)
    else:
        root = Node(cmdline, None, None)
    return root

def parse_raw_commands(cmdline: str, out: deque):
    root = parse(cmdline)
    print("Root: ", root)
    if not(isinstance(root.value, Pipe) or isinstance(root.value, GreaterThan) or isinstance(root.value, Semicolon)):
        parse_commands([root.value], out)
    else:
        root.value.run([root.left.value, root.right.value], out)

def parse_commands(raw_commands: [str], out: deque):
    print("Raw commands: ", raw_commands)
    for command in raw_commands:
        tokens = []
        for m in re.finditer("[^\\s\"']+|\"([^\"]*)\"|'([^']*)'", command):
            if m.group(1) or m.group(2):
                quoted = m.group(0)
                tokens.append(quoted[1:-1])
            else:
                globbing = glob(m.group(0))
                if globbing:
                    tokens.extend(globbing)
                else:
                    tokens.append(m.group(0))
        if len(tokens) == 0: continue
        print("Tokens: ", tokens)
        app = tokens[0]
        args = tokens[1:]
        if app in APPLICATIONS:
            APPLICATIONS[app]().run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")
'''

def parse_tree_output(cmdline:str):
    input_stream = InputStream(cmdline)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    visitor = ShellVisitor()
    print(tree.toStringTree(recog=parser))
    return visitor.visitProgram(tree)

def eval(cmd_str: str):  # function to call eval() and incorporate error handling
    try:
        print(parse_tree_output(cmd_str))
    except ValueError as e:
        print(e)

def check_args(
    args_num, args
):  # function to check command line arguments and incorporate error handling
    if args_num != 2:
        raise ValueError("wrong number of command line arguments")
    if args[1] != "-c":
        raise ValueError(f"unexpected command line argument {args[1]}")

if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:
        try:
            check_args(args_num, sys.argv)
            eval(sys.argv[2])
        except ValueError as e:
            print(e)
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            eval(cmdline)
