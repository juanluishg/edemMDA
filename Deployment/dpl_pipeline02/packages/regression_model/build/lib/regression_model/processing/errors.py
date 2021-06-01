# En este script se definen, a modo de ejemplo,
# dos clases para dos tipos de errores:
# uno genérico y uno específico de los datos.

class BaseError(Exception):
    """Error de base en la librería."""


class InvalidModelInputError(BaseError):
    """Los datos de entrada contienen errores."""
