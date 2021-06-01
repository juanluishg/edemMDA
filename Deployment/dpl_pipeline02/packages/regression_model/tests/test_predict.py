# En este script tenemos dos funciones sencillas para
# comprobar que nuestra librería funciona correctamente.
# Los test serán ejecutados por tox.

# Estas son sólo dos funciones de ejemplo que comprueba
# que el valor/dimensión del resultado es correcto. Pero
# la idea es que implementéis los test que tengan sentido
# en vustro proyecto.


# Librerías y módulos para este script:
import math

# De la propia librería:
from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Dado
    test_data = load_dataset(file_name='test.csv') # los datos test.
    single_test_json = test_data[0:1].to_json(orient='records') # se selecciona una única fila

    # Cuando
    subject = make_prediction(input_data=single_test_json) # predecimos para ese valor

    # Entonces
    assert subject is not None # comprobamos que hay datos.
    assert isinstance(subject.get('predictions')[0], float) # deben ser de tipo "float" (números con decimales)
    assert math.ceil(subject.get('predictions')[0]) == 112476 # se redonde el resultado y se comprueba el valor.


def test_make_multiple_predictions():
    # Dado
    test_data = load_dataset(file_name='test.csv') # los datos test.
    original_data_length = len(test_data) # con todos los datos
    multiple_test_json = test_data.to_json(orient='records')

    # Cuando
    subject = make_prediction(input_data=multiple_test_json) # predecimos para el conjunto de valores

    # Entonces
    assert subject is not None # comprobamos que hay datos.
    assert len(subject.get('predictions')) == 1451 # se comprueba la longitud del resultado.

    # Esperamos que el objeto resultante tenga menos filas
	# al quedar filtradas.
    assert len(subject.get('predictions')) != original_data_length
