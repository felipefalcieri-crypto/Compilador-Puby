import logging
import subprocess
from antlr4 import CommonTokenStream
from PubyParser import PubyParser
from erro import Erro, CustomErrorListener

class AnaliseSintatica:
    def __init__(self, erro_handler: Erro):
        self.erro_handler = erro_handler
        self.logger = logging.getLogger("Puby")
        self.ast = None

    def executarAnaliseSintatica(self, token_stream: CommonTokenStream):
        self.logger.info("Iniciando análise sintática...")

        if not token_stream:
            self.erro_handler.registrar_erro("SINTATICO", 0, 0, "Stream de tokens não fornecida.")
            return None

        try:
            parser = PubyParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(CustomErrorListener(self.erro_handler, "SINTATICO"))

            self.ast = parser.programa()

            if not self.erro_handler.tem_sintatico:
                self.logger.info("Análise sintática concluída com sucesso. AST gerada.")
            else:
                self.logger.error("Erros sintáticos encontrados. AST pode estar incompleta.")

            return self.ast

        except Exception as e:
            self.erro_handler.registrar_erro("SINTATICO", 0, 0, f"Erro inesperado na análise sintática: {e}")
            return None

    # ------------ EXPORTAÇÃO DA AST PARA DOT & SVG ------------

    def _gerar_dot_recursivo(self, no, parser_rules, id_map, dot_linhas):
        try:
            no_id = id(no)
            if no_id not in id_map:
                id_map[no_id] = len(id_map)

            # Define label para o nó
            if hasattr(no, 'getRuleIndex'):  # Nó interno (regra)
                nome_regra = parser_rules[no.getRuleIndex()]
                label = nome_regra

            elif hasattr(no, 'symbol'):  # Token (folha)
                texto = no.getText() or ""
                texto_escapado = (
                    texto.replace("\\", "\\\\")
                         .replace("\"", "\\\"")
                         .replace("\n", "\\n")
                         .replace("\t", "\\t")
                )
                token_name = PubyParser.symbolicNames[no.symbol.type]
                label = f"{texto_escapado}\\n<Token: {token_name}>"
            else:
                return

            dot_linhas.append(f'  node{id_map[no_id]} [label="{label}"];')

            # ligações (arestas)
            if hasattr(no, 'children') and no.children:
                for child in no.children:
                    child_id = id(child)
                    if child_id not in id_map:
                        id_map[child_id] = len(id_map)
                    dot_linhas.append(f'  node{id_map[no_id]} -- node{id_map[child_id]};')
                    self._gerar_dot_recursivo(child, parser_rules, id_map, dot_linhas)

        except Exception as e:
            self.logger.error(f"Falha ao gerar nó DOT: {e}")

    def exportarAST_DOT(self, ast, nome_arquivo_dot: str):
        self.logger.info(f"Exportando AST para DOT: {nome_arquivo_dot}")

        if not ast:
            self.erro_handler.registrar_erro("SINTATICO", 0, 0, "AST inválida para exportação DOT.")
            raise Exception("Falha na exportação DOT")

        try:
            parser_temp = PubyParser(None)
            parser_rules = parser_temp.ruleNames

            dot_linhas = [
                'graph "Árvore Sintática Puby" {',
                '  node [fontname="Arial" shape=box];',
                '  edge [arrowhead=none];'
            ]

            id_map = {}
            self._gerar_dot_recursivo(ast, parser_rules, id_map, dot_linhas)
            dot_linhas.append('}')

            with open(nome_arquivo_dot, 'w', encoding='utf-8') as f:
                f.write("\n".join(dot_linhas))

            self.logger.info(f"AST exportada com sucesso para {nome_arquivo_dot}")

        except Exception as e:
            self.erro_handler.registrar_erro("SINTATICO", 0, 0, f"Erro ao exportar AST DOT: {e}")
            raise

    def exportarAST_SVG(self, nome_arquivo_dot: str, nome_arquivo_svg: str):
        self.logger.info(f"Gerando SVG: {nome_arquivo_svg}")

        try:
            resultado = subprocess.run(['dot', '-Tsvg', nome_arquivo_dot, '-o', nome_arquivo_svg], capture_output=True, text=True)

            if resultado.returncode != 0:
                raise Exception(resultado.stderr.strip())

            self.logger.info(f"SVG gerado com sucesso: {nome_arquivo_svg}")

        except FileNotFoundError:
            self.erro_handler.registrar_erro("SINTATICO", 0, 0, "Graphviz não encontrado. Instale para gerar SVG.")
            raise
        except Exception as e:
            self.erro_handler.registrar_erro("SINTATICO", 0, 0, f"Erro ao gerar SVG: {e}")
            raise
