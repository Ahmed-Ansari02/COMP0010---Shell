import re
import sys
import os
import Antlr
from Antlr.ExprLexer import ExprLexer
from Antlr.ExprParser import ExprParser
from Antlr.ExprVisitor import ExprVisitor
from os import listdir
from collections import deque
from glob import glob
from antlr4 import *


class ShellVisitor(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.commands = []

    def visitProgram(self, ctx:ExprParser.ProgramContext):
        super().visitProgram(ctx)
        return self.commands

    def visitSimpleCommand(self, ctx: ExprParser.SimpleCommandContext):
        command = ctx.CMD().pop()
        arguments = []
        if len(ctx.arg()) != 0:
            for argument in ctx.arg():
                arguments.append(self.visitArg(argument))
        self.commands.append({"command": command.__str__(), "args": arguments})

    def visitArg(self, ctx:ExprParser.ArgContext)->str:

        if ctx.UNQUOTED_STRING():
            return ctx.UNQUOTED_STRING().__str__()
        elif ctx.FIlE():
            return ctx.FIlE().__str__()
        else:
            return ctx.STRING().__str__()





class Command:
    def run(self, argument: str, out: deque) -> None:
        pass


class echo(Command):
    def run(self, argument: str, out: deque) -> None:
        out.append(" ".join(argument) + "\n")


class pwd(Command):
    def run(self, argument: str, out: deque) -> None:
        out.append(os.getcwd() + "\n")


class cd(Command):
    def run(self, argument: str, out: deque) -> None:
        if len(argument) == 0 or len(argument) > 1:
            raise ValueError("wrong number of command line arguments")
        os.chdir(argument[0])


class ls(Command):
    def run(self, argument: str, out: deque) -> None:
        if len(argument) == 0:
            ls_dir = os.getcwd()
        elif len(argument) > 1:
            raise ValueError("wrong number of command line arguments")
        else:
            ls_dir = argument[0]
        try:
            for f in listdir(ls_dir):
                if not f.startswith("."):
                    out.append(f + "\n")
        except FileNotFoundError:
            raise ValueError(f"directory {ls_dir} does not exist")


class cat(Command):
    def run(self, argument: str, out: deque) -> None:
        for file in argument:
            try:
                with open(file) as f:
                    out.append(f.read())
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")


class head(Command):
    def run(self, argument: str, out: deque) -> None:
        if len(argument) != 1 and len(argument) != 3:
            raise ValueError("wrong number of command line arguments")
        if len(argument) == 1:
            num_lines = 10
            file = argument[0]
        if len(argument) == 3:
            if argument[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(argument[1])
                file = argument[2]
        try:
            with open(file) as f:
                lines = f.readlines()
                for i in range(0, min(len(lines), num_lines)):
                    out.append(lines[i])
        except FileNotFoundError:
            raise ValueError(f"file {file} does not exist")


class tail(Command):
    def run(self, argument: str, out: deque) -> None:
        if len(argument) != 1 and len(argument) != 3:
            raise ValueError("wrong number of command line arguments")
        if len(argument) == 1:
            num_lines = 10
            file = argument[0]
        if len(argument) == 3:
            if argument[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(argument[1])
                file = argument[2]
        try:
            with open(file) as f:
                lines = f.readlines()
                display_length = min(len(lines), num_lines)
                for i in range(0, display_length):
                    out.append(lines[len(lines) - display_length + i])
        except FileNotFoundError:
            raise ValueError(f"file {file} does not exist")


class grep(Command):
    def run(self, argument: str, out: deque) -> None:
        if len(argument) < 2:
            raise ValueError("wrong number of command line arguments")
        pattern = argument[0]
        files = argument[1:]
        for file in files:
            try:
                with open(file) as f:
                    lines = f.readlines()
                    for line in lines:
                        if re.match(pattern, line):
                            if len(files) > 1:
                                out.append(f"{file}:{line}")
                            else:
                                out.append(line)
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")


COMMANDS = {
    "pwd": pwd,
    "cd": cd,
    "echo": echo,
    "ls": ls,
    "cat": cat,
    "head": head,
    "tail": tail,
    "grep": grep,
}


def parse_raw_commands(cmdline: str):
    operators = {"|", ">", ";"}
    raw_commands = []
    stack = []
    for cmd in cmdline.split(" "):
        # Regex to parse command line arguments
        stack.append(cmd)
    print(f"stack: {stack}")
    while len(stack) != 0:
        token = stack.pop(0)
        command_str = token
        while (len(stack) != 0):
            if stack[0] in operators:
                stack.pop(0)
                break
            command_str += " " + stack.pop(0)
        print(command_str)
        raw_commands.append(command_str)

    return raw_commands


def parse_commands(raw_commands: [str], out: deque):
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

        app = tokens[0]
        args = tokens[1:]
        if app in COMMANDS:
            COMMANDS[app]().run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")
def parse_tree_commands(raw_commands, out: deque):
    for command in raw_commands:
        app = command["command"]
        args = command["args"]
        if app in COMMANDS:
            COMMANDS[app]().run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")

def parse_tree(cmdline:str):
    input_stream = InputStream(cmdline)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    visitor = ShellVisitor()
    return visitor.visitProgram(tree)


def eval(cmdline, out):
    # raw_commands = parse_raw_commands(cmdline)
    commands = parse_tree(cmdline)
    print(commands)
    try:
        parse_tree_commands(commands, out)
    except ValueError as err:
        print(err)


def run_eval(cmd_str: str):  # function to call eval() and incorporate error handling
    out = deque()
    try:
        eval(cmd_str, out)
        while len(out) > 0:
            print(out.popleft(), end="")
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
            run_eval(sys.argv[2])
        except ValueError as e:
            print(e)

    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            run_eval(cmdline)
