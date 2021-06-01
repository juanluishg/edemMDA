# Este script contiene la configuración necesaria
# para controlar la versión y el registro
# "log" de funcionamiento de la librería.


# Librerías para que funcione el script:
import logging

# De la propia librería:
from regression_model.config import config
from regression_model.config import logging_config


VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

# Configura el logger para que podamos usarlo
# en la librería
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False

# Guarda la versión de la librería para que podamos
# usarla
with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()
