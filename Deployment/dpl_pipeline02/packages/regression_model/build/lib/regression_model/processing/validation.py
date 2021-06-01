# En este escript se especifica la función
# para validar los datos de entrada,
# buscando valores que no puedan procesarse.


# Librarías y métodos para este script
import pandas as pd
# De la propia librería
from regression_model.config import config


def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """Busca valores introducidos que no puedan procesarse."""

    validated_data = input_data.copy()

    # variables numéricas con NA no detectados durante el entrenamiento
    if input_data[config.NUMERICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.NUMERICAL_NA_NOT_ALLOWED
        )

    # variables categóricas con NA no detectados durante el entrenamiento
    if input_data[config.CATEGORICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.CATEGORICAL_NA_NOT_ALLOWED
        )

    # Valores <= 0 en las variables transformadas a logaritmo
    if (input_data[config.NUMERICALS_LOG_VARS] <= 0).any().any():
        vars_with_neg_values = config.NUMERICALS_LOG_VARS[
            (input_data[config.NUMERICALS_LOG_VARS] <= 0).any()
        ]
        validated_data = validated_data[validated_data[vars_with_neg_values] > 0]

    return validated_data
