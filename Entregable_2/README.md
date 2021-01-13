# Entregable 2

Usando nifi+ELK debéis presentar una solución que muestre sobre un mapa la disposición de delitos presentes en esta api:

 

https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9



### Requisitos

* ElasticSearch (9200, 9300)
* Kibana (5601)
* Nifi (8080)



### Pasos

**Levantar docker**

Dentro de la carpeta docker: 

`docker-compose up -d`

**Configurar Nifi**

Componetes usados:

* InvokeHttp

<img src="./images/invokehttp.PNG"/>

* SplitJSON

<img src="./images/splitjson.PNG"/>

* JoltTransformJSON

<img src="./images/jolt.PNG"/>

```
[{
	"operation": "modify-overwrite-beta",
	"spec": {
		"location": {
			"latitude": "=toDouble",
			"longitude": "=toDouble"
		}
	}
}, {
	"operation": "shift",
	"spec": {
		"*": "&",
		"location": {
			"latitude": "location.lat",
			"longitude": "location.lon"
		}
	}
}]
```

* PutElasticsearchHttp

<img src="./images/elastic.PNG"/>

*Elasticsearch URL: http://elasticsearch:9200*

*Index: newyork (nombre del indice)*

*Type: _doc*

*Index Operation: index*

**Resumen Nifi**

<img src="./images/nifi.PNG"/>

**Comprobar los indices**

Dentro de [Kibana](http://localhost:5601) en Management -> Index Management

Comprobamos que se ha creado el índice y están los documentos

**Reindexar**

Para conseguir que "location" sea de tipo "geo_point" hay que crear un nuevo índice con este tipo y acumular en este los documentos.

Desde Kibana -> DevTools:

```
PUT /crimes_re
{
  "mappings" : {
    "properties": {
      "location": {
        "type": "geo_point"
      }
    }
  }
}
POST _reindex
{
  "source": {
    "index": "crimes"
  },
  "dest": {
    "index": "crimes_re"
  }
}
```



**Visualizar los datos**

Desde Kibana -> Visualize, creamos uno nuevo (Create new visualization) y seleccionamos Coordinate Map

<img src="./images/visualize.PNG"/>



**Resultado final**

Desde Kibana -> Dashborard, creamos un dashboard (Create new dashboard) y añadimos las visualizaciones

<img src="./images/dashboard.PNG"/>



### Extra

Repetir el proceso anterior.

**Visualizar los datos conjuntos**

En el apartado Maps de [Kibana](http://localhost:5601) creamos un nuevo mapa y añadimos una capa por cada indice(ciudad).

Pulsamos sobre "Add Layer" y como fuente seleccionamos "Documents", seleccionamos el índice que queramos añadir y por ultimo pulsamos en Add layer.

Repetimos este paso por cada índice(ciudad) que queramos añadir.

Por últimos, pulsamos en "Save" antes de salir

<img src="./images/maps.PNG"/>