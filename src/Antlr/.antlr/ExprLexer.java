// Generated from c:/Users/ayman/OneDrive/Documents/Comp10Project/comp0010-shell-python-p15/src/Antlr/Expr.g4 by ANTLR 4.13.1
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
		OPERATOR=1, CMD=2, UNQUOTED_STRING=3, FIlE=4, STRING=5, WS=6;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OPERATOR", "CMD", "UNQUOTED_STRING", "FIlE", "STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OPERATOR", "CMD", "UNQUOTED_STRING", "FIlE", "STRING", "WS"
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
		"\u0004\u0000\u0006@\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\u001f\b\u0001\u0001\u0002\u0004\u0002"+
		"\"\b\u0002\u000b\u0002\f\u0002#\u0001\u0003\u0004\u0003\'\b\u0003\u000b"+
		"\u0003\f\u0003(\u0001\u0003\u0001\u0003\u0004\u0003-\b\u0003\u000b\u0003"+
		"\f\u0003.\u0001\u0004\u0001\u0004\u0005\u00043\b\u0004\n\u0004\f\u0004"+
		"6\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0004\u0005;\b\u0005\u000b"+
		"\u0005\f\u0005<\u0001\u0005\u0001\u0005\u0000\u0000\u0006\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\u0001\u0000\u0004"+
		"\u0003\u0000;;>>||\u0004\u000009AZ__az\u0001\u0000\"\"\u0003\u0000\t\n"+
		"\r\r  H\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0001\r\u0001\u0000\u0000\u0000\u0003\u001e\u0001\u0000\u0000\u0000\u0005"+
		"!\u0001\u0000\u0000\u0000\u0007&\u0001\u0000\u0000\u0000\t0\u0001\u0000"+
		"\u0000\u0000\u000b:\u0001\u0000\u0000\u0000\r\u000e\u0007\u0000\u0000"+
		"\u0000\u000e\u0002\u0001\u0000\u0000\u0000\u000f\u0010\u0005e\u0000\u0000"+
		"\u0010\u0011\u0005c\u0000\u0000\u0011\u0012\u0005h\u0000\u0000\u0012\u001f"+
		"\u0005o\u0000\u0000\u0013\u0014\u0005l\u0000\u0000\u0014\u001f\u0005s"+
		"\u0000\u0000\u0015\u0016\u0005g\u0000\u0000\u0016\u0017\u0005r\u0000\u0000"+
		"\u0017\u0018\u0005e\u0000\u0000\u0018\u001f\u0005p\u0000\u0000\u0019\u001a"+
		"\u0005c\u0000\u0000\u001a\u001b\u0005a\u0000\u0000\u001b\u001f\u0005t"+
		"\u0000\u0000\u001c\u001d\u0005c\u0000\u0000\u001d\u001f\u0005d\u0000\u0000"+
		"\u001e\u000f\u0001\u0000\u0000\u0000\u001e\u0013\u0001\u0000\u0000\u0000"+
		"\u001e\u0015\u0001\u0000\u0000\u0000\u001e\u0019\u0001\u0000\u0000\u0000"+
		"\u001e\u001c\u0001\u0000\u0000\u0000\u001f\u0004\u0001\u0000\u0000\u0000"+
		" \"\u0007\u0001\u0000\u0000! \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000"+
		"\u0000#!\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$\u0006\u0001"+
		"\u0000\u0000\u0000%\'\u0007\u0001\u0000\u0000&%\u0001\u0000\u0000\u0000"+
		"\'(\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000"+
		"\u0000)*\u0001\u0000\u0000\u0000*,\u0005.\u0000\u0000+-\u0007\u0001\u0000"+
		"\u0000,+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000.,\u0001\u0000"+
		"\u0000\u0000./\u0001\u0000\u0000\u0000/\b\u0001\u0000\u0000\u000004\u0005"+
		"\"\u0000\u000013\b\u0002\u0000\u000021\u0001\u0000\u0000\u000036\u0001"+
		"\u0000\u0000\u000042\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u0000"+
		"57\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000078\u0005\"\u0000\u0000"+
		"8\n\u0001\u0000\u0000\u00009;\u0007\u0003\u0000\u0000:9\u0001\u0000\u0000"+
		"\u0000;<\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000<=\u0001\u0000"+
		"\u0000\u0000=>\u0001\u0000\u0000\u0000>?\u0006\u0005\u0000\u0000?\f\u0001"+
		"\u0000\u0000\u0000\u0007\u0000\u001e#(.4<\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}