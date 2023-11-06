from collections import deque
import os
import re
from os import listdir

class Application:
    def run(self, argument: str, out: deque) -> None:
        pass

class Call(Application):
    def __init__(self, arguments: [str]) -> None:
        self.command = arguments[0]
        self.arguments = arguments[1:]

    def run(self, argument: str, out: deque) -> None:
        pass

    def __str__(self) -> str:
        return "Call({command}, {arguments})".format(command=self.command, arguments=self.arguments)

class Pipe(Application):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def run(self, argument: str, out: deque) -> None:
        pass
    
    def __str__(self) -> str:
        return "Pipe({left}, {right})".format(left=self.left, right=self.right)

class GreaterThan(Application):

    def run(self, argument: str, out: deque) -> None:
        pass

    def __str__(self) -> str:
        return "GreaterThan"

class Semicolon(Application):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def run(self, argument: [str], out: deque) -> None:
        pass
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
        return "Semicolon({left}, {right})".format(left=self.left, right=self.right)

class echo(Application):
    def run(self, argument: [str], out: deque) -> None:
        out.append(" ".join(argument) + "\n")

class pwd(Application):
    def run(self, argument: str, out: deque) -> None:
        out.append(os.getcwd() + "\n")

class cd(Application):
    def run(self, argument: str, out: deque) -> None:
        if len(argument) == 0 or len(argument) > 1:
            raise ValueError("wrong number of command line arguments")
        os.chdir(argument[0])

class ls(Application):
    def run(self, argument: [str], out: deque) -> None:
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

class cat(Application):
    def run(self, argument: str, out: deque) -> None:
        for file in argument:
            try:
                with open(file) as f:
                    out.append(f.read())
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")

class head(Application):
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

class tail(Application):
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

class grep(Application):
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