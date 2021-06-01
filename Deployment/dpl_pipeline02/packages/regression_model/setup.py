# Este es "el corazón" de nuestra librería.
# Contiene los metadatos, dependencias y
# la función setup usada en "setuptools"
# para generar los archivos de distribución.


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dependencias
import io
import os
from pathlib import Path
from setuptools import find_packages, setup


# Meta-datos de la librería.
NAME = 'regression_model'
DESCRIPTION = 'Train and deploy regression model.'
URL = 'your github project'
EMAIL = 'your_email@email.com'
AUTHOR = 'Your name'
REQUIRES_PYTHON = '>=3.6.0'


# ¿Qué requerimientos son necesarios para que se ejecute el módulo?
# Esta función toma los requiermientos directamente del archivo
# requirements.txt
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))

# La "descripción larga" de la librería la podemos importar del archivo README.MD
# Si está disponible (si el archivo 'README.md' consta en el MANIFEST.in),
# que no es el caso.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Cargar la versión de la librería __version__.py como un diccionario.
# Actualiza la versión de la libería.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


# Setup de la librería, método importado de "setuptools".
	# Puede que os interese revisar qué son los "Trove Classifiers"
	# y para qué se usan aquí https://pypi.org/classifiers/
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'regression_model': ['VERSION']},
    install_requires=list_reqs(),
	# los tomará del archivo requirements.txt
	# en este punto se ve la importancia de trabajar con rangos de versiones
	# que no sean muy amplios (a nivel de patch o versión menor).
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Clasificadores Trove
        # Lista completa en: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
