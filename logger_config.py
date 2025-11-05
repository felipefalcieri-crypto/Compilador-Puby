import logging
import sys

def setup_logger():
    logger_name = "Puby"
    log_file = "Puby.log"

    # Remove handlers antigos
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),              # Console
            logging.FileHandler(log_file, mode='w', encoding='utf-8')  # Arquivo
        ]
    )

    # Suprimir logs internos do ANTLR
    logging.getLogger("antlr4").setLevel(logging.ERROR)

    return logging.getLogger(logger_name)

# Configurar logger ao importar
setup_logger()
