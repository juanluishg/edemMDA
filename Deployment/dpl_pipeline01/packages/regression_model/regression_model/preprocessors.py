import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """Imputa datos faltantes en variables categóricas."""

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'CategoricalImputer':
        """Para ajustarse a las convenciones de sklearn."""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Aplica las transformaciones a."""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X
