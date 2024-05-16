// Generated from c:/Users/wolek/source/repos/compiler/Expr.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, CALL=9, 
		FUNCTION=10, ENDFUNCTION=11, WRITE=12, READ=13, TOINT=14, TOREAL=15, ID=16, 
		INT=17, REAL=18, ADDOP=19, MULOP=20, DIVOP=21, NEWLINE=22, WS=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "CALL", 
			"FUNCTION", "ENDFUNCTION", "WRITE", "READ", "TOINT", "TOREAL", "ID", 
			"INT", "REAL", "ADDOP", "MULOP", "DIVOP", "NEWLINE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<EOF>'", "'='", "'['", "';'", "']'", "','", "'('", "')'", "'call'", 
			"'function'", "'endfunction'", "'write'", "'read'", "'(int)'", "'(real)'", 
			null, null, null, "'+'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "CALL", "FUNCTION", 
			"ENDFUNCTION", "WRITE", "READ", "TOINT", "TOREAL", "ID", "INT", "REAL", 
			"ADDOP", "MULOP", "DIVOP", "NEWLINE", "WS"
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
		"\u0004\u0000\u0017\u009c\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000fw\b\u000f\u000b\u000f"+
		"\f\u000fx\u0001\u0010\u0004\u0010|\b\u0010\u000b\u0010\f\u0010}\u0001"+
		"\u0011\u0004\u0011\u0081\b\u0011\u000b\u0011\f\u0011\u0082\u0001\u0011"+
		"\u0001\u0011\u0004\u0011\u0087\b\u0011\u000b\u0011\f\u0011\u0088\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0003\u0015\u0092\b\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0004"+
		"\u0016\u0097\b\u0016\u000b\u0016\f\u0016\u0098\u0001\u0016\u0001\u0016"+
		"\u0000\u0000\u0017\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015"+
		"+\u0016-\u0017\u0001\u0000\u0002\u0002\u0000AZaz\u0002\u0000\t\t  \u00a1"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0001/"+
		"\u0001\u0000\u0000\u0000\u00035\u0001\u0000\u0000\u0000\u00057\u0001\u0000"+
		"\u0000\u0000\u00079\u0001\u0000\u0000\u0000\t;\u0001\u0000\u0000\u0000"+
		"\u000b=\u0001\u0000\u0000\u0000\r?\u0001\u0000\u0000\u0000\u000fA\u0001"+
		"\u0000\u0000\u0000\u0011C\u0001\u0000\u0000\u0000\u0013H\u0001\u0000\u0000"+
		"\u0000\u0015Q\u0001\u0000\u0000\u0000\u0017]\u0001\u0000\u0000\u0000\u0019"+
		"c\u0001\u0000\u0000\u0000\u001bh\u0001\u0000\u0000\u0000\u001dn\u0001"+
		"\u0000\u0000\u0000\u001fv\u0001\u0000\u0000\u0000!{\u0001\u0000\u0000"+
		"\u0000#\u0080\u0001\u0000\u0000\u0000%\u008a\u0001\u0000\u0000\u0000\'"+
		"\u008c\u0001\u0000\u0000\u0000)\u008e\u0001\u0000\u0000\u0000+\u0091\u0001"+
		"\u0000\u0000\u0000-\u0096\u0001\u0000\u0000\u0000/0\u0005<\u0000\u0000"+
		"01\u0005E\u0000\u000012\u0005O\u0000\u000023\u0005F\u0000\u000034\u0005"+
		">\u0000\u00004\u0002\u0001\u0000\u0000\u000056\u0005=\u0000\u00006\u0004"+
		"\u0001\u0000\u0000\u000078\u0005[\u0000\u00008\u0006\u0001\u0000\u0000"+
		"\u00009:\u0005;\u0000\u0000:\b\u0001\u0000\u0000\u0000;<\u0005]\u0000"+
		"\u0000<\n\u0001\u0000\u0000\u0000=>\u0005,\u0000\u0000>\f\u0001\u0000"+
		"\u0000\u0000?@\u0005(\u0000\u0000@\u000e\u0001\u0000\u0000\u0000AB\u0005"+
		")\u0000\u0000B\u0010\u0001\u0000\u0000\u0000CD\u0005c\u0000\u0000DE\u0005"+
		"a\u0000\u0000EF\u0005l\u0000\u0000FG\u0005l\u0000\u0000G\u0012\u0001\u0000"+
		"\u0000\u0000HI\u0005f\u0000\u0000IJ\u0005u\u0000\u0000JK\u0005n\u0000"+
		"\u0000KL\u0005c\u0000\u0000LM\u0005t\u0000\u0000MN\u0005i\u0000\u0000"+
		"NO\u0005o\u0000\u0000OP\u0005n\u0000\u0000P\u0014\u0001\u0000\u0000\u0000"+
		"QR\u0005e\u0000\u0000RS\u0005n\u0000\u0000ST\u0005d\u0000\u0000TU\u0005"+
		"f\u0000\u0000UV\u0005u\u0000\u0000VW\u0005n\u0000\u0000WX\u0005c\u0000"+
		"\u0000XY\u0005t\u0000\u0000YZ\u0005i\u0000\u0000Z[\u0005o\u0000\u0000"+
		"[\\\u0005n\u0000\u0000\\\u0016\u0001\u0000\u0000\u0000]^\u0005w\u0000"+
		"\u0000^_\u0005r\u0000\u0000_`\u0005i\u0000\u0000`a\u0005t\u0000\u0000"+
		"ab\u0005e\u0000\u0000b\u0018\u0001\u0000\u0000\u0000cd\u0005r\u0000\u0000"+
		"de\u0005e\u0000\u0000ef\u0005a\u0000\u0000fg\u0005d\u0000\u0000g\u001a"+
		"\u0001\u0000\u0000\u0000hi\u0005(\u0000\u0000ij\u0005i\u0000\u0000jk\u0005"+
		"n\u0000\u0000kl\u0005t\u0000\u0000lm\u0005)\u0000\u0000m\u001c\u0001\u0000"+
		"\u0000\u0000no\u0005(\u0000\u0000op\u0005r\u0000\u0000pq\u0005e\u0000"+
		"\u0000qr\u0005a\u0000\u0000rs\u0005l\u0000\u0000st\u0005)\u0000\u0000"+
		"t\u001e\u0001\u0000\u0000\u0000uw\u0007\u0000\u0000\u0000vu\u0001\u0000"+
		"\u0000\u0000wx\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001"+
		"\u0000\u0000\u0000y \u0001\u0000\u0000\u0000z|\u000209\u0000{z\u0001\u0000"+
		"\u0000\u0000|}\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001"+
		"\u0000\u0000\u0000~\"\u0001\u0000\u0000\u0000\u007f\u0081\u000209\u0000"+
		"\u0080\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000"+
		"\u0082\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0086\u0005.\u0000\u0000\u0085"+
		"\u0087\u000209\u0000\u0086\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001"+
		"\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001"+
		"\u0000\u0000\u0000\u0089$\u0001\u0000\u0000\u0000\u008a\u008b\u0005+\u0000"+
		"\u0000\u008b&\u0001\u0000\u0000\u0000\u008c\u008d\u0005*\u0000\u0000\u008d"+
		"(\u0001\u0000\u0000\u0000\u008e\u008f\u0005/\u0000\u0000\u008f*\u0001"+
		"\u0000\u0000\u0000\u0090\u0092\u0005\r\u0000\u0000\u0091\u0090\u0001\u0000"+
		"\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0005\n\u0000\u0000\u0094,\u0001\u0000\u0000"+
		"\u0000\u0095\u0097\u0007\u0001\u0000\u0000\u0096\u0095\u0001\u0000\u0000"+
		"\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000"+
		"\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099\u009a\u0001\u0000\u0000"+
		"\u0000\u009a\u009b\u0006\u0016\u0000\u0000\u009b.\u0001\u0000\u0000\u0000"+
		"\u0007\u0000x}\u0082\u0088\u0091\u0098\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}