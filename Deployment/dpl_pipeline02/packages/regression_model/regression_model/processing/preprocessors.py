# En este secript tenemos definidas las funciones para 
# el pre-procesado de los datos. 
# Tenemos un conjunto de funciones que incluyen:
# Operaciones de preprocesamiento de los datos (ejemplo: eliminar NAs) 
# como tratamiento de las variables (ejemplo: recodificar variables categóricas).

	# La transformación logarítmica la llevamos a otro script: features.py
	# ya que es claramente una operación de tratamiento de las variables.
	# Se podría discutir que algunas funciones incluidas aquí deberían ir
	# en realidad al script features.py, pero el objetivo aquí es plantear
	# una estructura coherente de la librería. Podíes decidir redistribuir
	# el proceso en varios scritps, unificar alguno... siempre que mantengáis
	# la consistencia y las dependencias entre los scripts.

#Librerías y métodos necesarios en el script:
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# De la propia librería
from regression_model.processing.errors import InvalidModelInputError


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """Imputador de datos faltantes en variables categóricas."""

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> "CategoricalImputer":
        """Para ajustarse al formato pipeline de sklearn."""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Aplicar los transformadores a los datos."""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna("Missing")

        return X


class NumericalImputer(BaseEstimator, TransformerMixin):
    """Imputador de datos faltantes en variables numéricas."""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # Guardar en diccionario
        self.imputer_dict_ = {}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mode()[0]
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)
        return X


class TemporalVariableEstimator(BaseEstimator, TransformerMixin):
    """Variable temporal."""

    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        self.reference_variables = reference_variable

    def fit(self, X, y=None):
        # Para ajustarnos al formato pipeline, lo vimos en las sesiones.
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variables] - X[feature]

        return X


class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """Recodificador para etiquetas poco frecuentes en variables categóricas"""

    def __init__(self, tol=0.05, variables=None):
        self.tol = tol
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # guardar en diccionario
        self.encoder_dict_ = {}

        for var in self.variables:
            # Las categorías más frecuentes en los datos.
            t = pd.Series(X[var].value_counts() / np.float(len(X)))
            # Etiquetas frecuentes:
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(
                X[feature].isin(self.encoder_dict_[feature]), X[feature], "Rare"
            )

        return X


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """Recodifica categorías, pasando los niveles de caracter a número."""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ["target"]

        # guardar en diccionario
        self.encoder_dict_ = {}

        for var in self.variables:
            t = temp.groupby([var])["target"].mean().sort_values(ascending=True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t, 0)}

        return self

    def transform(self, X):
        # codifica etiquetas
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])

        # comprueba si el transformador introduce NaN
        if X[self.variables].isnull().any().any():
            null_counts = X[self.variables].isnull().any()
            vars_ = {
                key: value for (key, value) in null_counts.items() if value is True
            }
            raise InvalidModelInputError(
                f"Categorical encoder has introduced NaN when "
                f"transforming categorical variables: {vars_.keys()}"
            )

        return X


class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # codificar etiquetas
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X
