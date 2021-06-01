# En este scipt incluiríamos todas las funciones
# relacionadas con el tratamiento y transformación de variables.
# La línea que separa las operaciones de "preprocessing" y 
# de transoformación de variables o "feature engineering"
# es algo difusa por lo que muchos procesos que podrían considerarse
# de transformación se han incluido en preprocessors.py.

# Aquí se describe la función para la 
# transformación logarítmica que vimos en el
# código durante las sesiones y que es, claramente
# una operación de "feature engineering".


# Librerías y métodos necesarios en este script:
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# Métodos definidos en la propia librería:
from regression_model.processing.errors import InvalidModelInputError


class LogTransformer(BaseEstimator, TransformerMixin):
    """Transformador logarítmico."""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # para ajustarse a la estructura propia
		# del pipeline en Python (comentado en las sesiones)
        return self

    def transform(self, X):
        X = X.copy()

        # comprueba que los valores no sean negativos
        if not (X[self.variables] > 0).all().all():
            vars_ = self.variables[(X[self.variables] <= 0).any()]
            raise InvalidModelInputError(
                f"Variables contain zero or negative values, "
                f"can't apply log for vars: {vars_}"
            )

        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X
