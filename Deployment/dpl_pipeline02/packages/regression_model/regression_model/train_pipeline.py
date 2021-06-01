# En este script definimos la función que entrena el modelo

# Toma los métodos que hemos definido a lo largo de las capas
# de nuestra librería: proprocesado de datos, transformación de variables,
# definiciónd el pipeline...


# Librerías y métodos necesarios en este script:
import numpy as np
from sklearn.model_selection import train_test_split
import logging

# De la propia librería:
from regression_model import pipeline # Descripción del pipeline.
from regression_model.processing.data_management import load_dataset, save_pipeline # carga de datos y función para guardar el pipeline in /trained_model
from regression_model.config import config # Paths, listas de variables, etc.
from regression_model import __version__ as _version # Control de la versión.


_logger = logging.getLogger(__name__)


def run_training() -> None:
    """Entenar el modelo."""

    # Lee los datos de entrenamiento
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # Divide entre set de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], test_size=0.1, random_state=0
    )  # indicamos la semilla!!!

    # Transformamos la variable objetivo
    y_train = np.log(y_train)

    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == "__main__":
    run_training()
