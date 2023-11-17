// Generated from c:/Users/ayman/OneDrive/Documents/Comp10Project/comp0010-shell-python-p15/src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ShellGrammarParser}.
 */
public interface ShellGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#s}.
	 * @param ctx the parse tree
	 */
	void enterS(ShellGrammarParser.SContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#s}.
	 * @param ctx the parse tree
	 */
	void exitS(ShellGrammarParser.SContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ShellGrammarParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ShellGrammarParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(ShellGrammarParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(ShellGrammarParser.RedirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(ShellGrammarParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(ShellGrammarParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(ShellGrammarParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(ShellGrammarParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(ShellGrammarParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(ShellGrammarParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellGrammarParser#quoted}.
	 * @param ctx the parse tree
	 */
	void enterQuoted(ShellGrammarParser.QuotedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellGrammarParser#quoted}.
	 * @param ctx the parse tree
	 */
	void exitQuoted(ShellGrammarParser.QuotedContext ctx);
}