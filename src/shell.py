import sys
import os
from antlr4 import InputStream, CommonTokenStream

from Converter import Converter
from Evaluator import Evaluator
from Antlr.ShellGrammarLexer import ShellGrammarLexer
from Antlr.ShellGrammarParser import ShellGrammarParser


def convert(cmdline: str):

    input_stream = InputStream(cmdline)
    lexer = ShellGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ShellGrammarParser(stream)
    tree = parser.command()
    command = tree.accept(Converter())

    return command


def evaluate(e):
    if e is None:
        return ""
    return e.accept(Evaluator())  #Visitor for the application

    try:
        return evaluate(convert(cmd_str))
    except ValueError as e:
        return str(e)


def check_args(args_num, args):

    # function to check command line arguments and incorporate error handling

    if args_num != 2:
        raise ValueError("wrong number of command line arguments")
    if args[1] != "-c":
        raise ValueError(f"unexpected command line argument {args[1]}")


if __name__ == "__main__":

    args_num = len(sys.argv) - 1
    if args_num > 0:
        try:
            check_args(args_num, sys.argv)
            print(eval(sys.argv[2]))
        except ValueError as e:
            print(e)
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            print(eval(cmdline))
