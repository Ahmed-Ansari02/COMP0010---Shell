import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob


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
    raw_commands = []
    stack = []
    for cmd in cmdline.split(" "):
        stack.append(cmd)

    while len(stack) != 0:
        token = stack.pop(0)
        command_str = token
        while (len(stack) != 0) and (
            (stack[0] != "|") or (stack[0] != ">") or (stack[0] != ";")
        ):
            command_str += " " + stack.pop(0)
        raw_commands.append(command_str)
    return raw_commands


def parse_commands(raw_commands: str, out: deque):
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


def eval(cmdline, out):
    raw_commands = parse_raw_commands(cmdline)
    try:
        parse_commands(raw_commands, out)
    except ValueError as e:
        print(e)


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
