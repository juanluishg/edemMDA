# Tratamiento De Datos

- Jupyter Notebook
- Google Colab
- Zeeppeling

## Notebook

Características:

- El servidor que ejecuta el Notebook se llama Kernel
- Las variables son compartidas entre celdas
- Las variables se eliminan(de memoria) cuando se reinicia el Kernel
- Las celdas se pueden ejecutar independientemente y sin orden(¡OJO! si depende de una variable de otra celda no ejecutada, no funcionará)
- Los Notebooks puede ser multi-lenguajes



Aspectos importantes:

- Intercalar celdas de codigo con explicaciones
- Un notebook, un objetivo
- Un notebook no es un editor de código
- Mantener limpio el código
- Etiquetar diagramas

### Jupyter Notebook

Notebook que ser tanto [online](https://jupyter.org/try) como [on-premise](https://www.anaconda.com/). 

Es monolenguaje, solo admite python. También se pueden ejecutar comandos de Bash poniendo "!" antes del comando. 

Ejemplo:  `!ls -la`



### Google Colab

Notebook online y colaborativo que utiliza principalmente Google Drive como almacen de datos y de los propios notebooks.

Es monolenguaje, solo admite python. Además incluye varios fragmentos de codigo (Snippets) ya programado para ciertas funciones, y posee una gran documentación de proyectos ya hechos en [Colab](https://colab.research.google.com/).

Al igual que Jupyter, se pueden ejecutar comandos bash.

Google Colab permite escoger si queremos aumentar CPU, GPU o TPU, ya que por debajo se ejecuta sobre instancias libres de Google Cloud.



### Apache Zeppelin

Notebook on-premise. Nosotros lo utilizamos sobre docker:

- Debe existir la carpeta *logs* y *data* en la carpeta donde vayamos a ejecutar el docker. Si usamos el [repositorio de clase](https://github.com/a10pepo/edem2021/), debemos situarnos en *Sesiones/zeppelin/Exercise 0*.

- En *data* estarán los datsets que vayamos a utilizar

  `docker run -p 19999:8080  -v $PWD/logs:/zeppelin/logs -v $PWD/data:/zeppelin/data --rm --name zeppelin_single apache/zeppelin:0.8.1`

- Entramos en [localhost:19999](localhost:19999)

Zepplin es un notebook multi-lenguaje, que además permite mover celdas, redimensionarlas...

Para elegir el lenguaje a utilizar, en la primera linea de la celda debemos especificarlos con *%*. Ejemplo:

`%python`



## Ejercicios

#### JupyterNotebook.ipynb

Ejecicio para comprobar que si utilizamos los codigos ya escritos de google colab (Snippets) en jupyter probablemente fallen pues en nuestro ordenador no tenemos librerias que utiliza, que por defecto en colab estan instaladas. Se muestra ademas como instalar libreriaas(primera celda)



#### MiPrimerNotebook.ipynb

Notebook creado en Colab para probar distintos Snippets, y ver como se cargan datasets, se muestran en tablas, graficas...



#### SecondColab.ipynb

Probar mas Snippets



#### zeppelin/Amazon Analysis.json



