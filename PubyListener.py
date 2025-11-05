# Generated from Puby.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PubyParser import PubyParser
else:
    from PubyParser import PubyParser

# This class defines a complete listener for a parse tree produced by PubyParser.
class PubyListener(ParseTreeListener):

    # Enter a parse tree produced by PubyParser#programa.
    def enterPrograma(self, ctx:PubyParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PubyParser#programa.
    def exitPrograma(self, ctx:PubyParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PubyParser#comando.
    def enterComando(self, ctx:PubyParser.ComandoContext):
        pass

    # Exit a parse tree produced by PubyParser#comando.
    def exitComando(self, ctx:PubyParser.ComandoContext):
        pass


    # Enter a parse tree produced by PubyParser#escrita.
    def enterEscrita(self, ctx:PubyParser.EscritaContext):
        pass

    # Exit a parse tree produced by PubyParser#escrita.
    def exitEscrita(self, ctx:PubyParser.EscritaContext):
        pass


    # Enter a parse tree produced by PubyParser#leitura.
    def enterLeitura(self, ctx:PubyParser.LeituraContext):
        pass

    # Exit a parse tree produced by PubyParser#leitura.
    def exitLeitura(self, ctx:PubyParser.LeituraContext):
        pass


    # Enter a parse tree produced by PubyParser#atribuicao.
    def enterAtribuicao(self, ctx:PubyParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by PubyParser#atribuicao.
    def exitAtribuicao(self, ctx:PubyParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by PubyParser#condicional.
    def enterCondicional(self, ctx:PubyParser.CondicionalContext):
        pass

    # Exit a parse tree produced by PubyParser#condicional.
    def exitCondicional(self, ctx:PubyParser.CondicionalContext):
        pass


    # Enter a parse tree produced by PubyParser#corpo_if.
    def enterCorpo_if(self, ctx:PubyParser.Corpo_ifContext):
        pass

    # Exit a parse tree produced by PubyParser#corpo_if.
    def exitCorpo_if(self, ctx:PubyParser.Corpo_ifContext):
        pass


    # Enter a parse tree produced by PubyParser#enquanto.
    def enterEnquanto(self, ctx:PubyParser.EnquantoContext):
        pass

    # Exit a parse tree produced by PubyParser#enquanto.
    def exitEnquanto(self, ctx:PubyParser.EnquantoContext):
        pass


    # Enter a parse tree produced by PubyParser#laco_para.
    def enterLaco_para(self, ctx:PubyParser.Laco_paraContext):
        pass

    # Exit a parse tree produced by PubyParser#laco_para.
    def exitLaco_para(self, ctx:PubyParser.Laco_paraContext):
        pass


    # Enter a parse tree produced by PubyParser#intervalo.
    def enterIntervalo(self, ctx:PubyParser.IntervaloContext):
        pass

    # Exit a parse tree produced by PubyParser#intervalo.
    def exitIntervalo(self, ctx:PubyParser.IntervaloContext):
        pass


    # Enter a parse tree produced by PubyParser#incremento.
    def enterIncremento(self, ctx:PubyParser.IncrementoContext):
        pass

    # Exit a parse tree produced by PubyParser#incremento.
    def exitIncremento(self, ctx:PubyParser.IncrementoContext):
        pass


    # Enter a parse tree produced by PubyParser#condicao.
    def enterCondicao(self, ctx:PubyParser.CondicaoContext):
        pass

    # Exit a parse tree produced by PubyParser#condicao.
    def exitCondicao(self, ctx:PubyParser.CondicaoContext):
        pass


    # Enter a parse tree produced by PubyParser#expressao.
    def enterExpressao(self, ctx:PubyParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by PubyParser#expressao.
    def exitExpressao(self, ctx:PubyParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by PubyParser#logico_baixo.
    def enterLogico_baixo(self, ctx:PubyParser.Logico_baixoContext):
        pass

    # Exit a parse tree produced by PubyParser#logico_baixo.
    def exitLogico_baixo(self, ctx:PubyParser.Logico_baixoContext):
        pass


    # Enter a parse tree produced by PubyParser#logico_baixo_suf.
    def enterLogico_baixo_suf(self, ctx:PubyParser.Logico_baixo_sufContext):
        pass

    # Exit a parse tree produced by PubyParser#logico_baixo_suf.
    def exitLogico_baixo_suf(self, ctx:PubyParser.Logico_baixo_sufContext):
        pass


    # Enter a parse tree produced by PubyParser#not_baixo.
    def enterNot_baixo(self, ctx:PubyParser.Not_baixoContext):
        pass

    # Exit a parse tree produced by PubyParser#not_baixo.
    def exitNot_baixo(self, ctx:PubyParser.Not_baixoContext):
        pass


    # Enter a parse tree produced by PubyParser#logico_alto.
    def enterLogico_alto(self, ctx:PubyParser.Logico_altoContext):
        pass

    # Exit a parse tree produced by PubyParser#logico_alto.
    def exitLogico_alto(self, ctx:PubyParser.Logico_altoContext):
        pass


    # Enter a parse tree produced by PubyParser#logico_alto_suf.
    def enterLogico_alto_suf(self, ctx:PubyParser.Logico_alto_sufContext):
        pass

    # Exit a parse tree produced by PubyParser#logico_alto_suf.
    def exitLogico_alto_suf(self, ctx:PubyParser.Logico_alto_sufContext):
        pass


    # Enter a parse tree produced by PubyParser#rel.
    def enterRel(self, ctx:PubyParser.RelContext):
        pass

    # Exit a parse tree produced by PubyParser#rel.
    def exitRel(self, ctx:PubyParser.RelContext):
        pass


    # Enter a parse tree produced by PubyParser#soma.
    def enterSoma(self, ctx:PubyParser.SomaContext):
        pass

    # Exit a parse tree produced by PubyParser#soma.
    def exitSoma(self, ctx:PubyParser.SomaContext):
        pass


    # Enter a parse tree produced by PubyParser#mult.
    def enterMult(self, ctx:PubyParser.MultContext):
        pass

    # Exit a parse tree produced by PubyParser#mult.
    def exitMult(self, ctx:PubyParser.MultContext):
        pass


    # Enter a parse tree produced by PubyParser#unario.
    def enterUnario(self, ctx:PubyParser.UnarioContext):
        pass

    # Exit a parse tree produced by PubyParser#unario.
    def exitUnario(self, ctx:PubyParser.UnarioContext):
        pass


    # Enter a parse tree produced by PubyParser#primario.
    def enterPrimario(self, ctx:PubyParser.PrimarioContext):
        pass

    # Exit a parse tree produced by PubyParser#primario.
    def exitPrimario(self, ctx:PubyParser.PrimarioContext):
        pass



del PubyParser