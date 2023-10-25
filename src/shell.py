import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob

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

class Command:
    def run(self, argument: str, out: deque) -> None:
        pass

class Pipe(Command):

    def run(self, argument: str, out: deque) -> None:
        pass
    
    def __str__(self) -> str:
        return "Pipe"

class GreaterThan(Command):

    def run(self, argument: str, out: deque) -> None:
        pass

    def __str__(self) -> str:
        return "GreaterThan"

class Semicolon(Command):

    def run(self, argument: [str], out: deque) -> None:
        print("ARGUMENT: ", argument)
        parse_commands([argument[0]], out)
        parse_commands([argument[1]], out)
    
    def __str__(self) -> str:
        return "Semicolon"

class echo(Command):
    def run(self, argument: [str], out: deque) -> None:
        print(argument)
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
    "|": Pipe,
    ">": GreaterThan,
    ";": Semicolon
}

def combine_broken_strings(stack: [str]) -> [str]:
    i = 0
    while i < len(stack):
        print(stack)
        if stack[i][0]=="'":
            while (stack[i][0]=="'" and stack[i][-1]!="'") or len(stack[i])==1:
                if i==len(stack)-1:
                    raise Exception("SyntaxError: Unterminated string")
                stack[i] += ' ' + stack.pop(i+1)
        elif stack[i][0]=='"':
            while (stack[i][0]=='"' and stack[i][-1]!='"') or len(stack[i])==1:
                if i==len(stack)-1:
                    raise Exception("SyntaxError: Unterminated string")
                stack[i] += ' ' + stack.pop(i+1)
        i += 1
    for i in range(len(stack)):
        if not ((stack[i][0]=="'" or stack[i][0]=='"') or (stack[i][-1]=="'" or stack[i][-1]=='"')):
            stack[i] = stack[i].replace(" ; ", ";")
            stack[i] = stack[i].replace(" | ", "|")
            stack[i] = stack[i].replace(" > ", ">")
    return stack

def parse(cmdline: str):
    root = Node(None, None, None)
    pattern = r"([^;|>]*)([;|>])(.*)"
    match = re.match(pattern, cmdline)
    if match:
        s1 = parse(match.group(1))
        s2 = COMMANDS[match.group(2)]()
        s3 = parse(match.group(3))
        root = Node(s2, s1, s3)
    else:
        root = Node(cmdline, None, None)
    return root

def parse_raw_commands(cmdline: str, out: deque):
    root = parse(cmdline)
    if not(isinstance(root.value, Pipe) or isinstance(root.value, GreaterThan) or isinstance(root.value, Semicolon)):
        parse_commands([root.value], out)
    else:
        root.value.run([root.left.value, root.right.value], out)

    # cmdline = re.sub(r'([;|>])', r' \1 ', cmdline)
    # operators = {"|", ">", ";"}
    # raw_commands = []
    # stack = re.split(r'\s+', cmdline)
    # stack = [item for item in stack if item]
    # stack = combine_broken_strings(stack)
    # print("Stack: ", stack)
    # while len(stack) != 0:
    #     token = stack.pop(0)
    #     command_str = token
    #     while (len(stack) != 0):
    #         if stack[0] in operators:
    #             stack.pop(0)
    #             break
    #         command_str += " " + str(stack.pop(0))
    #     raw_commands.append(command_str)
    # print("Raw commands: ", raw_commands)
    # return raw_commands

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
        if app in COMMANDS:
            COMMANDS[app]().run(args, out)
        else:
            raise ValueError(f"unsupported application {app}")

def eval(cmdline, out):
    try:
        parse_raw_commands(cmdline, out)
        # parse_commands(raw_commands, out)
        # print("Out: ", out)
    except Exception as e:
        print(e)

def run_eval(cmd_str: str):  # function to call eval() and incorporate error handling
    out = deque()
    try:
        eval(cmd_str, out)
        print("Out before printed: ", out)
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
