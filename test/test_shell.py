import unittest
import os
from shell import evaluate, convert

def eval(cmdline):
    try :
        return evaluate(convert(cmdline))
    except ValueError as e:
        return str(e)

class TestShell(unittest.TestCase):
    def test_ls(self):
        output = eval("cd test; ls")
        self.assertEqual(output, "\ntest_shell.py\n__pycache__\n")
        eval("cd ..")
    def test_echo(self):
        output = eval("echo foo")
        self.assertEqual(output, "foo")
    def test_echo_semicolon_in_quotes(self):
        output = eval('echo "foo ; foo2"')
        self.assertEqual(output, "foo ; foo2")
    def test_cd(self):
        output = eval("cd comp0010")
        self.assertEqual(os.getcwd(), "/comp0010")
    def test_pwd(self):
        output = eval("pwd")
        self.assertEqual(output, "/comp0010\n")
    def test_cat(self):
        output = eval("cat test.txt")
        out = ""
        with open('test.txt') as f:
            out += f.read()
        self.assertEqual(output, f"{out}")
    def test_head(self):
        output = eval("head -n 2 requirements.txt")
        self.assertEqual(output, "nose2\ncoverage\n")
    def test_tail(self):
        output = eval("tail -n 2 requirements.txt")
        self.assertEqual(output, "antlr4-python3-runtime==4.13.1\nantlr4-tools==0.2\n")
    def test_grep(self):
        output = eval("grep 'fla..' requirements.txt")
        self.assertEqual(output, "flake8==3.8.0\nflake8-html\n")

    def test_substitution(self):
        output = eval("echo `echo hello`")
        self.assertEqual(output, "hello")
    def test_redirection(self):
        output = eval("echo foo > newfile.txt ; cat newfile.txt")
        self.assertEqual(output, "\nfoo")
    def test_input_redirection(self):
        output = eval("cat < test.txt")
        out = ""
        with open('test.txt') as f:
            out += f.read()
        self.assertEqual(output, f"{out}")
    def test_pipe(self):
        output = eval("echo foo | cat")
        self.assertEqual(output, "foo")
    def test_globbing(self):
        output = eval("*.txt")
        self.assertEqual(output, "requirements.txt test2.txt testfile.txt test.txt")

if __name__ == "__main__":
    unittest.main()
