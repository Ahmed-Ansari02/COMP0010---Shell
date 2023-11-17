from collections import deque
import os
import re
from os import listdir
from typing import Any

class Application:
    def run(self, arguments: str, out: deque) -> None:
        pass

class Redirection(Application):
    def __init__(self,  call_object, arrow, io_file) -> None:
        self.arrow = arrow
        self.io_file = io_file
        self.call_object = call_object
    def accept(self, visitor):
        return visitor.visit_redirection(self)
    def __str__(self)->str:
        return f"Redirection( {self.call_arr}, {self.arrow}, {self.io_file})"


class Pattern():
    def __init__(self, pattern: str) -> None:
        self.raw_text = pattern
        self.pattern = pattern.replace("*", ".*").replace("?", ".")
        dir = os.getcwd()
        files_in_dir = listdir(dir)
        self.files = []
        for file in files_in_dir:
            if re.match(self.pattern, file):
                self.files.append(file)

    def __str__(self) -> str:
        return f"Pattern({self.files})"
    
    def accept(self, visitor):
        return visitor.visit_pattern(self)
    
class Quoted():
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self) -> str:
        return self.value[1:-1]

    def accept(self, visitor):
        pass

class DoubleQuoted(Quoted):
    def __init__(self, value: str) -> None:
        self.value = value
        
    def __str__(self) -> str:
        return f"DoubleQuoted({self.value[1:-1]})"

    def __repr__(self) -> str:
        return f"DoubleQuoted({self.value[1:-1]})"

    def accept(self, visitor):
        return visitor.visit_double_quoted(self)

class SingleQuoted(Quoted):
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"SingleQuoted({self.value[1:-1]})"

    def __repr__(self) -> str:
        return f"SingleQuoted({self.value[1:-1]})"
    
    def accept(self, visitor):
        return visitor.visit_single_quoted(self)

class BackQuoted(Quoted):
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"BackQuoted({self.value[1:-1]})"
    
    def __repr__(self) -> str:
        return f"BackQuoted({self.value[1:-1]})"

    def accept(self, visitor):
        return visitor.visit_back_quoted(self)

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

class Seq(Application):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_seq(self)
    
    def __str__(self) -> str:
        return "Seq({left}, {right})".format(left=self.left, right=self.right)

class echo(Application):
    def run(self, arguments: [str] = []) -> None:
        return " ".join(arguments)

class ls(Application):
    def run(self, arguments: [str] = []) -> None:
        if len(arguments) == 0:
            ls_dir = os.getcwd()
        elif len(arguments) > 1:
            raise ValueError("wrong number of command line arguments")
        else:
            ls_dir = arguments[0]
        out = ""
        try:
            for f in listdir(ls_dir):
                if not f.startswith("."):
                    out += f + "\n"
            return out
        except FileNotFoundError:
            raise ValueError(f"directory {ls_dir} does not exist")

class cd(Application):
    
    def run(self, arguments: [str] = []) -> None:
        if len(arguments) == 0 or len(arguments) > 1:
            raise ValueError("wrong number of command line arguments")
        try:
            os.chdir(arguments[0])
        except FileNotFoundError:
            raise ValueError(f"directory {arguments[0]} does not exist")
            
        return ""

class pwd(Application):
    def run(self, arguments: [str] = []) -> None:
        return os.getcwd() + "\n"

class cat(Application):
    def run(self, arguments: [str] = []) -> str:
        out = ""
        for file in arguments:
            try:
                with open(file) as f:
                    out += f.read()
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")
        return out

class head(Application):
    def run(self, arguments: [str] = []) -> str:
        if len(arguments) != 1 and len(arguments) != 3:
            raise ValueError("wrong number of command line arguments")
        if len(arguments) == 1:
            num_lines = 10
            file = arguments[0]
        if len(arguments) == 3:
            if arguments[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(arguments[1])
                file = arguments[2]
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
    def run(self, arguments: [str] = []) -> None:
        if len(arguments) != 1 and len(arguments) != 3:
            raise ValueError("wrong number of command line arguments")
        if len(arguments) == 1:
            num_lines = 10
            file = arguments[0]
        if len(arguments) == 3:
            if arguments[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(arguments[1])
                file = arguments[2]
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
    def run(self, arguments: [str] = []) -> None:
        if len(arguments) < 2:
            raise ValueError("wrong number of command line arguments")
        pattern = arguments[0]
        pattern = pattern.replace('"', "")
        files = arguments[1:]
        for file in files:
            try:
                out = ""
                with open(file) as f:
                    lines = f.readlines()
                    linesDict = {index: element for index, element in enumerate(lines)}
                    checked = []
                    for line in lines:
                        if re.match(pattern, line):
                            if len(files) > 1:
                                out += f"{file}:{line}"
                            else:
                                out += line
                return out
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")

class uniq(Application):
    def run(self, arguments: [str] = [], stdin: [str] = []) -> None:
        lines = stdin if stdin else []
        if arguments:
            filename = arguments[0]
            try:
                with open(filename) as f:
                    lines = f.readlines()
            except FileNotFoundError:
                raise ValueError(f"file {filename} does not exist")
        out = []
        prev_line = None
        for line in lines:
            if line != prev_line:
                out.append(line)
            prev_line = line
        return "".join(out)
          

class sort(Application):
    def run(self, arguments: [str] = [], stdin: [str] = []) -> None:
        out = stdin if stdin else ""
        if arguments:
            for filename in arguments:
                try:
                    with open(filename) as f:
                        out += "".join(sorted(f.readlines()))
                except FileNotFoundError:
                    raise ValueError(f"file {filename} does not exist")
        return out

class cut(Application):
    def run(self, arguments: [str] = [], stdin: [str] = []) -> None:
        if len(arguments) != 2 or arguments[0] != "-f":
            raise ValueError("wrong number of command line arguments or flags")
        field = int(arguments[1])
        lines = stdin if stdin else []
        if len(arguments) > 2:
            file = arguments[2]
            try:
                with open(file) as f:
                    lines = f.readlines()
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")
        out = []
        for line in lines:
            fields = line.split()
            if field <= len(fields):
                out.append(fields[field - 1])
        return out

class find(Application):
    def run(self, arguments: [str] = [], stdin: [str] = []) -> None:
        if len(arguments) != 2:
            raise ValueError("wrong number of command line arguments")
        path, pattern = arguments
        matches = []
        for root, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))
        return matches
    
APPLICATIONS = {
    "pwd": pwd,
    "cd": cd,
    "echo": echo,
    "ls": ls,
    "cat": cat,
    "head": head,
    "tail": tail,
    "grep": grep,
    "uniq": uniq,
    "sort": sort,
    "cut": cut,
    "find": find,
}
