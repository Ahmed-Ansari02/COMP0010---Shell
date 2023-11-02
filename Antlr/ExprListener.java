// Generated from Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ExprParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ExprParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ExprParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ExprParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#simpleCommand}.
	 * @param ctx the parse tree
	 */
	void enterSimpleCommand(ExprParser.SimpleCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#simpleCommand}.
	 * @param ctx the parse tree
	 */
	void exitSimpleCommand(ExprParser.SimpleCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(ExprParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(ExprParser.ArgContext ctx);
}