// Generated from c:/Users/ayman/OneDrive/Documents/Comp10Project/comp0010-shell-python-p15/src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ShellGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, WHITESPACE=5, APPLICATION=6, UNQUOTED=7, 
		SINGLE_QUOTED=8, DOUBLE_QUOTED=9, BACK_QUOTED=10, WS=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "WHITESPACE", "APPLICATION", "UNQUOTED", 
			"NOT_QUOTED", "NOT_SINGLE_QUOTED", "NOT_DOUBLE_QUOTED", "NOT_BACK_QUOTED", 
			"NOT_DOUBLE_BACK_QUOTED", "QUOTED", "SINGLE_QUOTED", "DOUBLE_QUOTED", 
			"BACK_QUOTED", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'<'", "'>'", "'|'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "WHITESPACE", "APPLICATION", "UNQUOTED", 
			"SINGLE_QUOTED", "DOUBLE_QUOTED", "BACK_QUOTED", "WS"
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


	public ShellGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ShellGrammar.g4"; }

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
		"\u0004\u0000\u000b\u0087\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0004\u0004-\b\u0004\u000b\u0004\f\u0004.\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005>\b\u0005\u0001\u0006\u0004\u0006A\b\u0006\u000b\u0006\f\u0006B"+
		"\u0001\u0007\u0004\u0007F\b\u0007\u000b\u0007\f\u0007G\u0001\b\u0004\b"+
		"K\b\b\u000b\b\f\bL\u0001\t\u0004\tP\b\t\u000b\t\f\tQ\u0001\n\u0004\nU"+
		"\b\n\u000b\n\f\nV\u0001\u000b\u0004\u000bZ\b\u000b\u000b\u000b\f\u000b"+
		"[\u0001\f\u0001\f\u0001\f\u0003\fa\b\f\u0001\r\u0001\r\u0001\r\u0005\r"+
		"f\b\r\n\r\f\ri\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0005\u000ep\b\u000e\n\u000e\f\u000es\t\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000fz\b\u000f\n\u000f\f\u000f"+
		"}\t\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010\u0082\b\u0010"+
		"\u000b\u0010\f\u0010\u0083\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\u0000\u0011\u0000\u0013\u0000\u0015\u0000\u0017\u0000\u0019\u0000"+
		"\u001b\b\u001d\t\u001f\n!\u000b\u0001\u0000\b\u0002\u0000\t\t  \t\u0000"+
		"\t\n\r\r  \"\"\'\';<>>``||\u0004\u0000\n\n\"\"\'\'``\u0002\u0000\n\n\'"+
		"\'\u0002\u0000\n\n\"\"\u0002\u0000\n\n``\u0003\u0000\n\n\"\"``\u0003\u0000"+
		"\t\n\r\r  \u0093\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0001#\u0001\u0000\u0000\u0000\u0003"+
		"%\u0001\u0000\u0000\u0000\u0005\'\u0001\u0000\u0000\u0000\u0007)\u0001"+
		"\u0000\u0000\u0000\t,\u0001\u0000\u0000\u0000\u000b=\u0001\u0000\u0000"+
		"\u0000\r@\u0001\u0000\u0000\u0000\u000fE\u0001\u0000\u0000\u0000\u0011"+
		"J\u0001\u0000\u0000\u0000\u0013O\u0001\u0000\u0000\u0000\u0015T\u0001"+
		"\u0000\u0000\u0000\u0017Y\u0001\u0000\u0000\u0000\u0019`\u0001\u0000\u0000"+
		"\u0000\u001bb\u0001\u0000\u0000\u0000\u001dl\u0001\u0000\u0000\u0000\u001f"+
		"v\u0001\u0000\u0000\u0000!\u0081\u0001\u0000\u0000\u0000#$\u0005;\u0000"+
		"\u0000$\u0002\u0001\u0000\u0000\u0000%&\u0005<\u0000\u0000&\u0004\u0001"+
		"\u0000\u0000\u0000\'(\u0005>\u0000\u0000(\u0006\u0001\u0000\u0000\u0000"+
		")*\u0005|\u0000\u0000*\b\u0001\u0000\u0000\u0000+-\u0007\u0000\u0000\u0000"+
		",+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000"+
		"\u0000./\u0001\u0000\u0000\u0000/\n\u0001\u0000\u0000\u000001\u0005e\u0000"+
		"\u000012\u0005c\u0000\u000023\u0005h\u0000\u00003>\u0005o\u0000\u0000"+
		"45\u0005l\u0000\u00005>\u0005s\u0000\u000067\u0005g\u0000\u000078\u0005"+
		"r\u0000\u000089\u0005e\u0000\u00009>\u0005p\u0000\u0000:;\u0005c\u0000"+
		"\u0000;<\u0005a\u0000\u0000<>\u0005t\u0000\u0000=0\u0001\u0000\u0000\u0000"+
		"=4\u0001\u0000\u0000\u0000=6\u0001\u0000\u0000\u0000=:\u0001\u0000\u0000"+
		"\u0000>\f\u0001\u0000\u0000\u0000?A\b\u0001\u0000\u0000@?\u0001\u0000"+
		"\u0000\u0000AB\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001"+
		"\u0000\u0000\u0000C\u000e\u0001\u0000\u0000\u0000DF\b\u0002\u0000\u0000"+
		"ED\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000"+
		"\u0000GH\u0001\u0000\u0000\u0000H\u0010\u0001\u0000\u0000\u0000IK\b\u0003"+
		"\u0000\u0000JI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LJ\u0001"+
		"\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000M\u0012\u0001\u0000\u0000"+
		"\u0000NP\b\u0004\u0000\u0000ON\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000R\u0014\u0001"+
		"\u0000\u0000\u0000SU\b\u0005\u0000\u0000TS\u0001\u0000\u0000\u0000UV\u0001"+
		"\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000"+
		"W\u0016\u0001\u0000\u0000\u0000XZ\b\u0006\u0000\u0000YX\u0001\u0000\u0000"+
		"\u0000Z[\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000"+
		"\u0000\u0000\\\u0018\u0001\u0000\u0000\u0000]a\u0003\u001b\r\u0000^a\u0003"+
		"\u001d\u000e\u0000_a\u0003\u001f\u000f\u0000`]\u0001\u0000\u0000\u0000"+
		"`^\u0001\u0000\u0000\u0000`_\u0001\u0000\u0000\u0000a\u001a\u0001\u0000"+
		"\u0000\u0000bg\u0005\'\u0000\u0000cf\u0003\u001b\r\u0000df\u0003\u0011"+
		"\b\u0000ec\u0001\u0000\u0000\u0000ed\u0001\u0000\u0000\u0000fi\u0001\u0000"+
		"\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hj\u0001"+
		"\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000jk\u0005\'\u0000\u0000k\u001c"+
		"\u0001\u0000\u0000\u0000lq\u0005\"\u0000\u0000mp\u0003\u001d\u000e\u0000"+
		"np\u0003\u0013\t\u0000om\u0001\u0000\u0000\u0000on\u0001\u0000\u0000\u0000"+
		"ps\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000"+
		"\u0000rt\u0001\u0000\u0000\u0000sq\u0001\u0000\u0000\u0000tu\u0005\"\u0000"+
		"\u0000u\u001e\u0001\u0000\u0000\u0000v{\u0005`\u0000\u0000wz\u0003\u001f"+
		"\u000f\u0000xz\u0003\u0015\n\u0000yw\u0001\u0000\u0000\u0000yx\u0001\u0000"+
		"\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001"+
		"\u0000\u0000\u0000|~\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000"+
		"~\u007f\u0005`\u0000\u0000\u007f \u0001\u0000\u0000\u0000\u0080\u0082"+
		"\u0007\u0007\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\u0083"+
		"\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084"+
		"\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0086"+
		"\u0006\u0010\u0000\u0000\u0086\"\u0001\u0000\u0000\u0000\u0011\u0000."+
		"=BGLQV[`egoqy{\u0083\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}