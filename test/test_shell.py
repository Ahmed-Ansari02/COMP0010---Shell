import unittest
import os
from shell import eval
from Applications import (Argument, Call, Seq, Pipe, Redirection,
                          Pattern, SingleQuoted, DoubleQuoted, BackQuoted,
                          Quoted, Application)
from Visitor import Visitor


class TestShell(unittest.TestCase):

    def test_ls(self):
        output = eval("cd test; ls")
        self.assertEqual(output, "\ntest_shell.py\n__pycache__\n")
        eval("cd ..")

    def test_ls_wrong_args(self):
        output = eval("ls a b")
        self.assertEqual(output, "wrong number of command line arguments")

    def test_ls_one_arg(self):
        output = eval("ls test")
        self.assertEqual(output, "test_shell.py\n__pycache__\n")

    def test_echo(self):
        output = eval("echo foo")
        self.assertEqual(output, "foo")

    def test_echo_semicolon_in_quotes(self):
        output = eval('echo "foo ; foo2"')
        self.assertEqual(output, "foo ; foo2")

    def test_cd(self):
        eval("cd comp0010")
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

    def test_head_wrong_args(self):
        output = eval("head -n 2 requirements.txt test.txt")
        self.assertEqual(output, "wrong number of command line arguments")

    def test_head_wrong_flag(self):
        output = eval("head -a 2 requirements.txt")
        self.assertEqual(output, "wrong flags")

    def test_tail(self):
        output = eval("tail -n 2 requirements.txt")
        self.assertEqual(output,
                         "antlr4-python3-runtime==4.13.1\nantlr4-tools==0.2\n")

    def test_grep(self):
        output = eval("grep 'fla..' requirements.txt")
        self.assertEqual(output, "flake8==3.8.0\nflake8-html\n")

    def test_single_quoted(self):
        output = eval("echo 'hello'")
        self.assertEqual(output, "hello")

    def test_double_quoted(self):
        output = eval("echo \"hello\"")
        self.assertEqual(output, "hello")

    def test_substitution(self):
        output = eval("echo `echo hello`")
        self.assertEqual(output, "hello")

    def test_substitution_with_splitting(self):
        cmdline = "echo hello`echo hello`world"
        output = eval(cmdline)
        self.assertEqual(output, "hellohelloworld")

    def test_input_redirection_infront(self):
        cmdline = "< test2.txt cat"
        output = eval(cmdline)
        out = ""
        with open('test2.txt') as f:
            out += f.read()
        self.assertEqual(output, out)

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
        output = eval("cat test.txt | grep abc")
        self.assertEqual(output, "abc\n")

    def test_multiple_pipe(self):
        output = eval("cat test.txt | grep \" *\" | grep abc")
        self.assertEqual(output, "abc\n")

    def test_sequence(self):
        output = eval("echo foo ; echo bar")
        self.assertEqual(output, "foo\nbar")

    def test_sequence_with_error(self):
        output = eval("grep 'abc' notadirectory ; echo hi ")
        self.assertEqual(output, "")

    def test_multiple_sequence(self):
        output = eval("echo foo ; echo bar ; echo great")
        self.assertEqual(output, "foo\nbar\ngreat")

    def test_sequence_substitution(self):
        output = eval("echo `echo foo; echo bar`")
        self.assertEqual(output, "foo bar")

    def test_globbing(self):
        output = eval("*.txt")
        self.assertEqual(output,
                         "requirements.txt test2.txt test.txt testfile.txt")

    def test_globbing_command(self):
        output = eval("echo *.txt")
        self.assertEqual(output,
                         "requirements.txt test2.txt test.txt testfile.txt")

    def test_globbing_files(self):
        output = eval("test/*")
        self.assertEqual(output, "test/test_shell.py test/__pycache__")

    def test_globbing_files_not_found(self):
        output = eval("thisisntafile/*")
        self.assertEqual(output, "directory thisisntafile does not exist")

    def test_to_string_call(self):
        object_to_string = str(Call([Argument(['echo']), Argument(['hello'])]))
        self.assertEqual(object_to_string,
                         "Call(Argument(['echo']), [Argument(['hello'])])")

    def test_to_string_sequence(self):
        object_to_string = str(Seq(Call(
            [Argument(['echo']), Argument(['a'])]),
            Call([Argument(['echo']), Argument(['b'])])))
        self.assertEqual(object_to_string,
                         "Seq(Call(Argument(['echo']),\
        [Argument(['a'])]),\
        Call(Argument(['echo']),\
        [Argument(['b'])]))")

    def test_to_string_pipe(self):
        object_to_string = str(Pipe(Call(
            [Argument(['cat']),
                Argument(['test.txt'])]),
                Call([Argument(['grep']),
                     Argument(['.'])])))
        self.assertEqual(object_to_string,
                         "Pipe(Call(Argument(['cat']),\
            [Argument(['test.txt'])]),\
            Call(Argument(['grep']),\
            [Argument(['.'])]))")

    def test_to_string_redirection(self):
        object_to_string = str(Redirection(Call(
            [Argument(['echo']),
                Argument(['foo'])]),
            '>',
            Argument(['newfile.txt'])))
        self.assertEqual(object_to_string,
                         "Redirection(Call(Argument(['echo']),\
        [Argument(['foo'])]),\
        >,\
        Argument(['newfile.txt']))")

    def test_to_string_pattern(self):
        object_to_string = str(Pattern('*.txt'))
        self.assertEqual(object_to_string, "Pattern(.*.txt)")

    def test_to_string_single_quoted(self):
        object_to_string = str(SingleQuoted("'hello'"))
        self.assertEqual(object_to_string, "SingleQuoted(hello)")

    def test_to_string_double_quoted(self):
        object_to_string = str(DoubleQuoted('"hello"'))
        self.assertEqual(object_to_string, 'DoubleQuoted(hello)')

    def test_to_string_back_quoted(self):
        object_to_string = str(BackQuoted("`echo hello`"))
        self.assertEqual(object_to_string, "BackQuoted(echo hello)")

    def test_to_string_quoted(self):
        object_to_string = str(Quoted("'hello'"))
        self.assertEqual(object_to_string, "Quoted(hello)")

    def test_application(self):
        instance = Application()
        self.assertEqual(instance.run(None, None), None)

    def test_visitor(self):
        instance = Visitor()
        self.assertEqual(True,
                         instance.visit_argument(None) ==
                         instance.visit_back_quoted(None) ==
                         instance.visit_call(None) ==
                         instance.visit_double_quoted(None) ==
                         instance.visit_pattern(None) ==
                         instance.visit_pipe(None) ==
                         instance.visit_seq(None) ==
                         instance.visit_single_quoted(None) ==
                         instance.visit_redirection(None))

    def test_quoted(self):
        instance = Quoted("'hello'")
        self.assertEqual(instance.accept(None), None)


if __name__ == "__main__":
    unittest.main()
