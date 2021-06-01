# Este script carga el pipeline con el modelo
# entrenado y lo utiliza para predecir.


# Métodos y librerías que necesitamos en este script
import numpy as np
import pandas as pd
import logging


# De la propia librería:
from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model.processing.validation import validate_inputs
from regression_model import __version__ as _version


# El registro para el log
_logger = logging.getLogger(__name__)

# Carga el pipeline guardado
pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*, input_data) -> dict:
    """Hacer predicción utilizando el pipeline definido."""

    data = pd.read_json(input_data)
    validated_data = validate_inputs(input_data=data) #desde validation.py
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)

    results = {"predictions": output, "version": _version}

    _logger.info(
		# El log nos devolverá el resultado definido: datos predichos 
		# y la versiónde la librería con la que han sido generados.
        f"Making predictions with model version: {_version} "
        f"Inputs: {validated_data} "
        f"Predictions: {results}"
    )
    return results #Las predicciones.
