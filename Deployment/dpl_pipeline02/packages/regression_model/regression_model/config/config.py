# Este scritp contiene variables que se utilizan a lo largo
# de las distintas funciones como son
# las rutas a los distintos elementos y
# listas de variables a procesar.

# Durante las seseiones comentamos que cuando orientamos nuestra
# programación a objetos podemos simplificar el archivo de configuració
# ya que parte de las variables que necesita la librería para funcionar
# se obtienen de los propios datos/objetos manejados.


# Librerís y módulos para este script:
import pathlib
	# Object-oriented filesystem paths
	# https://docs.python.org/3/library/pathlib.html
import pandas as pd
	# pandas tiene un sistema de opciones que permite 
	# personalizar algunos aspectos de su comportamiento como
	# ajustes para la visualización. Aquí establecemos
	# número máximo de filas/columnas

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
	
# La librería
import regression_model


# Establecer las rutas:
PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
	# Al subdirectorio regression_model.
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
	# Al modelo una vez está entrenado.
DATASET_DIR = PACKAGE_ROOT / "datasets"
	# A los datos


# Datos:
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "SalePrice"


# A partir de aquí tenemos un código muy similar al que vimos en las sesiones:

	# La lista del variables para el procesmiento y el entrenamiento
FEATURES = [
    "MSSubClass",
    "MSZoning",
    "Neighborhood",
    "OverallQual",
    "OverallCond",
    "YearRemodAdd",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "1stFlrSF",
    "GrLivArea",
    "BsmtFullBath",
    "KitchenQual",
    "Fireplaces",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageCars",
    "PavedDrive",
    "LotFrontage",
    # Sólo usamos YrSols para obtener las variables
	# que hemos llamado temporales (explicado en las sesiones).
    "YrSold",
]

# Podrá descartarse tras ser utilizada.
DROP_FEATURES = "YrSold"

# Variables numéricas con NA en el set de entrenamiento
NUMERICAL_VARS_WITH_NA = ["LotFrontage"]

# Variables categóricas con NA en el set de entrenamiento
CATEGORICAL_VARS_WITH_NA = [
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
]

# Variable temporal calculada a partir de YrSold.
TEMPORAL_VARS = "YearRemodAdd"

# Variables para hacer la transformación logarítmica
NUMERICALS_LOG_VARS = ["LotFrontage", "1stFlrSF", "GrLivArea"]

# Variables categóricas a codificar
CATEGORICAL_VARS = [
    "MSZoning",
    "Neighborhood",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "KitchenQual",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "PavedDrive",
]

# Controles en los datos de entrada (para poder controlar que no
# se introduzcan NAs no detectados en el preprocesado de datos.
NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]

# Le damos un nombre al pipeline y lo guardamos.
PIPELINE_NAME = "lasso_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# Para evaluar el modelo (differential testing)
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
