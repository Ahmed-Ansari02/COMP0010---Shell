from collections import deque
import os
import re
import io
from os import listdir
from typing import Any


class Application:
    def run(self, arguments: str, out: deque) -> None:
        return None


class Redirection(Application):
    def __init__(self, call_object, arrow, io_file) -> None:
        self.arrow = arrow
        self.io_file = io_file
        self.call_object = call_object

    def accept(self, visitor):
        return visitor.visit_redirection(self)

    def __str__(self) -> str:
        return f"Redirection({self.call_object}, {self.arrow}, {self.io_file})"
    
    def __repr__(self) -> str:
        return f"Redirection({self.call_object}, {self.arrow}, {self.io_file})"


class Pattern:
    def __init__(self, pattern: str) -> None:
        self.files = []
        self.raw_text = pattern
        self.pattern = pattern.replace("*", ".*").replace("?", ".")
        dir = re.search(r"(.*)/", self.pattern)
        dir_path = ""
        if dir == None:
            dir = os.getcwd()
        else:
            dir = dir.group(1)
            self.pattern = self.pattern[len(dir) + 1 :]
            dir_path = dir + "/"
        try:
            files_in_dir = listdir(dir)
            for file in files_in_dir:
                if re.match(self.pattern, file):
                    self.files.append(dir_path + file)
        except FileNotFoundError:
            raise ValueError(f"directory {dir} does not exist")

    def __str__(self) -> str:
        return f"Pattern({self.pattern})"
    
    def __repr__(self) -> str:
        return f"Pattern({self.pattern})"

    def accept(self, visitor):
        return visitor.visit_pattern(self)


class Options:
    def __init__(self, options: str) -> None:
        self.options = [x for x in options]

    def __str__(self) -> str:
        return f"Options({self.options})"

    def accept(self, visitor):
        return visitor.visit_options(self)


class Quoted:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return f"Quoted({self.value[1:-1]})"

    def accept(self, visitor):
        return None


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


class Argument:
    def __init__(self, argument_list: [str]) -> None:
        self.argument_list = argument_list

    def __str__(self) -> str:
        return f"Argument({self.argument_list})"
    
    def __repr__(self) -> str:
        return f"Argument({self.argument_list})"

    def accept(self, visitor):
        return visitor.visit_argument(self)

class Call(Application):
    def __init__(self, arguments: [str]) -> None:
        self.application = arguments[0]
        self.arguments = arguments[1:]

    def accept(self, visitor):
        return visitor.visit_call(self)

    def __str__(self) -> str:
        return "Call({application}, {arguments})".format(
            application=self.application, arguments=self.arguments
        )


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
            raise FileNotFoundError(f"directory {ls_dir} does not exist")


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
            if not isinstance(file, io.StringIO):
                try:
                    file = open(file)
                except FileNotFoundError:
                    raise ValueError(f"file {file} does not exist")
                except IsADirectoryError:
                    out += f"{file} is not a directory"
            out+=file.read()    
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
        out = ""
        if not isinstance(file, io.StringIO):
            try:
                file = open(file)

            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")
        lines = file.readlines()
        for i in range(0, min(len(lines), num_lines)):
            out += lines[i]
        return out


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
        out = ""
        if not isinstance(file, io.StringIO):
            try:      
                file = open(file)
            except FileNotFoundError:
                raise ValueError(f"file {file} does not exist")
        lines = file.readlines()
        display_length = min(len(lines), num_lines)
        for i in range(0, display_length):
            out += lines[len(lines) - display_length + i]
        return out


class grep(Application):
    def run(self, arguments: [str] = []) -> None:
        out = ""
        if len(arguments) < 2:
            raise ValueError("wrong number of command line arguments")
        files = arguments[1:]
        pattern = re.compile(arguments[0])
        for file in files:
            if not isinstance(file, io.StringIO):
                try:
                    file = open(file)
                except FileNotFoundError:
                    raise ValueError(f"file {file} does not exist")
            lines = file.readlines()
            for line in lines:
                if re.search(pattern, line):
                    if len(files) > 1:
                        out += f"{file.name}:{line}"
                    else:
                        out += line
        return out


class uniq(Application):
    def run(self, arguments: [str] = [], stdin: [str] = []) -> None:
        lines = stdin if stdin else []
        if arguments:
            filename = arguments[0]
            if not isinstance(filename, io.StringIO):
                try:
                    filename = open(filename)
                except FileNotFoundError:
                    raise ValueError(f"file {filename} does not exist")
            lines = filename.readlines()
        
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
                if not isinstance(filename, io.StringIO):
                    try:
                        filename =  open(filename)

                    except FileNotFoundError:
                        raise ValueError(f"file {filename} does not exist")
            out += "".join(sorted(filename.readlines()))
        return out


class cut(Application):
    def byte_range(self, bytes, lines) -> str:
        search_bytes = []
        for byte in bytes:
            if "-" not in byte and isinstance(int(byte), int):
                if int(byte) >= len(lines):
                    raise ValueError("Index out of bounds")
                if int(byte) - 1 not in search_bytes:
                    search_bytes.append(int(byte) - 1)
            elif (len(byte) == 3) and (
                isinstance(int(byte[0]), int)
                and byte[1] == "-"
                and isinstance(int(byte[2]), int)
                and int(byte[0]) < int(byte[2])
            ):
                if int(byte[2]) > len(lines):
                    raise ValueError("Index out of bounds")
                for i in range(int(byte[0]) - 1, int(byte[2])):
                    if i not in search_bytes:
                        search_bytes.append(i)

            elif (len(byte) == 2) and byte[0] == "-" and isinstance(int(byte[1]), int):
                if int(byte[1]) > len(lines):
                    raise ValueError("Index out of bounds")
                for i in range(0, int(byte[1])):
                    if i not in search_bytes:
                        search_bytes.append(i)

            elif (len(byte) == 2) and isinstance(int(byte[0]), int) and byte[1] == "-":
                if int(byte[0]) > len(lines):
                    raise ValueError("Index out of bounds")
                for i in range(int(byte[0]) - 1, len(lines)):
                    if i not in search_bytes:
                        search_bytes.append(i)
            else:
                raise ValueError("Incorrect format for byte range")
        return search_bytes

    def run(self, arguments: [str] = []) -> None:
        if len(arguments) != 3 or arguments[0] != "-b":
            raise ValueError("wrong number of command line arguments or flags")
        option = arguments[0]
        out = ""
        if option == "-b":
            bytes = arguments[1].split(",")
            file = arguments[2]
            if not isinstance(file, io.StringIO):
                try:
                    file = open(file)
                except FileNotFoundError:
                    raise ValueError(f"file {file} does not exist")
            lines = file.readlines()
            for line in lines:
                line = line.replace("\n", "")
                search_bytes = self.byte_range(bytes, line)
                for i in search_bytes:
                    out += line[i]
                out += "\n"
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
