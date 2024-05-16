// Generated from /home/ms/Dokumenty/Inf_Stosowana/SEM_1/JFIK/Projekt/compiler/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, WRITE=5, READ=6, TOINT=7, TOREAL=8, ID=9, 
		INT=10, REAL=11, DIVOP=12, MULOP=13, ADDOP=14, SUBOP=15, NEWLINE=16, WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "WRITE", "READ", "TOINT", "TOREAL", "ID", 
			"INT", "REAL", "DIVOP", "MULOP", "ADDOP", "SUBOP", "NEWLINE", "WS"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0011p\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0004\bI\b\b\u000b"+
		"\b\f\bJ\u0001\t\u0004\tN\b\t\u000b\t\f\tO\u0001\n\u0004\nS\b\n\u000b\n"+
		"\f\nT\u0001\n\u0001\n\u0004\nY\b\n\u000b\n\f\nZ\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0003"+
		"\u000ff\b\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010k\b\u0010"+
		"\u000b\u0010\f\u0010l\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011\u0001\u0000\u0002\u0002\u0000AZaz\u0002\u0000"+
		"\t\t  u\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0001#\u0001\u0000\u0000\u0000\u0003)\u0001"+
		"\u0000\u0000\u0000\u0005+\u0001\u0000\u0000\u0000\u0007-\u0001\u0000\u0000"+
		"\u0000\t/\u0001\u0000\u0000\u0000\u000b5\u0001\u0000\u0000\u0000\r:\u0001"+
		"\u0000\u0000\u0000\u000f@\u0001\u0000\u0000\u0000\u0011H\u0001\u0000\u0000"+
		"\u0000\u0013M\u0001\u0000\u0000\u0000\u0015R\u0001\u0000\u0000\u0000\u0017"+
		"\\\u0001\u0000\u0000\u0000\u0019^\u0001\u0000\u0000\u0000\u001b`\u0001"+
		"\u0000\u0000\u0000\u001db\u0001\u0000\u0000\u0000\u001fe\u0001\u0000\u0000"+
		"\u0000!j\u0001\u0000\u0000\u0000#$\u0005<\u0000\u0000$%\u0005E\u0000\u0000"+
		"%&\u0005O\u0000\u0000&\'\u0005F\u0000\u0000\'(\u0005>\u0000\u0000(\u0002"+
		"\u0001\u0000\u0000\u0000)*\u0005=\u0000\u0000*\u0004\u0001\u0000\u0000"+
		"\u0000+,\u0005(\u0000\u0000,\u0006\u0001\u0000\u0000\u0000-.\u0005)\u0000"+
		"\u0000.\b\u0001\u0000\u0000\u0000/0\u0005w\u0000\u000001\u0005r\u0000"+
		"\u000012\u0005i\u0000\u000023\u0005t\u0000\u000034\u0005e\u0000\u0000"+
		"4\n\u0001\u0000\u0000\u000056\u0005r\u0000\u000067\u0005e\u0000\u0000"+
		"78\u0005a\u0000\u000089\u0005d\u0000\u00009\f\u0001\u0000\u0000\u0000"+
		":;\u0005(\u0000\u0000;<\u0005i\u0000\u0000<=\u0005n\u0000\u0000=>\u0005"+
		"t\u0000\u0000>?\u0005)\u0000\u0000?\u000e\u0001\u0000\u0000\u0000@A\u0005"+
		"(\u0000\u0000AB\u0005r\u0000\u0000BC\u0005e\u0000\u0000CD\u0005a\u0000"+
		"\u0000DE\u0005l\u0000\u0000EF\u0005)\u0000\u0000F\u0010\u0001\u0000\u0000"+
		"\u0000GI\u0007\u0000\u0000\u0000HG\u0001\u0000\u0000\u0000IJ\u0001\u0000"+
		"\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000K\u0012"+
		"\u0001\u0000\u0000\u0000LN\u000209\u0000ML\u0001\u0000\u0000\u0000NO\u0001"+
		"\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000"+
		"P\u0014\u0001\u0000\u0000\u0000QS\u000209\u0000RQ\u0001\u0000\u0000\u0000"+
		"ST\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000VX\u0005.\u0000\u0000WY\u000209\u0000"+
		"XW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000"+
		"\u0000Z[\u0001\u0000\u0000\u0000[\u0016\u0001\u0000\u0000\u0000\\]\u0005"+
		"/\u0000\u0000]\u0018\u0001\u0000\u0000\u0000^_\u0005*\u0000\u0000_\u001a"+
		"\u0001\u0000\u0000\u0000`a\u0005+\u0000\u0000a\u001c\u0001\u0000\u0000"+
		"\u0000bc\u0005-\u0000\u0000c\u001e\u0001\u0000\u0000\u0000df\u0005\r\u0000"+
		"\u0000ed\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fg\u0001\u0000"+
		"\u0000\u0000gh\u0005\n\u0000\u0000h \u0001\u0000\u0000\u0000ik\u0007\u0001"+
		"\u0000\u0000ji\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000lj\u0001"+
		"\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000"+
		"no\u0006\u0010\u0000\u0000o\"\u0001\u0000\u0000\u0000\u0007\u0000JOTZ"+
		"el\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}