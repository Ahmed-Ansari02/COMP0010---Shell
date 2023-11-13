// Generated from /Users/damonsurrao/Library/CloudStorage/OneDrive-Personal/Damon/UCL_University/UCL_YEAR2/SoftwareEngineering/comp0010-shell-python-p15/src/Antlr/ShellGrammar.g4 by ANTLR 4.13.1
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
			"SINGLE_QUOTED", "DOUBLE_QUOTED", "BACK_QUOTED", "WS"
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
		"\u0004\u0000\u000br\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0004\u0004!\b\u0004\u000b\u0004\f\u0004\"\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u00052\b\u0005\u0001\u0006\u0004\u00065\b\u0006\u000b\u0006"+
		"\f\u00066\u0001\u0007\u0001\u0007\u0001\u0007\u0004\u0007<\b\u0007\u000b"+
		"\u0007\f\u0007=\u0005\u0007@\b\u0007\n\u0007\f\u0007C\t\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0004\bJ\b\b\u000b\b\f\bK\u0005\b"+
		"N\b\b\n\b\f\bQ\t\b\u0001\b\u0001\b\u0001\b\u0001\b\u0004\bW\b\b\u000b"+
		"\b\f\bX\u0005\b[\b\b\n\b\f\b^\t\b\u0001\b\u0003\ba\b\b\u0001\t\u0001\t"+
		"\u0005\te\b\t\n\t\f\th\t\t\u0001\t\u0001\t\u0001\n\u0004\nm\b\n\u000b"+
		"\n\f\nn\u0001\n\u0001\n\u0000\u0000\u000b\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0001\u0000\u0006\u0002\u0000\t\t  \t\u0000\t\n\r\r  \"\""+
		"\'\';<>>``||\u0002\u0000\n\n``\u0003\u0000\n\n\"\"``\u0002\u0000\n\n\""+
		"\"\u0003\u0000\t\n\r\r  \u0082\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0001\u0017\u0001"+
		"\u0000\u0000\u0000\u0003\u0019\u0001\u0000\u0000\u0000\u0005\u001b\u0001"+
		"\u0000\u0000\u0000\u0007\u001d\u0001\u0000\u0000\u0000\t \u0001\u0000"+
		"\u0000\u0000\u000b1\u0001\u0000\u0000\u0000\r4\u0001\u0000\u0000\u0000"+
		"\u000f8\u0001\u0000\u0000\u0000\u0011`\u0001\u0000\u0000\u0000\u0013b"+
		"\u0001\u0000\u0000\u0000\u0015l\u0001\u0000\u0000\u0000\u0017\u0018\u0005"+
		";\u0000\u0000\u0018\u0002\u0001\u0000\u0000\u0000\u0019\u001a\u0005<\u0000"+
		"\u0000\u001a\u0004\u0001\u0000\u0000\u0000\u001b\u001c\u0005>\u0000\u0000"+
		"\u001c\u0006\u0001\u0000\u0000\u0000\u001d\u001e\u0005|\u0000\u0000\u001e"+
		"\b\u0001\u0000\u0000\u0000\u001f!\u0007\u0000\u0000\u0000 \u001f\u0001"+
		"\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000\" \u0001\u0000\u0000\u0000"+
		"\"#\u0001\u0000\u0000\u0000#\n\u0001\u0000\u0000\u0000$%\u0005e\u0000"+
		"\u0000%&\u0005c\u0000\u0000&\'\u0005h\u0000\u0000\'2\u0005o\u0000\u0000"+
		"()\u0005l\u0000\u0000)2\u0005s\u0000\u0000*+\u0005g\u0000\u0000+,\u0005"+
		"r\u0000\u0000,-\u0005e\u0000\u0000-2\u0005p\u0000\u0000./\u0005c\u0000"+
		"\u0000/0\u0005a\u0000\u000002\u0005t\u0000\u00001$\u0001\u0000\u0000\u0000"+
		"1(\u0001\u0000\u0000\u00001*\u0001\u0000\u0000\u00001.\u0001\u0000\u0000"+
		"\u00002\f\u0001\u0000\u0000\u000035\b\u0001\u0000\u000043\u0001\u0000"+
		"\u0000\u000056\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000067\u0001"+
		"\u0000\u0000\u00007\u000e\u0001\u0000\u0000\u00008A\u0005\'\u0000\u0000"+
		"9@\u0003\u000f\u0007\u0000:<\b\u0002\u0000\u0000;:\u0001\u0000\u0000\u0000"+
		"<=\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000"+
		"\u0000>@\u0001\u0000\u0000\u0000?9\u0001\u0000\u0000\u0000?;\u0001\u0000"+
		"\u0000\u0000@C\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001"+
		"\u0000\u0000\u0000BD\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000"+
		"DE\u0005\'\u0000\u0000E\u0010\u0001\u0000\u0000\u0000FO\u0005\"\u0000"+
		"\u0000GN\u0003\u0013\t\u0000HJ\b\u0003\u0000\u0000IH\u0001\u0000\u0000"+
		"\u0000JK\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000"+
		"\u0000\u0000LN\u0001\u0000\u0000\u0000MG\u0001\u0000\u0000\u0000MI\u0001"+
		"\u0000\u0000\u0000NQ\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000"+
		"OP\u0001\u0000\u0000\u0000PR\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000Ra\u0005\"\u0000\u0000S\\\u0005\"\u0000\u0000T[\u0003\u0011\b\u0000"+
		"UW\b\u0004\u0000\u0000VU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y[\u0001\u0000\u0000"+
		"\u0000ZT\u0001\u0000\u0000\u0000ZV\u0001\u0000\u0000\u0000[^\u0001\u0000"+
		"\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]_\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000_a\u0005\"\u0000\u0000`F"+
		"\u0001\u0000\u0000\u0000`S\u0001\u0000\u0000\u0000a\u0012\u0001\u0000"+
		"\u0000\u0000bf\u0005`\u0000\u0000ce\b\u0002\u0000\u0000dc\u0001\u0000"+
		"\u0000\u0000eh\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000fg\u0001"+
		"\u0000\u0000\u0000gi\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000"+
		"ij\u0005`\u0000\u0000j\u0014\u0001\u0000\u0000\u0000km\u0007\u0005\u0000"+
		"\u0000lk\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000nl\u0001\u0000"+
		"\u0000\u0000no\u0001\u0000\u0000\u0000op\u0001\u0000\u0000\u0000pq\u0006"+
		"\n\u0000\u0000q\u0016\u0001\u0000\u0000\u0000\u0010\u0000\"16=?AKMOXZ"+
		"\\`fn\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}