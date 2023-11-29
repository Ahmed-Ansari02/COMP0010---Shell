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
		T__0=1, T__1=2, T__2=3, T__3=4, WHITESPACE=5, UNQUOTED=6, SINGLE_QUOTED=7, 
		DOUBLE_QUOTED=8, BACK_QUOTED=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "WHITESPACE", "UNQUOTED", "NOT_QUOTED", 
			"NOT_SINGLE_QUOTED", "NOT_DOUBLE_QUOTED", "NOT_BACK_QUOTED", "NOT_DOUBLE_BACK_QUOTED", 
			"QUOTED", "SINGLE_QUOTED", "DOUBLE_QUOTED", "BACK_QUOTED", "WS"
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
			null, null, null, null, null, "WHITESPACE", "UNQUOTED", "SINGLE_QUOTED", 
			"DOUBLE_QUOTED", "BACK_QUOTED", "WS"
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
		"\u0004\u0000\nv\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0004\u0004+\b"+
		"\u0004\u000b\u0004\f\u0004,\u0001\u0005\u0004\u00050\b\u0005\u000b\u0005"+
		"\f\u00051\u0001\u0006\u0004\u00065\b\u0006\u000b\u0006\f\u00066\u0001"+
		"\u0007\u0004\u0007:\b\u0007\u000b\u0007\f\u0007;\u0001\b\u0004\b?\b\b"+
		"\u000b\b\f\b@\u0001\t\u0004\tD\b\t\u000b\t\f\tE\u0001\n\u0004\nI\b\n\u000b"+
		"\n\f\nJ\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000bP\b\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0005\fU\b\f\n\f\f\fX\t\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0005\r_\b\r\n\r\f\rb\t\r\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0005\u000ei\b\u000e\n\u000e\f\u000el\t\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0004\u000fq\b\u000f\u000b\u000f\f\u000f"+
		"r\u0001\u000f\u0001\u000f\u0000\u0000\u0010\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0000\u000f\u0000\u0011\u0000"+
		"\u0013\u0000\u0015\u0000\u0017\u0000\u0019\u0007\u001b\b\u001d\t\u001f"+
		"\n\u0001\u0000\b\u0002\u0000\t\t  \t\u0000\t\n\r\r  \"\"\'\';<>>``||\u0004"+
		"\u0000\n\n\"\"\'\'``\u0002\u0000\n\n\'\'\u0002\u0000\n\n\"\"\u0002\u0000"+
		"\n\n``\u0003\u0000\n\n\"\"``\u0003\u0000\t\n\r\r  \u007f\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0001!\u0001\u0000\u0000"+
		"\u0000\u0003#\u0001\u0000\u0000\u0000\u0005%\u0001\u0000\u0000\u0000\u0007"+
		"\'\u0001\u0000\u0000\u0000\t*\u0001\u0000\u0000\u0000\u000b/\u0001\u0000"+
		"\u0000\u0000\r4\u0001\u0000\u0000\u0000\u000f9\u0001\u0000\u0000\u0000"+
		"\u0011>\u0001\u0000\u0000\u0000\u0013C\u0001\u0000\u0000\u0000\u0015H"+
		"\u0001\u0000\u0000\u0000\u0017O\u0001\u0000\u0000\u0000\u0019Q\u0001\u0000"+
		"\u0000\u0000\u001b[\u0001\u0000\u0000\u0000\u001de\u0001\u0000\u0000\u0000"+
		"\u001fp\u0001\u0000\u0000\u0000!\"\u0005;\u0000\u0000\"\u0002\u0001\u0000"+
		"\u0000\u0000#$\u0005<\u0000\u0000$\u0004\u0001\u0000\u0000\u0000%&\u0005"+
		">\u0000\u0000&\u0006\u0001\u0000\u0000\u0000\'(\u0005|\u0000\u0000(\b"+
		"\u0001\u0000\u0000\u0000)+\u0007\u0000\u0000\u0000*)\u0001\u0000\u0000"+
		"\u0000+,\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000"+
		"\u0000\u0000-\n\u0001\u0000\u0000\u0000.0\b\u0001\u0000\u0000/.\u0001"+
		"\u0000\u0000\u000001\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u0000"+
		"12\u0001\u0000\u0000\u00002\f\u0001\u0000\u0000\u000035\b\u0002\u0000"+
		"\u000043\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000064\u0001\u0000"+
		"\u0000\u000067\u0001\u0000\u0000\u00007\u000e\u0001\u0000\u0000\u0000"+
		"8:\b\u0003\u0000\u000098\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000"+
		";9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<\u0010\u0001\u0000"+
		"\u0000\u0000=?\b\u0004\u0000\u0000>=\u0001\u0000\u0000\u0000?@\u0001\u0000"+
		"\u0000\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A\u0012"+
		"\u0001\u0000\u0000\u0000BD\b\u0005\u0000\u0000CB\u0001\u0000\u0000\u0000"+
		"DE\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000"+
		"\u0000F\u0014\u0001\u0000\u0000\u0000GI\b\u0006\u0000\u0000HG\u0001\u0000"+
		"\u0000\u0000IJ\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001"+
		"\u0000\u0000\u0000K\u0016\u0001\u0000\u0000\u0000LP\u0003\u0019\f\u0000"+
		"MP\u0003\u001b\r\u0000NP\u0003\u001d\u000e\u0000OL\u0001\u0000\u0000\u0000"+
		"OM\u0001\u0000\u0000\u0000ON\u0001\u0000\u0000\u0000P\u0018\u0001\u0000"+
		"\u0000\u0000QV\u0005\'\u0000\u0000RU\u0003\u0019\f\u0000SU\u0003\u000f"+
		"\u0007\u0000TR\u0001\u0000\u0000\u0000TS\u0001\u0000\u0000\u0000UX\u0001"+
		"\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000"+
		"WY\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000YZ\u0005\'\u0000\u0000"+
		"Z\u001a\u0001\u0000\u0000\u0000[`\u0005\"\u0000\u0000\\_\u0003\u001b\r"+
		"\u0000]_\u0003\u0011\b\u0000^\\\u0001\u0000\u0000\u0000^]\u0001\u0000"+
		"\u0000\u0000_b\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000ac\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000"+
		"cd\u0005\"\u0000\u0000d\u001c\u0001\u0000\u0000\u0000ej\u0005`\u0000\u0000"+
		"fi\u0003\u001d\u000e\u0000gi\u0003\u0013\t\u0000hf\u0001\u0000\u0000\u0000"+
		"hg\u0001\u0000\u0000\u0000il\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000"+
		"\u0000jk\u0001\u0000\u0000\u0000km\u0001\u0000\u0000\u0000lj\u0001\u0000"+
		"\u0000\u0000mn\u0005`\u0000\u0000n\u001e\u0001\u0000\u0000\u0000oq\u0007"+
		"\u0007\u0000\u0000po\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000"+
		"rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0001\u0000\u0000"+
		"\u0000tu\u0006\u000f\u0000\u0000u \u0001\u0000\u0000\u0000\u0010\u0000"+
		",16;@EJOTV^`hjr\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}