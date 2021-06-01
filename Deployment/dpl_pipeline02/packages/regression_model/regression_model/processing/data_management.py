# En este script tenemos las funciones para el 
# procesamiento: cargar datos, 
# guardar/cargar/actualizar el pipeline.


# Librerías y módulos necesarios en este script:
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
import logging
_logger = logging.getLogger(__name__)

# De la propia librería.
from regression_model.config import config
from regression_model import __version__ as _version


# FUNCIONES:

def load_dataset(*, file_name: str) -> pd.DataFrame:
    """Carga los datos."""
    _data = pd.read_csv(f"{config.DATASET_DIR}/{file_name}")
    return _data


def save_pipeline(*, pipeline_to_persist) -> None:
    """Fijar el pipeline (persist).
    Guarda la versión del modelo y sobrescribe
    cualquier modelo guardado con anterioridad.
	Asegura que se publica la librería con un
	único modelo.
    """

    # Perparar el archivo a guardar con su versión.
    save_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name
		# Un archivo PKL es un archivo creado por pickle, 
		# un módulo de Python que permite que los objetos 
		# se serialicen en archivos en el disco y se vuelvan 
		# a deserializar en el programa en tiempo de ejecución. 
		# Contiene una secuencia de bytes que representa los objetos.
    remove_old_pipelines(files_to_keep=save_file_name)
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f"saved pipeline: {save_file_name}")
		# Registra (log) que se ha guardado el archivo.


def load_pipeline(*, file_name: str) -> Pipeline:
    """Cargar el pipeline guardado."""

    file_path = config.TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep) -> None:
    """
    Borrar pipelines obsoletos.
    Asegura que hay un mapeado uno a uno
    entre la versión de la librería y la versión
    del modelo a importar y usar por otras aplicaciones.
    """

    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in [files_to_keep, "__init__.py"]:
            model_file.unlink()
