# Generated from Puby.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,219,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,5,2,68,8,
        2,10,2,12,2,71,9,2,3,2,73,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,5,1,5,3,
        5,97,8,5,1,5,1,5,1,6,5,6,102,8,6,10,6,12,6,105,9,6,1,7,1,7,1,7,3,
        7,110,8,7,1,7,5,7,113,8,7,10,7,12,7,116,9,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,3,8,125,8,8,1,8,5,8,128,8,8,10,8,12,8,131,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,158,8,14,1,15,
        1,15,1,15,3,15,163,8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,3,17,177,8,17,1,18,1,18,1,18,5,18,182,8,18,10,
        18,12,18,185,9,18,1,19,1,19,1,19,5,19,190,8,19,10,19,12,19,193,9,
        19,1,20,1,20,1,20,5,20,198,8,20,10,20,12,20,201,9,20,1,21,1,21,1,
        21,1,21,1,21,3,21,208,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,217,8,22,1,22,0,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,0,1,1,0,20,21,224,0,49,1,0,0,0,2,61,1,0,
        0,0,4,63,1,0,0,0,6,74,1,0,0,0,8,78,1,0,0,0,10,82,1,0,0,0,12,103,
        1,0,0,0,14,106,1,0,0,0,16,119,1,0,0,0,18,134,1,0,0,0,20,138,1,0,
        0,0,22,141,1,0,0,0,24,143,1,0,0,0,26,145,1,0,0,0,28,157,1,0,0,0,
        30,162,1,0,0,0,32,164,1,0,0,0,34,176,1,0,0,0,36,178,1,0,0,0,38,186,
        1,0,0,0,40,194,1,0,0,0,42,207,1,0,0,0,44,216,1,0,0,0,46,48,3,2,1,
        0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,
        1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,62,3,4,2,0,55,
        62,3,6,3,0,56,62,3,8,4,0,57,62,3,10,5,0,58,62,3,14,7,0,59,62,3,16,
        8,0,60,62,3,20,10,0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,
        57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,
        0,63,72,5,13,0,0,64,69,3,24,12,0,65,66,5,1,0,0,66,68,3,24,12,0,67,
        65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,73,1,0,0,
        0,71,69,1,0,0,0,72,64,1,0,0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,75,5,
        27,0,0,75,76,5,2,0,0,76,77,5,14,0,0,77,7,1,0,0,0,78,79,5,27,0,0,
        79,80,5,2,0,0,80,81,3,24,12,0,81,9,1,0,0,0,82,83,5,5,0,0,83,84,3,
        22,11,0,84,91,3,12,6,0,85,86,5,6,0,0,86,87,3,22,11,0,87,88,3,12,
        6,0,88,90,1,0,0,0,89,85,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,
        1,0,0,0,92,96,1,0,0,0,93,91,1,0,0,0,94,95,5,7,0,0,95,97,3,12,6,0,
        96,94,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,8,0,0,99,11,1,
        0,0,0,100,102,3,2,1,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,
        0,0,0,103,104,1,0,0,0,104,13,1,0,0,0,105,103,1,0,0,0,106,107,5,9,
        0,0,107,109,3,22,11,0,108,110,5,12,0,0,109,108,1,0,0,0,109,110,1,
        0,0,0,110,114,1,0,0,0,111,113,3,2,1,0,112,111,1,0,0,0,113,116,1,
        0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,114,1,
        0,0,0,117,118,5,8,0,0,118,15,1,0,0,0,119,120,5,10,0,0,120,121,5,
        27,0,0,121,122,5,11,0,0,122,124,3,18,9,0,123,125,5,12,0,0,124,123,
        1,0,0,0,124,125,1,0,0,0,125,129,1,0,0,0,126,128,3,2,1,0,127,126,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,
        1,0,0,0,131,129,1,0,0,0,132,133,5,8,0,0,133,17,1,0,0,0,134,135,3,
        24,12,0,135,136,5,26,0,0,136,137,3,24,12,0,137,19,1,0,0,0,138,139,
        5,27,0,0,139,140,7,0,0,0,140,21,1,0,0,0,141,142,3,24,12,0,142,23,
        1,0,0,0,143,144,3,26,13,0,144,25,1,0,0,0,145,146,3,30,15,0,146,147,
        3,28,14,0,147,27,1,0,0,0,148,149,5,16,0,0,149,150,3,30,15,0,150,
        151,3,28,14,0,151,158,1,0,0,0,152,153,5,17,0,0,153,154,3,30,15,0,
        154,155,3,28,14,0,155,158,1,0,0,0,156,158,1,0,0,0,157,148,1,0,0,
        0,157,152,1,0,0,0,157,156,1,0,0,0,158,29,1,0,0,0,159,160,5,15,0,
        0,160,163,3,30,15,0,161,163,3,32,16,0,162,159,1,0,0,0,162,161,1,
        0,0,0,163,31,1,0,0,0,164,165,3,36,18,0,165,166,3,34,17,0,166,33,
        1,0,0,0,167,168,5,18,0,0,168,169,3,36,18,0,169,170,3,34,17,0,170,
        177,1,0,0,0,171,172,5,19,0,0,172,173,3,36,18,0,173,174,3,34,17,0,
        174,177,1,0,0,0,175,177,1,0,0,0,176,167,1,0,0,0,176,171,1,0,0,0,
        176,175,1,0,0,0,177,35,1,0,0,0,178,183,3,38,19,0,179,180,5,24,0,
        0,180,182,3,38,19,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,1,0,
        0,0,183,184,1,0,0,0,184,37,1,0,0,0,185,183,1,0,0,0,186,191,3,40,
        20,0,187,188,5,22,0,0,188,190,3,40,20,0,189,187,1,0,0,0,190,193,
        1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,39,1,0,0,0,193,191,1,
        0,0,0,194,199,3,42,21,0,195,196,5,23,0,0,196,198,3,42,21,0,197,195,
        1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,41,1,
        0,0,0,201,199,1,0,0,0,202,203,5,25,0,0,203,208,3,42,21,0,204,205,
        5,22,0,0,205,208,3,42,21,0,206,208,3,44,22,0,207,202,1,0,0,0,207,
        204,1,0,0,0,207,206,1,0,0,0,208,43,1,0,0,0,209,217,5,28,0,0,210,
        217,5,29,0,0,211,217,5,27,0,0,212,213,5,3,0,0,213,214,3,24,12,0,
        214,215,5,4,0,0,215,217,1,0,0,0,216,209,1,0,0,0,216,210,1,0,0,0,
        216,211,1,0,0,0,216,212,1,0,0,0,217,45,1,0,0,0,19,49,61,69,72,91,
        96,103,109,114,124,129,157,162,176,183,191,199,207,216
    ]

class PubyParser ( Parser ):

    grammarFileName = "Puby.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'='", "'('", "')'", "'if'", "'elsif'", 
                     "'else'", "'end'", "'while'", "'for'", "'in'", "'do'", 
                     "'puts'", "'gets'", "'not'", "'and'", "'or'", "'&&'", 
                     "'||'", "'++'", "'--'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "ELSIF", "ELSE", "END", "WHILE", 
                      "FOR", "IN", "DO", "PUTS", "GETS", "NOT", "AND_WORD", 
                      "OR_WORD", "AND_SYM", "OR_SYM", "OP_INC", "OP_DEC", 
                      "OP_ADD", "OP_MUL", "OP_REL", "OP_NOT", "RANGE", "ID", 
                      "NUM", "STRING", "WS" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_escrita = 2
    RULE_leitura = 3
    RULE_atribuicao = 4
    RULE_condicional = 5
    RULE_corpo_if = 6
    RULE_enquanto = 7
    RULE_laco_para = 8
    RULE_intervalo = 9
    RULE_incremento = 10
    RULE_condicao = 11
    RULE_expressao = 12
    RULE_logico_baixo = 13
    RULE_logico_baixo_suf = 14
    RULE_not_baixo = 15
    RULE_logico_alto = 16
    RULE_logico_alto_suf = 17
    RULE_rel = 18
    RULE_soma = 19
    RULE_mult = 20
    RULE_unario = 21
    RULE_primario = 22

    ruleNames =  [ "programa", "comando", "escrita", "leitura", "atribuicao", 
                   "condicional", "corpo_if", "enquanto", "laco_para", "intervalo", 
                   "incremento", "condicao", "expressao", "logico_baixo", 
                   "logico_baixo_suf", "not_baixo", "logico_alto", "logico_alto_suf", 
                   "rel", "soma", "mult", "unario", "primario" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IF=5
    ELSIF=6
    ELSE=7
    END=8
    WHILE=9
    FOR=10
    IN=11
    DO=12
    PUTS=13
    GETS=14
    NOT=15
    AND_WORD=16
    OR_WORD=17
    AND_SYM=18
    OR_SYM=19
    OP_INC=20
    OP_DEC=21
    OP_ADD=22
    OP_MUL=23
    OP_REL=24
    OP_NOT=25
    RANGE=26
    ID=27
    NUM=28
    STRING=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PubyParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PubyParser.ComandoContext,i)


        def getRuleIndex(self):
            return PubyParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = PubyParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134227488) != 0):
                self.state = 46
                self.comando()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(PubyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def escrita(self):
            return self.getTypedRuleContext(PubyParser.EscritaContext,0)


        def leitura(self):
            return self.getTypedRuleContext(PubyParser.LeituraContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(PubyParser.AtribuicaoContext,0)


        def condicional(self):
            return self.getTypedRuleContext(PubyParser.CondicionalContext,0)


        def enquanto(self):
            return self.getTypedRuleContext(PubyParser.EnquantoContext,0)


        def laco_para(self):
            return self.getTypedRuleContext(PubyParser.Laco_paraContext,0)


        def incremento(self):
            return self.getTypedRuleContext(PubyParser.IncrementoContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = PubyParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.escrita()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.leitura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.atribuicao()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.enquanto()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.laco_para()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.incremento()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUTS(self):
            return self.getToken(PubyParser.PUTS, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(PubyParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return PubyParser.RULE_escrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrita" ):
                listener.enterEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrita" ):
                listener.exitEscrita(self)




    def escrita(self):

        localctx = PubyParser.EscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_escrita)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(PubyParser.PUTS)
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 64
                self.expressao()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 65
                    self.match(PubyParser.T__0)
                    self.state = 66
                    self.expressao()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PubyParser.ID, 0)

        def GETS(self):
            return self.getToken(PubyParser.GETS, 0)

        def getRuleIndex(self):
            return PubyParser.RULE_leitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeitura" ):
                listener.enterLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeitura" ):
                listener.exitLeitura(self)




    def leitura(self):

        localctx = PubyParser.LeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_leitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PubyParser.ID)
            self.state = 75
            self.match(PubyParser.T__1)
            self.state = 76
            self.match(PubyParser.GETS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PubyParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(PubyParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = PubyParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(PubyParser.ID)
            self.state = 79
            self.match(PubyParser.T__1)
            self.state = 80
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PubyParser.IF, 0)

        def condicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.CondicaoContext)
            else:
                return self.getTypedRuleContext(PubyParser.CondicaoContext,i)


        def corpo_if(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.Corpo_ifContext)
            else:
                return self.getTypedRuleContext(PubyParser.Corpo_ifContext,i)


        def END(self):
            return self.getToken(PubyParser.END, 0)

        def ELSIF(self, i:int=None):
            if i is None:
                return self.getTokens(PubyParser.ELSIF)
            else:
                return self.getToken(PubyParser.ELSIF, i)

        def ELSE(self):
            return self.getToken(PubyParser.ELSE, 0)

        def getRuleIndex(self):
            return PubyParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = PubyParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PubyParser.IF)
            self.state = 83
            self.condicao()
            self.state = 84
            self.corpo_if()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 85
                self.match(PubyParser.ELSIF)
                self.state = 86
                self.condicao()
                self.state = 87
                self.corpo_if()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 94
                self.match(PubyParser.ELSE)
                self.state = 95
                self.corpo_if()


            self.state = 98
            self.match(PubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Corpo_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PubyParser.ComandoContext,i)


        def getRuleIndex(self):
            return PubyParser.RULE_corpo_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorpo_if" ):
                listener.enterCorpo_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorpo_if" ):
                listener.exitCorpo_if(self)




    def corpo_if(self):

        localctx = PubyParser.Corpo_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_corpo_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134227488) != 0):
                self.state = 100
                self.comando()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PubyParser.WHILE, 0)

        def condicao(self):
            return self.getTypedRuleContext(PubyParser.CondicaoContext,0)


        def END(self):
            return self.getToken(PubyParser.END, 0)

        def DO(self):
            return self.getToken(PubyParser.DO, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PubyParser.ComandoContext,i)


        def getRuleIndex(self):
            return PubyParser.RULE_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnquanto" ):
                listener.enterEnquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnquanto" ):
                listener.exitEnquanto(self)




    def enquanto(self):

        localctx = PubyParser.EnquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_enquanto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(PubyParser.WHILE)
            self.state = 107
            self.condicao()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 108
                self.match(PubyParser.DO)


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134227488) != 0):
                self.state = 111
                self.comando()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(PubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Laco_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PubyParser.FOR, 0)

        def ID(self):
            return self.getToken(PubyParser.ID, 0)

        def IN(self):
            return self.getToken(PubyParser.IN, 0)

        def intervalo(self):
            return self.getTypedRuleContext(PubyParser.IntervaloContext,0)


        def END(self):
            return self.getToken(PubyParser.END, 0)

        def DO(self):
            return self.getToken(PubyParser.DO, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PubyParser.ComandoContext,i)


        def getRuleIndex(self):
            return PubyParser.RULE_laco_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaco_para" ):
                listener.enterLaco_para(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaco_para" ):
                listener.exitLaco_para(self)




    def laco_para(self):

        localctx = PubyParser.Laco_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_laco_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(PubyParser.FOR)
            self.state = 120
            self.match(PubyParser.ID)
            self.state = 121
            self.match(PubyParser.IN)
            self.state = 122
            self.intervalo()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 123
                self.match(PubyParser.DO)


            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134227488) != 0):
                self.state = 126
                self.comando()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(PubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervaloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(PubyParser.ExpressaoContext,i)


        def RANGE(self):
            return self.getToken(PubyParser.RANGE, 0)

        def getRuleIndex(self):
            return PubyParser.RULE_intervalo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntervalo" ):
                listener.enterIntervalo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntervalo" ):
                listener.exitIntervalo(self)




    def intervalo(self):

        localctx = PubyParser.IntervaloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_intervalo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.expressao()
            self.state = 135
            self.match(PubyParser.RANGE)
            self.state = 136
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PubyParser.ID, 0)

        def OP_INC(self):
            return self.getToken(PubyParser.OP_INC, 0)

        def OP_DEC(self):
            return self.getToken(PubyParser.OP_DEC, 0)

        def getRuleIndex(self):
            return PubyParser.RULE_incremento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)




    def incremento(self):

        localctx = PubyParser.IncrementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_incremento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(PubyParser.ID)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(PubyParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)




    def condicao(self):

        localctx = PubyParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logico_baixo(self):
            return self.getTypedRuleContext(PubyParser.Logico_baixoContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = PubyParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.logico_baixo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logico_baixoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_baixo(self):
            return self.getTypedRuleContext(PubyParser.Not_baixoContext,0)


        def logico_baixo_suf(self):
            return self.getTypedRuleContext(PubyParser.Logico_baixo_sufContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_logico_baixo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico_baixo" ):
                listener.enterLogico_baixo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico_baixo" ):
                listener.exitLogico_baixo(self)




    def logico_baixo(self):

        localctx = PubyParser.Logico_baixoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logico_baixo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.not_baixo()
            self.state = 146
            self.logico_baixo_suf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logico_baixo_sufContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_WORD(self):
            return self.getToken(PubyParser.AND_WORD, 0)

        def not_baixo(self):
            return self.getTypedRuleContext(PubyParser.Not_baixoContext,0)


        def logico_baixo_suf(self):
            return self.getTypedRuleContext(PubyParser.Logico_baixo_sufContext,0)


        def OR_WORD(self):
            return self.getToken(PubyParser.OR_WORD, 0)

        def getRuleIndex(self):
            return PubyParser.RULE_logico_baixo_suf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico_baixo_suf" ):
                listener.enterLogico_baixo_suf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico_baixo_suf" ):
                listener.exitLogico_baixo_suf(self)




    def logico_baixo_suf(self):

        localctx = PubyParser.Logico_baixo_sufContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logico_baixo_suf)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(PubyParser.AND_WORD)
                self.state = 149
                self.not_baixo()
                self.state = 150
                self.logico_baixo_suf()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(PubyParser.OR_WORD)
                self.state = 153
                self.not_baixo()
                self.state = 154
                self.logico_baixo_suf()
                pass
            elif token in [-1, 1, 4, 5, 6, 7, 8, 9, 10, 12, 13, 26, 27]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_baixoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PubyParser.NOT, 0)

        def not_baixo(self):
            return self.getTypedRuleContext(PubyParser.Not_baixoContext,0)


        def logico_alto(self):
            return self.getTypedRuleContext(PubyParser.Logico_altoContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_not_baixo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_baixo" ):
                listener.enterNot_baixo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_baixo" ):
                listener.exitNot_baixo(self)




    def not_baixo(self):

        localctx = PubyParser.Not_baixoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_not_baixo)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(PubyParser.NOT)
                self.state = 160
                self.not_baixo()
                pass
            elif token in [3, 22, 25, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.logico_alto()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logico_altoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel(self):
            return self.getTypedRuleContext(PubyParser.RelContext,0)


        def logico_alto_suf(self):
            return self.getTypedRuleContext(PubyParser.Logico_alto_sufContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_logico_alto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico_alto" ):
                listener.enterLogico_alto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico_alto" ):
                listener.exitLogico_alto(self)




    def logico_alto(self):

        localctx = PubyParser.Logico_altoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logico_alto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.rel()
            self.state = 165
            self.logico_alto_suf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logico_alto_sufContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_SYM(self):
            return self.getToken(PubyParser.AND_SYM, 0)

        def rel(self):
            return self.getTypedRuleContext(PubyParser.RelContext,0)


        def logico_alto_suf(self):
            return self.getTypedRuleContext(PubyParser.Logico_alto_sufContext,0)


        def OR_SYM(self):
            return self.getToken(PubyParser.OR_SYM, 0)

        def getRuleIndex(self):
            return PubyParser.RULE_logico_alto_suf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico_alto_suf" ):
                listener.enterLogico_alto_suf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico_alto_suf" ):
                listener.exitLogico_alto_suf(self)




    def logico_alto_suf(self):

        localctx = PubyParser.Logico_alto_sufContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logico_alto_suf)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(PubyParser.AND_SYM)
                self.state = 168
                self.rel()
                self.state = 169
                self.logico_alto_suf()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(PubyParser.OR_SYM)
                self.state = 172
                self.rel()
                self.state = 173
                self.logico_alto_suf()
                pass
            elif token in [-1, 1, 4, 5, 6, 7, 8, 9, 10, 12, 13, 16, 17, 26, 27]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def soma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.SomaContext)
            else:
                return self.getTypedRuleContext(PubyParser.SomaContext,i)


        def OP_REL(self, i:int=None):
            if i is None:
                return self.getTokens(PubyParser.OP_REL)
            else:
                return self.getToken(PubyParser.OP_REL, i)

        def getRuleIndex(self):
            return PubyParser.RULE_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel" ):
                listener.enterRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel" ):
                listener.exitRel(self)




    def rel(self):

        localctx = PubyParser.RelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.soma()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 179
                self.match(PubyParser.OP_REL)
                self.state = 180
                self.soma()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SomaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.MultContext)
            else:
                return self.getTypedRuleContext(PubyParser.MultContext,i)


        def OP_ADD(self, i:int=None):
            if i is None:
                return self.getTokens(PubyParser.OP_ADD)
            else:
                return self.getToken(PubyParser.OP_ADD, i)

        def getRuleIndex(self):
            return PubyParser.RULE_soma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoma" ):
                listener.enterSoma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoma" ):
                listener.exitSoma(self)




    def soma(self):

        localctx = PubyParser.SomaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_soma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.mult()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 187
                self.match(PubyParser.OP_ADD)
                self.state = 188
                self.mult()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubyParser.UnarioContext)
            else:
                return self.getTypedRuleContext(PubyParser.UnarioContext,i)


        def OP_MUL(self, i:int=None):
            if i is None:
                return self.getTokens(PubyParser.OP_MUL)
            else:
                return self.getToken(PubyParser.OP_MUL, i)

        def getRuleIndex(self):
            return PubyParser.RULE_mult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)




    def mult(self):

        localctx = PubyParser.MultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mult)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.unario()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 195
                self.match(PubyParser.OP_MUL)
                self.state = 196
                self.unario()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(PubyParser.OP_NOT, 0)

        def unario(self):
            return self.getTypedRuleContext(PubyParser.UnarioContext,0)


        def OP_ADD(self):
            return self.getToken(PubyParser.OP_ADD, 0)

        def primario(self):
            return self.getTypedRuleContext(PubyParser.PrimarioContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_unario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnario" ):
                listener.enterUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnario" ):
                listener.exitUnario(self)




    def unario(self):

        localctx = PubyParser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unario)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(PubyParser.OP_NOT)
                self.state = 203
                self.unario()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(PubyParser.OP_ADD)
                self.state = 205
                self.unario()
                pass
            elif token in [3, 27, 28, 29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.primario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(PubyParser.NUM, 0)

        def STRING(self):
            return self.getToken(PubyParser.STRING, 0)

        def ID(self):
            return self.getToken(PubyParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(PubyParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return PubyParser.RULE_primario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimario" ):
                listener.enterPrimario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimario" ):
                listener.exitPrimario(self)




    def primario(self):

        localctx = PubyParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primario)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(PubyParser.NUM)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(PubyParser.STRING)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.match(PubyParser.ID)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.match(PubyParser.T__2)
                self.state = 213
                self.expressao()
                self.state = 214
                self.match(PubyParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





