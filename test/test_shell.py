import unittest
import os
from shell import eval
from Applications import (Argument, Call, Seq, Pipe, Redirection,
                          Pattern, SingleQuoted, DoubleQuoted, BackQuoted,
                          Quoted, Application)
from Visitor import Visitor


class TestShell(unittest.TestCase):

    # Test applications

    def test_application(self):
        instance = Application()
        self.assertEqual(instance.run(None, None), None)

    def test_ls(self):
        output = eval("cd test; ls")
        self.assertEqual(output, "\ntest_shell.py\n__pycache__\n")
        eval("cd ..")

    def test_ls_wrong_args(self):
        output = eval("ls a b")
        self.assertEqual(output, "wrong number of command line arguments")

    def ls_dir_not_found(self):
        output = eval("ls thisisntadir")
        self.assertEqual(output, "directory thisisntadir does not exist")

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

    def test_cd_wrong_args(self):
        output = eval("cd")
        self.assertEqual(output, "wrong number of command line arguments")

    def test_pwd(self):
        output = eval("pwd")
        self.assertEqual(output, "/comp0010\n")

    def test_cat(self):
        output = eval("cat test.txt")
        out = ""
        with open('test.txt') as f:
            out += f.read()
        self.assertEqual(output, f"{out}")

    def test_cat_file_not_found(self):
        output = eval("cat notfound")
        self.assertEqual(output, "file notfound does not exist")

    def test_head(self):
        output = eval("head -n 2 requirements.txt")
        self.assertEqual(output, "nose2\ncoverage\n")

    def test_head_wrong_args(self):
        output = eval("head -n 2 requirements.txt test.txt")
        self.assertEqual(output, "wrong number of command line arguments")

    def test_head_wrong_flag(self):
        output = eval("head -a 2 requirements.txt")
        self.assertEqual(output, "wrong flags")

    def test_head_file_not_found(self):
        output = eval("head nonexistent.txt")
        self.assertEqual(output, "file nonexistent.txt does not exist")

    def test_tail(self):
        output = eval("tail -n 2 requirements.txt")
        self.assertEqual(output,
                         "antlr4-python3-runtime==4.13.1\nantlr4-tools==0.2\n")

    def test_tail_wrong_flag(self):
        output = eval("tail -a 2 requirements.txt")
        self.assertEqual(output, "wrong flags")

    def test_tail_wrong_args(self):
        output = eval("tail -n 2 requirements.txt test.txt")
        self.assertEqual(output, "wrong number of command line arguments")

    def test_tail_one_arg(self):
        output = eval("tail test.txt")
        expected = ""
        with open('test.txt') as f:
            expected += f.read()
        self.assertEqual(output, f"{expected}")

    def test_tail_file_not_found(self):
        output = eval("tail nonexistent.txt")
        self.assertEqual(output, "file nonexistent.txt does not exist")

    def test_grep(self):
        output = eval("grep 'fla..' requirements.txt")
        self.assertEqual(output, "flake8==3.8.0\nflake8-html\n")

    def test_grep_wrong_args(self):
        output = eval("grep wrongargs")
        self.assertEqual(output, "wrong number of command line arguments")

    def test_uniq(self):
        output = eval("uniq test.txt")
        arguments = ["\" hel lo\"", 'abc', '\'hello\'', " AAA ", 'test2.txt']
        self.assertEqual(output.split("\n"), arguments)

    def test_uniq_file_not_found(self):
        output = eval("uniq nonexistent.txt")
        self.assertEqual(output, "file nonexistent.txt does not exist")

    def test_uniq_i(self):
        output = eval("uniq -i test.txt")
        arguments = ["\" hel lo\"", 'abc', '\'hello\'', " AAA ", 'test2.txt']
        arguments = [arg.upper() for arg in arguments]
        self.assertEqual(output.split("\n"), arguments)

    def test_sort(self):
        output = eval("sort test.txt")
        arguments = [" AAA ", "\" hel lo\"",
                     '\'hello\'', 'abc', 'test2.txt', '']
        self.assertEqual(output.split("\n"), arguments)

    def test_sort_reverse(self):
        output = eval("sort -r test.txt")
        arguments = ['test2.txt', 'abc', '\'hello\'',
                     "\" hel lo\"", " AAA ", '']
        self.assertEqual(output.split("\n"), arguments)

    def test_sort_file_not_found(self):
        output = eval("sort nonexistent.txt")
        self.assertEqual(output, "file nonexistent.txt does not exist")

    def test_find(self):
        output = eval("find -name \'*.txt\'")
        output = sorted(output.split("\n"))
        self.assertEqual(
            output,
            sorted(
                "./requirements.txt\n./test2.txt\n\
                ./testfile.txt\n./test.txt".replace(" ", "").split("\n")
            ),
        )

    def test_cut(self):
        output = eval("cut -b 1 test.txt")
        self.assertEqual(output.split("\n"),
                         ["\"", "a", "\'", " ", "t", ''])

    def test_cut_overlapping(self):
        output = eval("cut -b 1-3,2 test.txt")
        self.assertEqual(output.split("\n"),
                         ["\" h", "abc", "\'he", " AA", "tes", ''])

    def test_cut_wrong_line(self):
        output = eval("cut -b 1-5 test.txt")
        self.assertEqual(output, "Index out of bounds")

    def test_cut_incorrect_options(self):
        output = eval("cut -b 5-1 test.txt")
        self.assertEqual(output, "Incorrect format for byte range")

    def test_cut_pre_interval(self):
        output = eval("cut -b 2- test.txt")
        self.assertEqual(output.split("\n"),
                         [" hel lo\"", "bc", "hello\'",
                          "AAA ", "est2.txt", ''])

    def test_cut_post_interval(self):
        output = eval("cut -b -2 test.txt")
        self.assertEqual(output.split("\n"),
                         ["\" ", "ab", "\'h", " A", "te", ''])

    def test_cut_wrong_option(self):
        output = eval("cut -c 1 test.txt")
        self.assertEqual(output,
                         "wrong number of command line arguments or flags")

    def test_cut_file_not_found(self):
        output = eval("cut -b 1 nonexistent.txt")
        self.assertEqual(output, "file nonexistent.txt does not exist")

    def test_wc(self):
        output = eval("wc test.txt").strip().split()
        line_count = "5"
        word_count = "7"
        byte_count = "37"
        self.assertEqual(output, [line_count, word_count, byte_count])

    def test_wc_l(self):
        output = eval("wc -l test.txt").strip().split()
        line_count = "5"
        self.assertEqual(output, [line_count])

    def test_wc_w(self):
        output = eval("wc -w test.txt").strip().split()
        word_count = "7"
        self.assertEqual(output, [word_count])

    def test_wc_m(self):
        output = eval("wc -m test.txt").strip().split()
        byte_count = '37'
        self.assertEqual(output, [byte_count])

    def test_wc_wrong_args(self):
        output = eval("wc")
        self.assertEqual(output,
                         "wrong number of command line arguments")

    def test_wc_file_not_found(self):
        output = eval("wc nonexistent.txt")
        self.assertEqual(output,
                         "file nonexistent.txt does not exist")

    def test_unsafe(self):
        output = eval("_cd ; echo hi")
        self.assertEqual(output,
                         "wrong number of command line arguments" +
                         "\nhi")

    # Test functionalities
    # (quotes, substitution, redirection, pipe, sequence, etc.)

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

    def test_input_redirection_wrong_file(self):
        output = eval("cat < nonexistent.txt")
        self.assertEqual(str(output), str("file nonexistent.txt not found"))

    def test_pipe(self):
        output = eval("cat test.txt | grep abc")
        self.assertEqual(output, "abc\n")

    def test_multiple_pipe(self):
        output = eval("cat test.txt | grep \" *\" | grep abc")
        self.assertEqual(output, "abc\n")

    def test_pipe_with_error(self):
        output = eval("cat doesnotexist.txt | grep abc")
        self.assertEqual(output, "")

    def test_sequence(self):
        output = eval("echo foo ; echo bar")
        self.assertEqual(output, "foo\nbar")

    def test_sequence_with_error(self):
        output = eval("grep 'abc' notadirectory ; echo hi ")
        self.assertEqual(output, "")

    def test_sequence_substitution_with_error(self):
        output = eval("`cat notadirectory.txt` ; echo hi ")
        self.assertEqual(output, "")

    def test_multiple_sequence(self):
        output = eval("echo foo ; echo bar ; echo great")
        self.assertEqual(output, "foo\nbar\ngreat")

    def test_sequence_substitution(self):
        output = eval("echo `echo foo; echo bar`")
        self.assertEqual(output, "foo bar")

    def test_globbing(self):
        output = eval("echo *.txt")
        output = sorted(output.split(" "))
        self.assertEqual(
            output,
            sorted(["requirements.txt", "test2.txt",
                    "testfile.txt", "test.txt"])
        )

    def test_globbing_files(self):
        output = eval("echo test/*")
        self.assertEqual(output, "test/test_shell.py test/__pycache__")

    def test_globbing_files_not_found(self):
        output = eval("thisisntafile/*")
        self.assertEqual(output, "directory thisisntafile does not exist")

    # Test str and repr

    def test_to_string_call(self):
        object_to_string = str(Call([Argument(['echo']), Argument(['hello'])]))
        self.assertEqual(object_to_string,
                         "Call(Argument(['echo']), [Argument(['hello'])])")

    def test_unknown_command(self):
        output = eval("unknowncommand")
        self.assertEqual(output, "unknowncommand is an unknown command")

    def test_to_string_sequence(self):
        object_to_string = str(Seq(Call(
            [Argument(['echo']), Argument(['a'])]),
            Call([Argument(['echo']), Argument(['b'])])))
        self.assertEqual(object_to_string,
                         "Seq(Call(Argument(['echo']), " +
                         "[Argument(['a'])]), " +
                         "Call(Argument(['echo']), " +
                         "[Argument(['b'])]))")

    def test_to_string_pipe(self):
        object_to_string = str(Pipe(Call(
            [Argument(['cat']),
                Argument(['test.txt'])]),
                Call([Argument(['grep']),
                     Argument(['.'])])))
        self.assertEqual(object_to_string,
                         "Pipe(Call(Argument(['cat']), " +
                         "[Argument(['test.txt'])]), " +
                         "Call(Argument(['grep']), " +
                         "[Argument(['.'])]))")

    def test_to_string_redirection(self):
        object_to_string = str(Redirection(Call(
            [Argument(['echo']),
                Argument(['foo'])]),
            '>',
            Argument(['newfile.txt'])))
        self.assertEqual(object_to_string,
                         "Redirection(Call(Argument(['echo']), " +
                         "[Argument(['foo'])]), " +
                         ">, " +
                         "Argument(['newfile.txt']))")

    def test_to_string_pattern(self):
        object_to_string = str(Pattern('*.txt'))
        self.assertEqual(object_to_string, "Pattern(.*.txt)")

    def test_repr_pattern(self):
        object_to_string = repr(Pattern('*.txt'))
        self.assertEqual(object_to_string, "Pattern(.*.txt)")

    def test_to_string_single_quoted(self):
        object_to_string = str(SingleQuoted("'hello'"))
        self.assertEqual(object_to_string, "SingleQuoted(hello)")

    def test_repr_single_quoted(self):
        object_to_string = repr(SingleQuoted("'hello'"))
        self.assertEqual(object_to_string, "SingleQuoted(hello)")

    def test_to_string_double_quoted(self):
        object_to_string = str(DoubleQuoted('"hello"'))
        self.assertEqual(object_to_string, 'DoubleQuoted(hello)')

    def test_repr_double_quoted(self):
        object_to_string = repr(DoubleQuoted('"hello"'))
        self.assertEqual(object_to_string, 'DoubleQuoted(hello)')

    def test_to_string_back_quoted(self):
        object_to_string = str(BackQuoted("`echo hello`"))
        self.assertEqual(object_to_string, "BackQuoted(echo hello)")

    def test_repr_back_quoted(self):
        object_to_string = repr(BackQuoted("`echo hello`"))
        self.assertEqual(object_to_string, "BackQuoted(echo hello)")

    def test_to_string_quoted(self):
        object_to_string = str(Quoted("'hello'"))
        self.assertEqual(object_to_string, "Quoted(hello)")


if __name__ == "__main__":
    unittest.main()
