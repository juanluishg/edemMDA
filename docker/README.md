# Docker

## From Dockerfile

- **FROM**: imagen desde la que parte
- **RUN**: comandos a ejecutar
- **EXPOSE**: puerto que abre internamente
- **CMD**: ejecuta y vuelca por pantalla

Para construir la imagen a partir de fichero:

`docker build -t nombre_imagen .`

Ejemplo:

<code>

FROM ubuntu

RUN apt-get update -y

CMD [ "bash" ]

</code>

## From image

Parametros:

- -i: mantener la entrada abierta aunque no esté "atada"
- -t: inicia un terminal
- -d: ejecutar en segundo plano (Detached)
- --name: nombre del contenedor
- -p: puertos

`docker run -itd --name nombre_contenedor -p puerto_externo:puerto_interno nombre_imagen`

Ejemplo:

`docker run -itd --name prueba -p 80:80 nginx`

## From docker-compose

Es un mecanismo para generar multiple contenedores(a partir de múltiples imagens) de manera sencilla.

El archivo siempre debe llamarse **docker-compose.yml** o **docker-compose.yaml**

Etiquetas:

- version: version del docker compose

- servicios: los contenedores

- image: la imagen para crear el contenedor

- ports: puertos

- enviroment: variables de entornos

- volumes: crea volúmenes

- restart: cuando docker arranque que arranque el contedor

##### Levantar los contenedores

`docker-compose up -d`

##### Parar los contenedores

`docker-compose down`



### Resumen Funciones 

`docker pull nombre_imagen` -> Descargar imagen

`docker run -itd --name nombre_contenedor -p puerto_externo:puerto_interno nombre_imagen` -> Ejecutar contenedor

`docker exec -it nombre_contenero funcion` -> Ejecutar funcion en el docker

`docker stop id_contenedor` -> Parar ejecucion contenedor

`docker start  id_contenedor` -> Iniciar contenedor ya creado previamente (con docker run)



## Ejericios de clase

### Demo 1

Dockerfile basico, en el que crea un contenedor a partir de una imagen de ubuntu de una version concreta, la cual(la versión) se almacena dentro de una variables



### Demo 2

Dockerfile basico, en el que crea un contenedor a partir de una imagen de ubuntu de una version concreta, instala algunos paquetes, crea una carpeta y declara varias variables de entorno.



### Demo 3

Dockerfile basico, en el que crea un contenedor a partir de una imagen de ubuntu, instala un servidor web usando nginx, abre el pueto 80 interno y copia un fichero html de la carpeta donde se ha ejecutado el docker(pc host) a la ruta especificada de dentro del docker. Por ultimo lanza nginx



### Docker Compose

Crea dos contenedores, uno para alojar un wordpress y otro para una base de datos mysql. Y les configura los parametros