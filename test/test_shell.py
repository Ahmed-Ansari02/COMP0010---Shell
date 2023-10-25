import unittest

from shell import eval
from collections import deque


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)
    def echo_quotes_test(self):
        out = deque()
        eval("echo 'foo'", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)
    def echo_semicolon_test(self):
        out = deque()
        eval("echo hello; echo world ; echo something", out)
        self.assertEqual(out.popleft(), "hello\nworld\nsomething\n")
        self.assertEqual(len(out), 0)
    def echo_semicolon_in_quotes_test(self):
        out = deque()
        eval('echo "foo ; foo2"', out)
        self.assertEqual(out.popleft(), "foo ; foo2\n")
        self.assertEqual(len(out), 0)
    def echo_quotes_test_2(self):
        out = deque()
        eval('echo "foo"', out)
        self.assertEqual(out.popleft(), "\"foo\"\n")
        self.assertEqual(len(out), 0)

if __name__ == "__main__":
    unittest.main()
