import unittest
import os
from shell import evaluate, convert

def eval(cmdline):
    try :
        return evaluate(convert(cmdline))
    except ValueError as e:
        return str(e)

class TestShell(unittest.TestCase):
    # def test_shell(self):
    #     out = deque()
    #     eval("echo foo", out)
    #     self.assertEqual(out.popleft(), "foo\n")
    #     self.assertEqual(len(out), 0)
    # def grep_test_re(self):
    #     cmdline = "grep 'fla..' comp0010/requirements.txt"
    #     self.assertEqual(eval(cmdline), "flake8==3.8.0\nflake8-html\n")
    # def echo_quotes_test(self):
    #     out = deque()
    #     eval("echo 'foo'", out)
    #     self.assertEqual(out.popleft(), "foo\n")
    #     self.assertEqual(len(out), 0)
    # def echo_semicolon_test(self):
    #     out = deque()
    #     eval("echo hello; echo world ; echo something", out)
    #     self.assertEqual(out.popleft(), "hello\nworld\nsomething\n")
    #     self.assertEqual(len(out), 0)
    def test_cd(self):
        output = eval("cd comp0010")
        self.assertEqual(os.getcwd(), "/comp0010")
    def test_echo(self):
        output = eval("echo foo")
        self.assertEqual(output, "foo")
    def test_echo_semicolon_in_quotes(self):
        output = eval('echo "foo ; foo2"')
        self.assertEqual(output, "foo ; foo2")
    def test_substitution(self):
        output = eval("echo `echo hello`")
        self.assertEqual(output, "hello")
    def test_redirection(self):
        output = eval("echo foo > test.txt")
        self.assertEqual(output, "")
    def test_pipe(self):
        output = eval("echo foo | cat")
        self.assertEqual(output, "foo")


if __name__ == "__main__":
    unittest.main()
