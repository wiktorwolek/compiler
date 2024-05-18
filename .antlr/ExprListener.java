// Generated from /home/ms/Dokumenty/Inf_Stosowana/SEM_1/JFIK/Projekt/compiler/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(ExprParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(ExprParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ExprParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ExprParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(ExprParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(ExprParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#write}.
	 * @param ctx the parse tree
	 */
	void enterWrite(ExprParser.WriteContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#write}.
	 * @param ctx the parse tree
	 */
	void exitWrite(ExprParser.WriteContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#read}.
	 * @param ctx the parse tree
	 */
	void enterRead(ExprParser.ReadContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#read}.
	 * @param ctx the parse tree
	 */
	void exitRead(ExprParser.ReadContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expression1}.
	 * @param ctx the parse tree
	 */
	void enterExpression1(ExprParser.Expression1Context ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expression1}.
	 * @param ctx the parse tree
	 */
	void exitExpression1(ExprParser.Expression1Context ctx);
	/**
	 * Enter a parse tree produced by the {@code int}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterInt(ExprParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code int}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitInt(ExprParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by the {@code real}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterReal(ExprParser.RealContext ctx);
	/**
	 * Exit a parse tree produced by the {@code real}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitReal(ExprParser.RealContext ctx);
	/**
	 * Enter a parse tree produced by the {@code toint}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterToint(ExprParser.TointContext ctx);
	/**
	 * Exit a parse tree produced by the {@code toint}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitToint(ExprParser.TointContext ctx);
	/**
	 * Enter a parse tree produced by the {@code toreal}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterToreal(ExprParser.TorealContext ctx);
	/**
	 * Exit a parse tree produced by the {@code toreal}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitToreal(ExprParser.TorealContext ctx);
	/**
	 * Enter a parse tree produced by the {@code par}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterPar(ExprParser.ParContext ctx);
	/**
	 * Exit a parse tree produced by the {@code par}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitPar(ExprParser.ParContext ctx);
	/**
	 * Enter a parse tree produced by the {@code id}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void enterId(ExprParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code id}
	 * labeled alternative in {@link ExprParser#expression2}.
	 * @param ctx the parse tree
	 */
	void exitId(ExprParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#add}.
	 * @param ctx the parse tree
	 */
	void enterAdd(ExprParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#add}.
	 * @param ctx the parse tree
	 */
	void exitAdd(ExprParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#multiply}.
	 * @param ctx the parse tree
	 */
	void enterMultiply(ExprParser.MultiplyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#multiply}.
	 * @param ctx the parse tree
	 */
	void exitMultiply(ExprParser.MultiplyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#divide}.
	 * @param ctx the parse tree
	 */
	void enterDivide(ExprParser.DivideContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#divide}.
	 * @param ctx the parse tree
	 */
	void exitDivide(ExprParser.DivideContext ctx);
}