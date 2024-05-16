// Generated from /home/ms/Dokumenty/Inf_Stosowana/SEM_1/JFIK/Projekt/compiler/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, WRITE=5, READ=6, TOINT=7, TOREAL=8, ID=9, 
		INT=10, REAL=11, DIVOP=12, MULOP=13, ADDOP=14, SUBOP=15, NEWLINE=16, WS=17;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_assign = 2, RULE_write = 3, RULE_read = 4, 
		RULE_expression = 5, RULE_expression1 = 6, RULE_expression2 = 7, RULE_add = 8, 
		RULE_substract = 9, RULE_multiply = 10, RULE_divide = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "assign", "write", "read", "expression", "expression1", 
			"expression2", "add", "substract", "multiply", "divide"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<EOF>'", "'='", "'('", "')'", "'write'", "'read'", "'(int)'", 
			"'(real)'", null, null, null, "'/'", "'*'", "'+'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "WRITE", "READ", "TOINT", "TOREAL", "ID", 
			"INT", "REAL", "DIVOP", "MULOP", "ADDOP", "SUBOP", "NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<TerminalNode> NEWLINE() { return getTokens(ExprParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ExprParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 66144L) != 0)) {
				{
				{
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 608L) != 0)) {
					{
					setState(24);
					statement();
					}
				}

				setState(27);
				match(NEWLINE);
				}
				}
				setState(32);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(33);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public WriteContext write() {
			return getRuleContext(WriteContext.class,0);
		}
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(38);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WRITE:
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				write();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				assign();
				}
				break;
			case READ:
				enterOuterAlt(_localctx, 3);
				{
				setState(37);
				read();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(ID);
			setState(41);
			match(T__1);
			setState(42);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteContext extends ParserRuleContext {
		public TerminalNode WRITE() { return getToken(ExprParser.WRITE, 0); }
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_write);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(WRITE);
			setState(45);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(ExprParser.READ, 0); }
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(READ);
			setState(48);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public Expression1Context expression1() {
			return getRuleContext(Expression1Context.class,0);
		}
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public SubstractContext substract() {
			return getRuleContext(SubstractContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expression);
		try {
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				expression1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				add();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				substract();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression1Context extends ParserRuleContext {
		public Expression2Context expression2() {
			return getRuleContext(Expression2Context.class,0);
		}
		public MultiplyContext multiply() {
			return getRuleContext(MultiplyContext.class,0);
		}
		public DivideContext divide() {
			return getRuleContext(DivideContext.class,0);
		}
		public Expression1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression1; }
	}

	public final Expression1Context expression1() throws RecognitionException {
		Expression1Context _localctx = new Expression1Context(_ctx, getState());
		enterRule(_localctx, 12, RULE_expression1);
		try {
			setState(58);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				expression2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				multiply();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(57);
				divide();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression2Context extends ParserRuleContext {
		public Expression2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression2; }
	 
		public Expression2Context() { }
		public void copyFrom(Expression2Context ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParContext extends Expression2Context {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParContext(Expression2Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TointContext extends Expression2Context {
		public TerminalNode TOINT() { return getToken(ExprParser.TOINT, 0); }
		public Expression2Context expression2() {
			return getRuleContext(Expression2Context.class,0);
		}
		public TointContext(Expression2Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TorealContext extends Expression2Context {
		public TerminalNode TOREAL() { return getToken(ExprParser.TOREAL, 0); }
		public Expression2Context expression2() {
			return getRuleContext(Expression2Context.class,0);
		}
		public TorealContext(Expression2Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RealContext extends Expression2Context {
		public TerminalNode REAL() { return getToken(ExprParser.REAL, 0); }
		public RealContext(Expression2Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdContext extends Expression2Context {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public IdContext(Expression2Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends Expression2Context {
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public IntContext(Expression2Context ctx) { copyFrom(ctx); }
	}

	public final Expression2Context expression2() throws RecognitionException {
		Expression2Context _localctx = new Expression2Context(_ctx, getState());
		enterRule(_localctx, 14, RULE_expression2);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				_localctx = new IntContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				match(INT);
				}
				break;
			case REAL:
				_localctx = new RealContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				match(REAL);
				}
				break;
			case TOINT:
				_localctx = new TointContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(62);
				match(TOINT);
				setState(63);
				expression2();
				}
				break;
			case TOREAL:
				_localctx = new TorealContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(64);
				match(TOREAL);
				setState(65);
				expression2();
				}
				break;
			case T__2:
				_localctx = new ParContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(66);
				match(T__2);
				setState(67);
				expression();
				setState(68);
				match(T__3);
				}
				break;
			case ID:
				_localctx = new IdContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(70);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddContext extends ParserRuleContext {
		public Expression1Context expression1() {
			return getRuleContext(Expression1Context.class,0);
		}
		public TerminalNode ADDOP() { return getToken(ExprParser.ADDOP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AddContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add; }
	}

	public final AddContext add() throws RecognitionException {
		AddContext _localctx = new AddContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_add);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			expression1();
			setState(74);
			match(ADDOP);
			setState(75);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SubstractContext extends ParserRuleContext {
		public List<Expression1Context> expression1() {
			return getRuleContexts(Expression1Context.class);
		}
		public Expression1Context expression1(int i) {
			return getRuleContext(Expression1Context.class,i);
		}
		public TerminalNode SUBOP() { return getToken(ExprParser.SUBOP, 0); }
		public SubstractContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_substract; }
	}

	public final SubstractContext substract() throws RecognitionException {
		SubstractContext _localctx = new SubstractContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_substract);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			expression1();
			setState(78);
			match(SUBOP);
			setState(79);
			expression1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplyContext extends ParserRuleContext {
		public List<Expression2Context> expression2() {
			return getRuleContexts(Expression2Context.class);
		}
		public Expression2Context expression2(int i) {
			return getRuleContext(Expression2Context.class,i);
		}
		public TerminalNode MULOP() { return getToken(ExprParser.MULOP, 0); }
		public MultiplyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiply; }
	}

	public final MultiplyContext multiply() throws RecognitionException {
		MultiplyContext _localctx = new MultiplyContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_multiply);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			expression2();
			setState(82);
			match(MULOP);
			setState(83);
			expression2();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DivideContext extends ParserRuleContext {
		public List<Expression2Context> expression2() {
			return getRuleContexts(Expression2Context.class);
		}
		public Expression2Context expression2(int i) {
			return getRuleContext(Expression2Context.class,i);
		}
		public TerminalNode DIVOP() { return getToken(ExprParser.DIVOP, 0); }
		public DivideContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_divide; }
	}

	public final DivideContext divide() throws RecognitionException {
		DivideContext _localctx = new DivideContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_divide);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			expression2();
			setState(86);
			match(DIVOP);
			setState(87);
			expression2();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0011Z\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0003\u0000\u001a\b\u0000\u0001\u0000\u0005\u0000\u001d\b\u0000"+
		"\n\u0000\f\u0000 \t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\'\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u00056\b\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006;\b\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007H\b\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0000\u0000\f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0000\u0000Z\u0000\u001e\u0001\u0000\u0000\u0000\u0002&\u0001"+
		"\u0000\u0000\u0000\u0004(\u0001\u0000\u0000\u0000\u0006,\u0001\u0000\u0000"+
		"\u0000\b/\u0001\u0000\u0000\u0000\n5\u0001\u0000\u0000\u0000\f:\u0001"+
		"\u0000\u0000\u0000\u000eG\u0001\u0000\u0000\u0000\u0010I\u0001\u0000\u0000"+
		"\u0000\u0012M\u0001\u0000\u0000\u0000\u0014Q\u0001\u0000\u0000\u0000\u0016"+
		"U\u0001\u0000\u0000\u0000\u0018\u001a\u0003\u0002\u0001\u0000\u0019\u0018"+
		"\u0001\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u001b"+
		"\u0001\u0000\u0000\u0000\u001b\u001d\u0005\u0010\u0000\u0000\u001c\u0019"+
		"\u0001\u0000\u0000\u0000\u001d \u0001\u0000\u0000\u0000\u001e\u001c\u0001"+
		"\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f!\u0001\u0000"+
		"\u0000\u0000 \u001e\u0001\u0000\u0000\u0000!\"\u0005\u0001\u0000\u0000"+
		"\"\u0001\u0001\u0000\u0000\u0000#\'\u0003\u0006\u0003\u0000$\'\u0003\u0004"+
		"\u0002\u0000%\'\u0003\b\u0004\u0000&#\u0001\u0000\u0000\u0000&$\u0001"+
		"\u0000\u0000\u0000&%\u0001\u0000\u0000\u0000\'\u0003\u0001\u0000\u0000"+
		"\u0000()\u0005\t\u0000\u0000)*\u0005\u0002\u0000\u0000*+\u0003\n\u0005"+
		"\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0005\u0005\u0000\u0000-.\u0005"+
		"\t\u0000\u0000.\u0007\u0001\u0000\u0000\u0000/0\u0005\u0006\u0000\u0000"+
		"01\u0005\t\u0000\u00001\t\u0001\u0000\u0000\u000026\u0003\f\u0006\u0000"+
		"36\u0003\u0010\b\u000046\u0003\u0012\t\u000052\u0001\u0000\u0000\u0000"+
		"53\u0001\u0000\u0000\u000054\u0001\u0000\u0000\u00006\u000b\u0001\u0000"+
		"\u0000\u00007;\u0003\u000e\u0007\u00008;\u0003\u0014\n\u00009;\u0003\u0016"+
		"\u000b\u0000:7\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000:9\u0001"+
		"\u0000\u0000\u0000;\r\u0001\u0000\u0000\u0000<H\u0005\n\u0000\u0000=H"+
		"\u0005\u000b\u0000\u0000>?\u0005\u0007\u0000\u0000?H\u0003\u000e\u0007"+
		"\u0000@A\u0005\b\u0000\u0000AH\u0003\u000e\u0007\u0000BC\u0005\u0003\u0000"+
		"\u0000CD\u0003\n\u0005\u0000DE\u0005\u0004\u0000\u0000EH\u0001\u0000\u0000"+
		"\u0000FH\u0005\t\u0000\u0000G<\u0001\u0000\u0000\u0000G=\u0001\u0000\u0000"+
		"\u0000G>\u0001\u0000\u0000\u0000G@\u0001\u0000\u0000\u0000GB\u0001\u0000"+
		"\u0000\u0000GF\u0001\u0000\u0000\u0000H\u000f\u0001\u0000\u0000\u0000"+
		"IJ\u0003\f\u0006\u0000JK\u0005\u000e\u0000\u0000KL\u0003\n\u0005\u0000"+
		"L\u0011\u0001\u0000\u0000\u0000MN\u0003\f\u0006\u0000NO\u0005\u000f\u0000"+
		"\u0000OP\u0003\f\u0006\u0000P\u0013\u0001\u0000\u0000\u0000QR\u0003\u000e"+
		"\u0007\u0000RS\u0005\r\u0000\u0000ST\u0003\u000e\u0007\u0000T\u0015\u0001"+
		"\u0000\u0000\u0000UV\u0003\u000e\u0007\u0000VW\u0005\f\u0000\u0000WX\u0003"+
		"\u000e\u0007\u0000X\u0017\u0001\u0000\u0000\u0000\u0006\u0019\u001e&5"+
		":G";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}