// Generated from /Users/damonsurrao/Library/CloudStorage/OneDrive-Personal/Damon/UCL_University/UCL_YEAR2/SoftwareEngineering/comp0010-shell-python-p15/src/Antlr/Expr.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11;
	public static final int
		RULE_command = 0, RULE_pipe = 1, RULE_call = 2, RULE_whitespace = 3, RULE_nonkeyword = 4, 
		RULE_atom = 5, RULE_argument = 6, RULE_redirection = 7, RULE_quoted = 8, 
		RULE_singlequoted = 9, RULE_doublequoted = 10, RULE_doublequotecontent = 11, 
		RULE_backquoted = 12, RULE_unquoted = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "pipe", "call", "whitespace", "nonkeyword", "atom", "argument", 
			"redirection", "quoted", "singlequoted", "doublequoted", "doublequotecontent", 
			"backquoted", "unquoted"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'|'", "'\\t'", "' '", "'\\n'", "'''", "'\"'", "'`'", "'<'", 
			"'>'", "'\\r'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
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
	public static class CommandContext extends ParserRuleContext {
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		return command(0);
	}

	private CommandContext command(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CommandContext _localctx = new CommandContext(_ctx, _parentState);
		CommandContext _prevctx = _localctx;
		int _startState = 0;
		enterRecursionRule(_localctx, 0, RULE_command, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(29);
				pipe(0);
				}
				break;
			case 2:
				{
				setState(30);
				call();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(38);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CommandContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_command);
					setState(33);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(34);
					match(T__0);
					setState(35);
					command(3);
					}
					} 
				}
				setState(40);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipeContext extends ParserRuleContext {
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public PipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipe; }
	}

	public final PipeContext pipe() throws RecognitionException {
		return pipe(0);
	}

	private PipeContext pipe(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PipeContext _localctx = new PipeContext(_ctx, _parentState);
		PipeContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_pipe, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(42);
			call();
			setState(43);
			match(T__1);
			setState(44);
			call();
			}
			_ctx.stop = _input.LT(-1);
			setState(51);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PipeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_pipe);
					setState(46);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(47);
					match(T__1);
					setState(48);
					call();
					}
					} 
				}
				setState(53);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallContext extends ParserRuleContext {
		public List<NonkeywordContext> nonkeyword() {
			return getRuleContexts(NonkeywordContext.class);
		}
		public NonkeywordContext nonkeyword(int i) {
			return getRuleContext(NonkeywordContext.class,i);
		}
		public List<QuotedContext> quoted() {
			return getRuleContexts(QuotedContext.class);
		}
		public QuotedContext quoted(int i) {
			return getRuleContext(QuotedContext.class,i);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_call);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(56);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__2:
					case T__3:
					case T__8:
					case T__9:
					case T__10:
						{
						setState(54);
						nonkeyword();
						}
						break;
					case T__5:
					case T__6:
					case T__7:
						{
						setState(55);
						quoted();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(60);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
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
	public static class WhitespaceContext extends ParserRuleContext {
		public WhitespaceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whitespace; }
	}

	public final WhitespaceContext whitespace() throws RecognitionException {
		WhitespaceContext _localctx = new WhitespaceContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_whitespace);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(62); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(61);
					_la = _input.LA(1);
					if ( !(_la==T__2 || _la==T__3) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(64); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class NonkeywordContext extends ParserRuleContext {
		public NonkeywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nonkeyword; }
	}

	public final NonkeywordContext nonkeyword() throws RecognitionException {
		NonkeywordContext _localctx = new NonkeywordContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_nonkeyword);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			_la = _input.LA(1);
			if ( _la <= 0 || ((((_la) & ~0x3f) == 0 && ((1L << _la) & 486L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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
	public static class AtomContext extends ParserRuleContext {
		public RedirectionContext redirection() {
			return getRuleContext(RedirectionContext.class,0);
		}
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_atom);
		try {
			setState(70);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				redirection();
				}
				break;
			case T__3:
			case T__5:
			case T__6:
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				argument();
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
	public static class ArgumentContext extends ParserRuleContext {
		public List<QuotedContext> quoted() {
			return getRuleContexts(QuotedContext.class);
		}
		public QuotedContext quoted(int i) {
			return getRuleContext(QuotedContext.class,i);
		}
		public List<UnquotedContext> unquoted() {
			return getRuleContexts(UnquotedContext.class);
		}
		public UnquotedContext unquoted(int i) {
			return getRuleContext(UnquotedContext.class,i);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_argument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(74);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__5:
				case T__6:
				case T__7:
					{
					setState(72);
					quoted();
					}
					break;
				case T__3:
					{
					setState(73);
					unquoted();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(76); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 464L) != 0) );
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
	public static class RedirectionContext extends ParserRuleContext {
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public WhitespaceContext whitespace() {
			return getRuleContext(WhitespaceContext.class,0);
		}
		public RedirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_redirection; }
	}

	public final RedirectionContext redirection() throws RecognitionException {
		RedirectionContext _localctx = new RedirectionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_redirection);
		try {
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				match(T__8);
				setState(80);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
				case 1:
					{
					setState(79);
					whitespace();
					}
					break;
				}
				setState(82);
				argument();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				match(T__9);
				setState(85);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(84);
					whitespace();
					}
					break;
				}
				setState(87);
				argument();
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
	public static class QuotedContext extends ParserRuleContext {
		public SinglequotedContext singlequoted() {
			return getRuleContext(SinglequotedContext.class,0);
		}
		public DoublequotedContext doublequoted() {
			return getRuleContext(DoublequotedContext.class,0);
		}
		public BackquotedContext backquoted() {
			return getRuleContext(BackquotedContext.class,0);
		}
		public QuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quoted; }
	}

	public final QuotedContext quoted() throws RecognitionException {
		QuotedContext _localctx = new QuotedContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_quoted);
		try {
			setState(93);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				singlequoted();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				doublequoted();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				backquoted();
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
	public static class SinglequotedContext extends ParserRuleContext {
		public SinglequotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singlequoted; }
	}

	public final SinglequotedContext singlequoted() throws RecognitionException {
		SinglequotedContext _localctx = new SinglequotedContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_singlequoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(T__5);
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3998L) != 0)) {
				{
				{
				setState(96);
				_la = _input.LA(1);
				if ( _la <= 0 || (_la==T__4 || _la==T__5) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(102);
			match(T__5);
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
	public static class DoublequotedContext extends ParserRuleContext {
		public List<BackquotedContext> backquoted() {
			return getRuleContexts(BackquotedContext.class);
		}
		public BackquotedContext backquoted(int i) {
			return getRuleContext(BackquotedContext.class,i);
		}
		public List<DoublequotecontentContext> doublequotecontent() {
			return getRuleContexts(DoublequotecontentContext.class);
		}
		public DoublequotecontentContext doublequotecontent(int i) {
			return getRuleContext(DoublequotecontentContext.class,i);
		}
		public DoublequotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doublequoted; }
	}

	public final DoublequotedContext doublequoted() throws RecognitionException {
		DoublequotedContext _localctx = new DoublequotedContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_doublequoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(T__6);
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3934L) != 0)) {
				{
				setState(107);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__7:
					{
					setState(105);
					backquoted();
					}
					break;
				case T__0:
				case T__1:
				case T__2:
				case T__3:
				case T__5:
				case T__8:
				case T__9:
				case T__10:
					{
					setState(106);
					doublequotecontent();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(111);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(112);
			match(T__6);
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
	public static class DoublequotecontentContext extends ParserRuleContext {
		public DoublequotecontentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doublequotecontent; }
	}

	public final DoublequotecontentContext doublequotecontent() throws RecognitionException {
		DoublequotecontentContext _localctx = new DoublequotecontentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_doublequotecontent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			_la = _input.LA(1);
			if ( _la <= 0 || ((((_la) & ~0x3f) == 0 && ((1L << _la) & 416L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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
	public static class BackquotedContext extends ParserRuleContext {
		public BackquotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_backquoted; }
	}

	public final BackquotedContext backquoted() throws RecognitionException {
		BackquotedContext _localctx = new BackquotedContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_backquoted);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(T__7);
			setState(120);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(117);
					_la = _input.LA(1);
					if ( _la <= 0 || (_la==T__4 || _la==T__5) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(122);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			setState(123);
			match(T__7);
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
	public static class UnquotedContext extends ParserRuleContext {
		public UnquotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unquoted; }
	}

	public final UnquotedContext unquoted() throws RecognitionException {
		UnquotedContext _localctx = new UnquotedContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_unquoted);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(125);
					_la = _input.LA(1);
					if ( _la <= 0 || ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4078L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(128); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 0:
			return command_sempred((CommandContext)_localctx, predIndex);
		case 1:
			return pipe_sempred((PipeContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean command_sempred(CommandContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean pipe_sempred(PipeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000b\u0083\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001\u0000\u0003"+
		"\u0000 \b\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000%\b\u0000"+
		"\n\u0000\f\u0000(\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u00012\b\u0001"+
		"\n\u0001\f\u00015\t\u0001\u0001\u0002\u0001\u0002\u0005\u00029\b\u0002"+
		"\n\u0002\f\u0002<\t\u0002\u0001\u0003\u0004\u0003?\b\u0003\u000b\u0003"+
		"\f\u0003@\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0003\u0005"+
		"G\b\u0005\u0001\u0006\u0001\u0006\u0004\u0006K\b\u0006\u000b\u0006\f\u0006"+
		"L\u0001\u0007\u0001\u0007\u0003\u0007Q\b\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007V\b\u0007\u0001\u0007\u0003\u0007Y\b\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0003\b^\b\b\u0001\t\u0001\t\u0005\tb\b\t\n\t\f\te"+
		"\t\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\nl\b\n\n\n\f\no\t\n"+
		"\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0005\fw\b\f"+
		"\n\f\f\fz\t\f\u0001\f\u0001\f\u0001\r\u0004\r\u007f\b\r\u000b\r\f\r\u0080"+
		"\u0001\r\u0000\u0002\u0000\u0002\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u0000\u0005\u0001\u0000\u0003\u0004"+
		"\u0002\u0000\u0001\u0002\u0005\b\u0001\u0000\u0005\u0006\u0002\u0000\u0005"+
		"\u0005\u0007\b\u0002\u0000\u0001\u0003\u0005\u000b\u0087\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0002)\u0001\u0000\u0000\u0000\u0004:\u0001\u0000\u0000"+
		"\u0000\u0006>\u0001\u0000\u0000\u0000\bB\u0001\u0000\u0000\u0000\nF\u0001"+
		"\u0000\u0000\u0000\fJ\u0001\u0000\u0000\u0000\u000eX\u0001\u0000\u0000"+
		"\u0000\u0010]\u0001\u0000\u0000\u0000\u0012_\u0001\u0000\u0000\u0000\u0014"+
		"h\u0001\u0000\u0000\u0000\u0016r\u0001\u0000\u0000\u0000\u0018t\u0001"+
		"\u0000\u0000\u0000\u001a~\u0001\u0000\u0000\u0000\u001c\u001d\u0006\u0000"+
		"\uffff\uffff\u0000\u001d \u0003\u0002\u0001\u0000\u001e \u0003\u0004\u0002"+
		"\u0000\u001f\u001c\u0001\u0000\u0000\u0000\u001f\u001e\u0001\u0000\u0000"+
		"\u0000 &\u0001\u0000\u0000\u0000!\"\n\u0002\u0000\u0000\"#\u0005\u0001"+
		"\u0000\u0000#%\u0003\u0000\u0000\u0003$!\u0001\u0000\u0000\u0000%(\u0001"+
		"\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000"+
		"\'\u0001\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000)*\u0006\u0001"+
		"\uffff\uffff\u0000*+\u0003\u0004\u0002\u0000+,\u0005\u0002\u0000\u0000"+
		",-\u0003\u0004\u0002\u0000-3\u0001\u0000\u0000\u0000./\n\u0001\u0000\u0000"+
		"/0\u0005\u0002\u0000\u000002\u0003\u0004\u0002\u00001.\u0001\u0000\u0000"+
		"\u000025\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000034\u0001\u0000"+
		"\u0000\u00004\u0003\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u0000"+
		"69\u0003\b\u0004\u000079\u0003\u0010\b\u000086\u0001\u0000\u0000\u0000"+
		"87\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000"+
		"\u0000:;\u0001\u0000\u0000\u0000;\u0005\u0001\u0000\u0000\u0000<:\u0001"+
		"\u0000\u0000\u0000=?\u0007\u0000\u0000\u0000>=\u0001\u0000\u0000\u0000"+
		"?@\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000"+
		"\u0000A\u0007\u0001\u0000\u0000\u0000BC\b\u0001\u0000\u0000C\t\u0001\u0000"+
		"\u0000\u0000DG\u0003\u000e\u0007\u0000EG\u0003\f\u0006\u0000FD\u0001\u0000"+
		"\u0000\u0000FE\u0001\u0000\u0000\u0000G\u000b\u0001\u0000\u0000\u0000"+
		"HK\u0003\u0010\b\u0000IK\u0003\u001a\r\u0000JH\u0001\u0000\u0000\u0000"+
		"JI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000M\r\u0001\u0000\u0000\u0000NP\u0005\t"+
		"\u0000\u0000OQ\u0003\u0006\u0003\u0000PO\u0001\u0000\u0000\u0000PQ\u0001"+
		"\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RY\u0003\f\u0006\u0000SU\u0005"+
		"\n\u0000\u0000TV\u0003\u0006\u0003\u0000UT\u0001\u0000\u0000\u0000UV\u0001"+
		"\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WY\u0003\f\u0006\u0000XN\u0001"+
		"\u0000\u0000\u0000XS\u0001\u0000\u0000\u0000Y\u000f\u0001\u0000\u0000"+
		"\u0000Z^\u0003\u0012\t\u0000[^\u0003\u0014\n\u0000\\^\u0003\u0018\f\u0000"+
		"]Z\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]\\\u0001\u0000\u0000"+
		"\u0000^\u0011\u0001\u0000\u0000\u0000_c\u0005\u0006\u0000\u0000`b\b\u0002"+
		"\u0000\u0000a`\u0001\u0000\u0000\u0000be\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000df\u0001\u0000\u0000\u0000"+
		"ec\u0001\u0000\u0000\u0000fg\u0005\u0006\u0000\u0000g\u0013\u0001\u0000"+
		"\u0000\u0000hm\u0005\u0007\u0000\u0000il\u0003\u0018\f\u0000jl\u0003\u0016"+
		"\u000b\u0000ki\u0001\u0000\u0000\u0000kj\u0001\u0000\u0000\u0000lo\u0001"+
		"\u0000\u0000\u0000mk\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000"+
		"np\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000pq\u0005\u0007\u0000"+
		"\u0000q\u0015\u0001\u0000\u0000\u0000rs\b\u0003\u0000\u0000s\u0017\u0001"+
		"\u0000\u0000\u0000tx\u0005\b\u0000\u0000uw\b\u0002\u0000\u0000vu\u0001"+
		"\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000"+
		"xy\u0001\u0000\u0000\u0000y{\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000"+
		"\u0000{|\u0005\b\u0000\u0000|\u0019\u0001\u0000\u0000\u0000}\u007f\b\u0004"+
		"\u0000\u0000~}\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000"+
		"\u0080~\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081"+
		"\u001b\u0001\u0000\u0000\u0000\u0012\u001f&38:@FJLPUX]ckmx\u0080";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}