// Generated from c:/Users/vinii/OneDrive/Desktop/Compilador/Puby.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PubyParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, IF=5, ELSIF=6, ELSE=7, END=8, WHILE=9, 
		FOR=10, IN=11, DO=12, PUTS=13, GETS=14, NOT=15, AND_WORD=16, OR_WORD=17, 
		AND_SYM=18, OR_SYM=19, OP_INC=20, OP_DEC=21, OP_ADD=22, OP_MUL=23, OP_REL=24, 
		OP_NOT=25, RANGE=26, ID=27, NUM=28, STRING=29, WS=30;
	public static final int
		RULE_programa = 0, RULE_comando = 1, RULE_escrita = 2, RULE_leitura = 3, 
		RULE_atribuicao = 4, RULE_condicional = 5, RULE_corpo_if = 6, RULE_enquanto = 7, 
		RULE_laco_para = 8, RULE_intervalo = 9, RULE_incremento = 10, RULE_condicao = 11, 
		RULE_expressao = 12, RULE_logico_baixo = 13, RULE_logico_baixo_suf = 14, 
		RULE_not_baixo = 15, RULE_logico_alto = 16, RULE_logico_alto_suf = 17, 
		RULE_rel = 18, RULE_soma = 19, RULE_mult = 20, RULE_unario = 21, RULE_primario = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "comando", "escrita", "leitura", "atribuicao", "condicional", 
			"corpo_if", "enquanto", "laco_para", "intervalo", "incremento", "condicao", 
			"expressao", "logico_baixo", "logico_baixo_suf", "not_baixo", "logico_alto", 
			"logico_alto_suf", "rel", "soma", "mult", "unario", "primario"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", "'='", "'('", "')'", "'if'", "'elsif'", "'else'", "'end'", 
			"'while'", "'for'", "'in'", "'do'", "'puts'", "'gets'", "'not'", "'and'", 
			"'or'", "'&&'", "'||'", "'++'", "'--'", null, null, null, "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "IF", "ELSIF", "ELSE", "END", "WHILE", 
			"FOR", "IN", "DO", "PUTS", "GETS", "NOT", "AND_WORD", "OR_WORD", "AND_SYM", 
			"OR_SYM", "OP_INC", "OP_DEC", "OP_ADD", "OP_MUL", "OP_REL", "OP_NOT", 
			"RANGE", "ID", "NUM", "STRING", "WS"
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
	public String getGrammarFileName() { return "Puby.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PubyParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PubyParser.EOF, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134227488L) != 0)) {
				{
				{
				setState(46);
				comando();
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			match(EOF);
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
	public static class ComandoContext extends ParserRuleContext {
		public EscritaContext escrita() {
			return getRuleContext(EscritaContext.class,0);
		}
		public LeituraContext leitura() {
			return getRuleContext(LeituraContext.class,0);
		}
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public EnquantoContext enquanto() {
			return getRuleContext(EnquantoContext.class,0);
		}
		public Laco_paraContext laco_para() {
			return getRuleContext(Laco_paraContext.class,0);
		}
		public IncrementoContext incremento() {
			return getRuleContext(IncrementoContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_comando);
		try {
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				escrita();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				leitura();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				atribuicao();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(57);
				condicional();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(58);
				enquanto();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(59);
				laco_para();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(60);
				incremento();
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
	public static class EscritaContext extends ParserRuleContext {
		public TerminalNode PUTS() { return getToken(PubyParser.PUTS, 0); }
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public EscritaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escrita; }
	}

	public final EscritaContext escrita() throws RecognitionException {
		EscritaContext _localctx = new EscritaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_escrita);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(PUTS);
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(64);
				expressao();
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__0) {
					{
					{
					setState(65);
					match(T__0);
					setState(66);
					expressao();
					}
					}
					setState(71);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
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
	public static class LeituraContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PubyParser.ID, 0); }
		public TerminalNode GETS() { return getToken(PubyParser.GETS, 0); }
		public LeituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leitura; }
	}

	public final LeituraContext leitura() throws RecognitionException {
		LeituraContext _localctx = new LeituraContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_leitura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(ID);
			setState(75);
			match(T__1);
			setState(76);
			match(GETS);
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
	public static class AtribuicaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PubyParser.ID, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(ID);
			setState(79);
			match(T__1);
			setState(80);
			expressao();
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
	public static class CondicionalContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(PubyParser.IF, 0); }
		public List<CondicaoContext> condicao() {
			return getRuleContexts(CondicaoContext.class);
		}
		public CondicaoContext condicao(int i) {
			return getRuleContext(CondicaoContext.class,i);
		}
		public List<Corpo_ifContext> corpo_if() {
			return getRuleContexts(Corpo_ifContext.class);
		}
		public Corpo_ifContext corpo_if(int i) {
			return getRuleContext(Corpo_ifContext.class,i);
		}
		public TerminalNode END() { return getToken(PubyParser.END, 0); }
		public List<TerminalNode> ELSIF() { return getTokens(PubyParser.ELSIF); }
		public TerminalNode ELSIF(int i) {
			return getToken(PubyParser.ELSIF, i);
		}
		public TerminalNode ELSE() { return getToken(PubyParser.ELSE, 0); }
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_condicional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(IF);
			setState(83);
			condicao();
			setState(84);
			corpo_if();
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSIF) {
				{
				{
				setState(85);
				match(ELSIF);
				setState(86);
				condicao();
				setState(87);
				corpo_if();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(94);
				match(ELSE);
				setState(95);
				corpo_if();
				}
			}

			setState(98);
			match(END);
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
	public static class Corpo_ifContext extends ParserRuleContext {
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public Corpo_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_corpo_if; }
	}

	public final Corpo_ifContext corpo_if() throws RecognitionException {
		Corpo_ifContext _localctx = new Corpo_ifContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_corpo_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134227488L) != 0)) {
				{
				{
				setState(100);
				comando();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class EnquantoContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(PubyParser.WHILE, 0); }
		public CondicaoContext condicao() {
			return getRuleContext(CondicaoContext.class,0);
		}
		public TerminalNode END() { return getToken(PubyParser.END, 0); }
		public TerminalNode DO() { return getToken(PubyParser.DO, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public EnquantoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enquanto; }
	}

	public final EnquantoContext enquanto() throws RecognitionException {
		EnquantoContext _localctx = new EnquantoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_enquanto);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(WHILE);
			setState(107);
			condicao();
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DO) {
				{
				setState(108);
				match(DO);
				}
			}

			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134227488L) != 0)) {
				{
				{
				setState(111);
				comando();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			match(END);
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
	public static class Laco_paraContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(PubyParser.FOR, 0); }
		public TerminalNode ID() { return getToken(PubyParser.ID, 0); }
		public TerminalNode IN() { return getToken(PubyParser.IN, 0); }
		public IntervaloContext intervalo() {
			return getRuleContext(IntervaloContext.class,0);
		}
		public TerminalNode END() { return getToken(PubyParser.END, 0); }
		public TerminalNode DO() { return getToken(PubyParser.DO, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public Laco_paraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_laco_para; }
	}

	public final Laco_paraContext laco_para() throws RecognitionException {
		Laco_paraContext _localctx = new Laco_paraContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_laco_para);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(FOR);
			setState(120);
			match(ID);
			setState(121);
			match(IN);
			setState(122);
			intervalo();
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DO) {
				{
				setState(123);
				match(DO);
				}
			}

			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134227488L) != 0)) {
				{
				{
				setState(126);
				comando();
				}
				}
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(132);
			match(END);
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
	public static class IntervaloContext extends ParserRuleContext {
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public TerminalNode RANGE() { return getToken(PubyParser.RANGE, 0); }
		public IntervaloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intervalo; }
	}

	public final IntervaloContext intervalo() throws RecognitionException {
		IntervaloContext _localctx = new IntervaloContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_intervalo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			expressao();
			setState(135);
			match(RANGE);
			setState(136);
			expressao();
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
	public static class IncrementoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PubyParser.ID, 0); }
		public TerminalNode OP_INC() { return getToken(PubyParser.OP_INC, 0); }
		public TerminalNode OP_DEC() { return getToken(PubyParser.OP_DEC, 0); }
		public IncrementoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incremento; }
	}

	public final IncrementoContext incremento() throws RecognitionException {
		IncrementoContext _localctx = new IncrementoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_incremento);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(ID);
			setState(139);
			_la = _input.LA(1);
			if ( !(_la==OP_INC || _la==OP_DEC) ) {
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
	public static class CondicaoContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public CondicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicao; }
	}

	public final CondicaoContext condicao() throws RecognitionException {
		CondicaoContext _localctx = new CondicaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			expressao();
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
	public static class ExpressaoContext extends ParserRuleContext {
		public Logico_baixoContext logico_baixo() {
			return getRuleContext(Logico_baixoContext.class,0);
		}
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expressao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			logico_baixo();
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
	public static class Logico_baixoContext extends ParserRuleContext {
		public Not_baixoContext not_baixo() {
			return getRuleContext(Not_baixoContext.class,0);
		}
		public Logico_baixo_sufContext logico_baixo_suf() {
			return getRuleContext(Logico_baixo_sufContext.class,0);
		}
		public Logico_baixoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logico_baixo; }
	}

	public final Logico_baixoContext logico_baixo() throws RecognitionException {
		Logico_baixoContext _localctx = new Logico_baixoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_logico_baixo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			not_baixo();
			setState(146);
			logico_baixo_suf();
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
	public static class Logico_baixo_sufContext extends ParserRuleContext {
		public TerminalNode AND_WORD() { return getToken(PubyParser.AND_WORD, 0); }
		public Not_baixoContext not_baixo() {
			return getRuleContext(Not_baixoContext.class,0);
		}
		public Logico_baixo_sufContext logico_baixo_suf() {
			return getRuleContext(Logico_baixo_sufContext.class,0);
		}
		public TerminalNode OR_WORD() { return getToken(PubyParser.OR_WORD, 0); }
		public Logico_baixo_sufContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logico_baixo_suf; }
	}

	public final Logico_baixo_sufContext logico_baixo_suf() throws RecognitionException {
		Logico_baixo_sufContext _localctx = new Logico_baixo_sufContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_logico_baixo_suf);
		try {
			setState(157);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND_WORD:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				match(AND_WORD);
				setState(149);
				not_baixo();
				setState(150);
				logico_baixo_suf();
				}
				break;
			case OR_WORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				match(OR_WORD);
				setState(153);
				not_baixo();
				setState(154);
				logico_baixo_suf();
				}
				break;
			case EOF:
			case T__0:
			case T__3:
			case IF:
			case ELSIF:
			case ELSE:
			case END:
			case WHILE:
			case FOR:
			case DO:
			case PUTS:
			case RANGE:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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
	public static class Not_baixoContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(PubyParser.NOT, 0); }
		public Not_baixoContext not_baixo() {
			return getRuleContext(Not_baixoContext.class,0);
		}
		public Logico_altoContext logico_alto() {
			return getRuleContext(Logico_altoContext.class,0);
		}
		public Not_baixoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_not_baixo; }
	}

	public final Not_baixoContext not_baixo() throws RecognitionException {
		Not_baixoContext _localctx = new Not_baixoContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_not_baixo);
		try {
			setState(162);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				match(NOT);
				setState(160);
				not_baixo();
				}
				break;
			case T__2:
			case OP_ADD:
			case OP_NOT:
			case ID:
			case NUM:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(161);
				logico_alto();
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
	public static class Logico_altoContext extends ParserRuleContext {
		public RelContext rel() {
			return getRuleContext(RelContext.class,0);
		}
		public Logico_alto_sufContext logico_alto_suf() {
			return getRuleContext(Logico_alto_sufContext.class,0);
		}
		public Logico_altoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logico_alto; }
	}

	public final Logico_altoContext logico_alto() throws RecognitionException {
		Logico_altoContext _localctx = new Logico_altoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_logico_alto);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			rel();
			setState(165);
			logico_alto_suf();
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
	public static class Logico_alto_sufContext extends ParserRuleContext {
		public TerminalNode AND_SYM() { return getToken(PubyParser.AND_SYM, 0); }
		public RelContext rel() {
			return getRuleContext(RelContext.class,0);
		}
		public Logico_alto_sufContext logico_alto_suf() {
			return getRuleContext(Logico_alto_sufContext.class,0);
		}
		public TerminalNode OR_SYM() { return getToken(PubyParser.OR_SYM, 0); }
		public Logico_alto_sufContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logico_alto_suf; }
	}

	public final Logico_alto_sufContext logico_alto_suf() throws RecognitionException {
		Logico_alto_sufContext _localctx = new Logico_alto_sufContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_logico_alto_suf);
		try {
			setState(176);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND_SYM:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(AND_SYM);
				setState(168);
				rel();
				setState(169);
				logico_alto_suf();
				}
				break;
			case OR_SYM:
				enterOuterAlt(_localctx, 2);
				{
				setState(171);
				match(OR_SYM);
				setState(172);
				rel();
				setState(173);
				logico_alto_suf();
				}
				break;
			case EOF:
			case T__0:
			case T__3:
			case IF:
			case ELSIF:
			case ELSE:
			case END:
			case WHILE:
			case FOR:
			case DO:
			case PUTS:
			case AND_WORD:
			case OR_WORD:
			case RANGE:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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
	public static class RelContext extends ParserRuleContext {
		public List<SomaContext> soma() {
			return getRuleContexts(SomaContext.class);
		}
		public SomaContext soma(int i) {
			return getRuleContext(SomaContext.class,i);
		}
		public List<TerminalNode> OP_REL() { return getTokens(PubyParser.OP_REL); }
		public TerminalNode OP_REL(int i) {
			return getToken(PubyParser.OP_REL, i);
		}
		public RelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel; }
	}

	public final RelContext rel() throws RecognitionException {
		RelContext _localctx = new RelContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_rel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			soma();
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_REL) {
				{
				{
				setState(179);
				match(OP_REL);
				setState(180);
				soma();
				}
				}
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class SomaContext extends ParserRuleContext {
		public List<MultContext> mult() {
			return getRuleContexts(MultContext.class);
		}
		public MultContext mult(int i) {
			return getRuleContext(MultContext.class,i);
		}
		public List<TerminalNode> OP_ADD() { return getTokens(PubyParser.OP_ADD); }
		public TerminalNode OP_ADD(int i) {
			return getToken(PubyParser.OP_ADD, i);
		}
		public SomaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_soma; }
	}

	public final SomaContext soma() throws RecognitionException {
		SomaContext _localctx = new SomaContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_soma);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			mult();
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_ADD) {
				{
				{
				setState(187);
				match(OP_ADD);
				setState(188);
				mult();
				}
				}
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class MultContext extends ParserRuleContext {
		public List<UnarioContext> unario() {
			return getRuleContexts(UnarioContext.class);
		}
		public UnarioContext unario(int i) {
			return getRuleContext(UnarioContext.class,i);
		}
		public List<TerminalNode> OP_MUL() { return getTokens(PubyParser.OP_MUL); }
		public TerminalNode OP_MUL(int i) {
			return getToken(PubyParser.OP_MUL, i);
		}
		public MultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mult; }
	}

	public final MultContext mult() throws RecognitionException {
		MultContext _localctx = new MultContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_mult);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			unario();
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_MUL) {
				{
				{
				setState(195);
				match(OP_MUL);
				setState(196);
				unario();
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class UnarioContext extends ParserRuleContext {
		public TerminalNode OP_NOT() { return getToken(PubyParser.OP_NOT, 0); }
		public UnarioContext unario() {
			return getRuleContext(UnarioContext.class,0);
		}
		public TerminalNode OP_ADD() { return getToken(PubyParser.OP_ADD, 0); }
		public PrimarioContext primario() {
			return getRuleContext(PrimarioContext.class,0);
		}
		public UnarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unario; }
	}

	public final UnarioContext unario() throws RecognitionException {
		UnarioContext _localctx = new UnarioContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_unario);
		try {
			setState(207);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OP_NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				match(OP_NOT);
				setState(203);
				unario();
				}
				break;
			case OP_ADD:
				enterOuterAlt(_localctx, 2);
				{
				setState(204);
				match(OP_ADD);
				setState(205);
				unario();
				}
				break;
			case T__2:
			case ID:
			case NUM:
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(206);
				primario();
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
	public static class PrimarioContext extends ParserRuleContext {
		public TerminalNode NUM() { return getToken(PubyParser.NUM, 0); }
		public TerminalNode STRING() { return getToken(PubyParser.STRING, 0); }
		public TerminalNode ID() { return getToken(PubyParser.ID, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public PrimarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primario; }
	}

	public final PrimarioContext primario() throws RecognitionException {
		PrimarioContext _localctx = new PrimarioContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_primario);
		try {
			setState(216);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				match(NUM);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(211);
				match(ID);
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 4);
				{
				setState(212);
				match(T__2);
				setState(213);
				expressao();
				setState(214);
				match(T__3);
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

	public static final String _serializedATN =
		"\u0004\u0001\u001e\u00db\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0005\u00000\b\u0000\n\u0000"+
		"\f\u00003\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001>\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002D\b"+
		"\u0002\n\u0002\f\u0002G\t\u0002\u0003\u0002I\b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0005\u0005Z\b\u0005\n\u0005\f\u0005]\t\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u0005a\b\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0005\u0006f\b\u0006\n\u0006\f\u0006i\t\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007n\b\u0007\u0001\u0007\u0005\u0007q\b\u0007"+
		"\n\u0007\f\u0007t\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0003\b}\b\b\u0001\b\u0005\b\u0080\b\b\n\b\f\b\u0083"+
		"\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u009e\b\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u00a3\b\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00b1\b\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u00b6\b\u0012\n\u0012\f\u0012"+
		"\u00b9\t\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013\u00be\b"+
		"\u0013\n\u0013\f\u0013\u00c1\t\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0005\u0014\u00c6\b\u0014\n\u0014\f\u0014\u00c9\t\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00d0\b\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0003\u0016\u00d9\b\u0016\u0001\u0016\u0000\u0000\u0017\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*,\u0000\u0001\u0001\u0000\u0014\u0015\u00e0\u00001\u0001\u0000"+
		"\u0000\u0000\u0002=\u0001\u0000\u0000\u0000\u0004?\u0001\u0000\u0000\u0000"+
		"\u0006J\u0001\u0000\u0000\u0000\bN\u0001\u0000\u0000\u0000\nR\u0001\u0000"+
		"\u0000\u0000\fg\u0001\u0000\u0000\u0000\u000ej\u0001\u0000\u0000\u0000"+
		"\u0010w\u0001\u0000\u0000\u0000\u0012\u0086\u0001\u0000\u0000\u0000\u0014"+
		"\u008a\u0001\u0000\u0000\u0000\u0016\u008d\u0001\u0000\u0000\u0000\u0018"+
		"\u008f\u0001\u0000\u0000\u0000\u001a\u0091\u0001\u0000\u0000\u0000\u001c"+
		"\u009d\u0001\u0000\u0000\u0000\u001e\u00a2\u0001\u0000\u0000\u0000 \u00a4"+
		"\u0001\u0000\u0000\u0000\"\u00b0\u0001\u0000\u0000\u0000$\u00b2\u0001"+
		"\u0000\u0000\u0000&\u00ba\u0001\u0000\u0000\u0000(\u00c2\u0001\u0000\u0000"+
		"\u0000*\u00cf\u0001\u0000\u0000\u0000,\u00d8\u0001\u0000\u0000\u0000."+
		"0\u0003\u0002\u0001\u0000/.\u0001\u0000\u0000\u000003\u0001\u0000\u0000"+
		"\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u000024\u0001\u0000"+
		"\u0000\u000031\u0001\u0000\u0000\u000045\u0005\u0000\u0000\u00015\u0001"+
		"\u0001\u0000\u0000\u00006>\u0003\u0004\u0002\u00007>\u0003\u0006\u0003"+
		"\u00008>\u0003\b\u0004\u00009>\u0003\n\u0005\u0000:>\u0003\u000e\u0007"+
		"\u0000;>\u0003\u0010\b\u0000<>\u0003\u0014\n\u0000=6\u0001\u0000\u0000"+
		"\u0000=7\u0001\u0000\u0000\u0000=8\u0001\u0000\u0000\u0000=9\u0001\u0000"+
		"\u0000\u0000=:\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=<\u0001"+
		"\u0000\u0000\u0000>\u0003\u0001\u0000\u0000\u0000?H\u0005\r\u0000\u0000"+
		"@E\u0003\u0018\f\u0000AB\u0005\u0001\u0000\u0000BD\u0003\u0018\f\u0000"+
		"CA\u0001\u0000\u0000\u0000DG\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000"+
		"\u0000EF\u0001\u0000\u0000\u0000FI\u0001\u0000\u0000\u0000GE\u0001\u0000"+
		"\u0000\u0000H@\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000I\u0005"+
		"\u0001\u0000\u0000\u0000JK\u0005\u001b\u0000\u0000KL\u0005\u0002\u0000"+
		"\u0000LM\u0005\u000e\u0000\u0000M\u0007\u0001\u0000\u0000\u0000NO\u0005"+
		"\u001b\u0000\u0000OP\u0005\u0002\u0000\u0000PQ\u0003\u0018\f\u0000Q\t"+
		"\u0001\u0000\u0000\u0000RS\u0005\u0005\u0000\u0000ST\u0003\u0016\u000b"+
		"\u0000T[\u0003\f\u0006\u0000UV\u0005\u0006\u0000\u0000VW\u0003\u0016\u000b"+
		"\u0000WX\u0003\f\u0006\u0000XZ\u0001\u0000\u0000\u0000YU\u0001\u0000\u0000"+
		"\u0000Z]\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000"+
		"\u0000\u0000\\`\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000^_\u0005"+
		"\u0007\u0000\u0000_a\u0003\f\u0006\u0000`^\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000bc\u0005\b\u0000\u0000c\u000b"+
		"\u0001\u0000\u0000\u0000df\u0003\u0002\u0001\u0000ed\u0001\u0000\u0000"+
		"\u0000fi\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000"+
		"\u0000\u0000h\r\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000jk\u0005"+
		"\t\u0000\u0000km\u0003\u0016\u000b\u0000ln\u0005\f\u0000\u0000ml\u0001"+
		"\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000nr\u0001\u0000\u0000\u0000"+
		"oq\u0003\u0002\u0001\u0000po\u0001\u0000\u0000\u0000qt\u0001\u0000\u0000"+
		"\u0000rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000su\u0001\u0000"+
		"\u0000\u0000tr\u0001\u0000\u0000\u0000uv\u0005\b\u0000\u0000v\u000f\u0001"+
		"\u0000\u0000\u0000wx\u0005\n\u0000\u0000xy\u0005\u001b\u0000\u0000yz\u0005"+
		"\u000b\u0000\u0000z|\u0003\u0012\t\u0000{}\u0005\f\u0000\u0000|{\u0001"+
		"\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\u0081\u0001\u0000\u0000"+
		"\u0000~\u0080\u0003\u0002\u0001\u0000\u007f~\u0001\u0000\u0000\u0000\u0080"+
		"\u0083\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0001\u0000\u0000\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083"+
		"\u0081\u0001\u0000\u0000\u0000\u0084\u0085\u0005\b\u0000\u0000\u0085\u0011"+
		"\u0001\u0000\u0000\u0000\u0086\u0087\u0003\u0018\f\u0000\u0087\u0088\u0005"+
		"\u001a\u0000\u0000\u0088\u0089\u0003\u0018\f\u0000\u0089\u0013\u0001\u0000"+
		"\u0000\u0000\u008a\u008b\u0005\u001b\u0000\u0000\u008b\u008c\u0007\u0000"+
		"\u0000\u0000\u008c\u0015\u0001\u0000\u0000\u0000\u008d\u008e\u0003\u0018"+
		"\f\u0000\u008e\u0017\u0001\u0000\u0000\u0000\u008f\u0090\u0003\u001a\r"+
		"\u0000\u0090\u0019\u0001\u0000\u0000\u0000\u0091\u0092\u0003\u001e\u000f"+
		"\u0000\u0092\u0093\u0003\u001c\u000e\u0000\u0093\u001b\u0001\u0000\u0000"+
		"\u0000\u0094\u0095\u0005\u0010\u0000\u0000\u0095\u0096\u0003\u001e\u000f"+
		"\u0000\u0096\u0097\u0003\u001c\u000e\u0000\u0097\u009e\u0001\u0000\u0000"+
		"\u0000\u0098\u0099\u0005\u0011\u0000\u0000\u0099\u009a\u0003\u001e\u000f"+
		"\u0000\u009a\u009b\u0003\u001c\u000e\u0000\u009b\u009e\u0001\u0000\u0000"+
		"\u0000\u009c\u009e\u0001\u0000\u0000\u0000\u009d\u0094\u0001\u0000\u0000"+
		"\u0000\u009d\u0098\u0001\u0000\u0000\u0000\u009d\u009c\u0001\u0000\u0000"+
		"\u0000\u009e\u001d\u0001\u0000\u0000\u0000\u009f\u00a0\u0005\u000f\u0000"+
		"\u0000\u00a0\u00a3\u0003\u001e\u000f\u0000\u00a1\u00a3\u0003 \u0010\u0000"+
		"\u00a2\u009f\u0001\u0000\u0000\u0000\u00a2\u00a1\u0001\u0000\u0000\u0000"+
		"\u00a3\u001f\u0001\u0000\u0000\u0000\u00a4\u00a5\u0003$\u0012\u0000\u00a5"+
		"\u00a6\u0003\"\u0011\u0000\u00a6!\u0001\u0000\u0000\u0000\u00a7\u00a8"+
		"\u0005\u0012\u0000\u0000\u00a8\u00a9\u0003$\u0012\u0000\u00a9\u00aa\u0003"+
		"\"\u0011\u0000\u00aa\u00b1\u0001\u0000\u0000\u0000\u00ab\u00ac\u0005\u0013"+
		"\u0000\u0000\u00ac\u00ad\u0003$\u0012\u0000\u00ad\u00ae\u0003\"\u0011"+
		"\u0000\u00ae\u00b1\u0001\u0000\u0000\u0000\u00af\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b0\u00a7\u0001\u0000\u0000\u0000\u00b0\u00ab\u0001\u0000\u0000"+
		"\u0000\u00b0\u00af\u0001\u0000\u0000\u0000\u00b1#\u0001\u0000\u0000\u0000"+
		"\u00b2\u00b7\u0003&\u0013\u0000\u00b3\u00b4\u0005\u0018\u0000\u0000\u00b4"+
		"\u00b6\u0003&\u0013\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b6\u00b9"+
		"\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b7\u00b8"+
		"\u0001\u0000\u0000\u0000\u00b8%\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001"+
		"\u0000\u0000\u0000\u00ba\u00bf\u0003(\u0014\u0000\u00bb\u00bc\u0005\u0016"+
		"\u0000\u0000\u00bc\u00be\u0003(\u0014\u0000\u00bd\u00bb\u0001\u0000\u0000"+
		"\u0000\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0\'\u0001\u0000\u0000\u0000"+
		"\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2\u00c7\u0003*\u0015\u0000\u00c3"+
		"\u00c4\u0005\u0017\u0000\u0000\u00c4\u00c6\u0003*\u0015\u0000\u00c5\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000\u0000\u0000\u00c8)\u0001"+
		"\u0000\u0000\u0000\u00c9\u00c7\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005"+
		"\u0019\u0000\u0000\u00cb\u00d0\u0003*\u0015\u0000\u00cc\u00cd\u0005\u0016"+
		"\u0000\u0000\u00cd\u00d0\u0003*\u0015\u0000\u00ce\u00d0\u0003,\u0016\u0000"+
		"\u00cf\u00ca\u0001\u0000\u0000\u0000\u00cf\u00cc\u0001\u0000\u0000\u0000"+
		"\u00cf\u00ce\u0001\u0000\u0000\u0000\u00d0+\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d9\u0005\u001c\u0000\u0000\u00d2\u00d9\u0005\u001d\u0000\u0000\u00d3"+
		"\u00d9\u0005\u001b\u0000\u0000\u00d4\u00d5\u0005\u0003\u0000\u0000\u00d5"+
		"\u00d6\u0003\u0018\f\u0000\u00d6\u00d7\u0005\u0004\u0000\u0000\u00d7\u00d9"+
		"\u0001\u0000\u0000\u0000\u00d8\u00d1\u0001\u0000\u0000\u0000\u00d8\u00d2"+
		"\u0001\u0000\u0000\u0000\u00d8\u00d3\u0001\u0000\u0000\u0000\u00d8\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d9-\u0001\u0000\u0000\u0000\u00131=EH[`gm"+
		"r|\u0081\u009d\u00a2\u00b0\u00b7\u00bf\u00c7\u00cf\u00d8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}