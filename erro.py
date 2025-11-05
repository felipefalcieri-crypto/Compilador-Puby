class Erro:
    def __init__(self):
        self.tem_lexico = False
        self.tem_sintatico = False
        self.tem_semantico = False

    def registrar_erro(self, tipo: str, linha: int, coluna: int, mensagem: str):
        # Ajuste de coluna para começar em 1
        coluna = coluna + 1 if coluna >= 0 else coluna

        if tipo == "LEXICO":
            self.tem_lexico = True
            prefixo = "ERRO LÉXICO"
        elif tipo == "SINTATICO":
            self.tem_sintatico = True
            prefixo = "ERRO SINTÁTICO"
        else:
            self.tem_semantico = True
            prefixo = "ERRO SEMÂNTICO"

        print(f"{prefixo} [Linha {linha}, Coluna {coluna}]: {mensagem}")


from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self, erro_handler: Erro, tipo_erro: str):
        super().__init__()
        self.erro_handler = erro_handler
        self.tipo_erro = tipo_erro

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.erro_handler.registrar_erro(self.tipo_erro, line, column, msg)
