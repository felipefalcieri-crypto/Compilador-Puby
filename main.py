import logger_config
from compilador import Compilador

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_fonte.puby>")
        sys.exit(1)

    arquivo_fonte = sys.argv[1]
    compilador = Compilador(arquivo_fonte)
    compilador.compilar()
