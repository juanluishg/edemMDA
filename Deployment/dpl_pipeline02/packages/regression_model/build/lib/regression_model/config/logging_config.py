# En este secript se establece la forma en que vamos a 
# registrar (log) los procesos en 
# nuestra librería. Es configurando una forma "loggear"
# los puntos del proceso que nos parezcan relevantes.

# Módulos y librerías necesarias:
import logging
import sys




# Aquí establecemos el formato con el que se van a mostrar
# estos registros.
FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler
