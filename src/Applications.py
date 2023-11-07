from collections import deque
import os
import re
from os import listdir

class Application:
    def run(self, argument: str, out: deque) -> None:
        pass

class Call(Application):
    def __init__(self, arguments: [str]) -> None:
        self.application = arguments[0]
        self.arguments = arguments[1:]

    def accept(self, visitor):
        return visitor.visit_call(self)

    def __str__(self) -> str:
        return "Call({application}, {arguments})".format(application=self.application, arguments=self.arguments)

class Pipe(Application):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_pipe(self)
    
    def __str__(self) -> str:
        return "Pipe({left}, {right})".format(left=self.left, right=self.right)

class GreaterThan(Application):

    def run(self, argument: str, out: deque) -> None:
        pass

    def __str__(self) -> str:
        return "GreaterThan"

class Seq(Application):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_seq(self)
        # print("ARGUMENT: ", argument)
        # left = argument[0]
        # right = argument[1]
        # if not(isinstance(left, Pipe) or isinstance(left, GreaterThan) or isinstance(left, Semicolon)):
        #     parse_commands([left], out)
        # else:
        #     argument[0].run([left.left.value, left.right.value], out)
        
        # if not(isinstance(right, Pipe) or isinstance(right, GreaterThan) or isinstance(right, Semicolon)):
        #     parse_commands([right], out)
        # else:
        #     argument[0].run([right.left.value, right.right.value], out)
    
    def __str__(self) -> str:
        return "Seq({left}, {right})".format(left=self.left, right=self.right)

class echo(Application):
    def run(self, argument: [str] = []) -> None:
        return " ".join(argument)

class ls(Application):
    def run(self, argument: [str] = []) -> None:

        if len(argument) == 0:
            ls_dir = os.getcwd()
        elif len(argument) > 1:
            raise ValueError("wrong number of command line arguments")
        else:
            ls_dir = argument[0]
        out = ""
        try:
            for f in listdir(ls_dir):
                if not f.startswith("."):
                    out += f + "\n"
            return out
        except FileNotFoundError:
            raise ValueError(f"directory {ls_dir} does not exist")

class cd(Application):
    
    def run(self, argument: str = []) -> None:
        if len(argument) == 0 or len(argument) > 1:
            raise ValueError("wrong number of command line arguments")
        os.chdir(argument[0])

class pwd(Application):
    def run(self, argument: str = []) -> None:
        return os.getcwd() + "\n"

class cat(Application):
    def run(self, argument: str = []) -> None:
        for file in argument:
            try:
                with open(file) as f:
                    return f.read()
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")

class head(Application):
    def run(self, argument: str = []) -> None:
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
            out = ""
            with open(file) as f:
                lines = f.readlines()
                for i in range(0, min(len(lines), num_lines)):
                    out += lines[i]
            return out
        except FileNotFoundError:
            raise ValueError(f"file {file} does not exist")

class tail(Application):
    def run(self, argument: str = []) -> None:
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
            out = ""
            with open(file) as f:
                lines = f.readlines()
                display_length = min(len(lines), num_lines)
                for i in range(0, display_length):
                    out += (lines[len(lines) - display_length + i])
            return out
        except FileNotFoundError:
            raise ValueError(f"file {file} does not exist")

class grep(Application):
    def run(self, argument: str = []) -> None:

        if len(argument) < 2:
            raise ValueError("wrong number of command line arguments")
        pattern = argument[0]
        files = argument[1:]
        for file in files:
            try:
                out = ""
                with open(file) as f:
                    lines = f.readlines()
                    for line in lines:
                        if re.match(pattern, line):
                            if len(files) > 1:
                                out += (f"{file}:{line}")
                            else:
                                out += (line)
                return out
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")
            
APPLICATIONS = {
    "pwd": pwd,
    "cd": cd,
    "echo": echo,
    "ls": ls,
    "cat": cat,
    "head": head,
    "tail": tail,
    "grep": grep,
}