import logging
from antlr4 import FileStream, CommonTokenStream, Token
from PubyLexer import PubyLexer
from erro import Erro, CustomErrorListener

class AnaliseLexica:
    def __init__(self, erro_handler: Erro):
        self.erro_handler = erro_handler
        self.logger = logging.getLogger("Puby")
        self.lista_tokens = []

    def _log_tokens(self, lexer: PubyLexer):
        temp_lexer = PubyLexer(lexer.inputStream)
        temp_lexer.removeErrorListeners()
        
        token = temp_lexer.nextToken()
        self.lista_tokens = []
        while token.type != Token.EOF:
            token_name = ""
            try:
                token_name = temp_lexer.vocabulary.getSymbolicName(token.type)
                if token_name is None:
                    token_name = temp_lexer.vocabulary.getLiteralName(token.type)
                    if token_name is None:
                        token_name = f"TYPE_{token.type}"
                    else:
                        if token_name.startswith("'") and token_name.endswith("'"):
                            token_name = token_name[1:-1]
            except Exception:
                token_name = f"TYPE_{token.type}"

            self.logger.info(f"Token: {token_name}, Texto: '{token.text}', Linha: {token.line}, Coluna: {token.column+1}")
            self.lista_tokens.append(token)
            token = temp_lexer.nextToken()
        
        self.lista_tokens.append(token)
        eof_symbol_name = "EOF"
        try:
            eof_symbol_name = temp_lexer.vocabulary.getSymbolicName(token.type) or "EOF"
        except Exception:
            pass
        self.logger.info(f"Token: {eof_symbol_name}, Texto: '{token.text}', Linha: {token.line}, Coluna: {token.column+1}")


    def executarAnaliseLexica(self, nome_arquivo_fonte: str):
        self.logger.info(f"Iniciando análise léxica do arquivo: {nome_arquivo_fonte}")
        try:
            input_stream = FileStream(nome_arquivo_fonte, encoding='utf-8')
            lexer = PubyLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(CustomErrorListener(self.erro_handler, "LEXICO"))

            log_input_stream = FileStream(nome_arquivo_fonte, encoding='utf-8')
            log_lexer = PubyLexer(log_input_stream)
            self._log_tokens(log_lexer)

            token_stream = CommonTokenStream(lexer)
            self.logger.info("Análise léxica concluída.")
            return self.lista_tokens, token_stream

        except FileNotFoundError:
            self.erro_handler.registrar_erro("LEXICO", 0, 0, f"Arquivo fonte '{nome_arquivo_fonte}' não encontrado.")
            return None, None
        except Exception as e:
            self.erro_handler.registrar_erro("LEXICO", 0, 0, f"Erro inesperado na análise léxica: {e}")
            self.logger.exception("Detalhes do erro inesperado:")
            return None, None
