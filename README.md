# PracticaBigdata
Proyecto4 de la materia Tópicos Especiales en Telemática. 

# Autores:

Pablo Quijano - pquijano@eafit.edu.co

Sebastian Galeano - sgalean7@eafit.edu.co

# Introducción:

El Proyecto4 de la materia Tópicos Especiales en Telemática consistió en diseñar e implementar una aplicación con tecnología y modelo de programación distribuida en Big Data, específicamente con tecnología Hadoop y Spark que permitiera agrupar (clustering) un conjunto de documentos utilizando el algoritmo de k–means y una métrica de similaridad entre documentos.

# Algoritmos empleados y solución:

Básicamente se emplearon 2 algoritmos, el kMeans para agupar los documentos, y el TF-IDF para medir la similaridad entre estos; al jaccard le pasamos las 10 palabras más repetidas por documento, sin tener en cuenta las "Stopwords" que son un conjunto de palabras que no sirven para saber de que trata un documento (Ej: the, it, why, else ...); despues se usa lo que devuelve el tf-idf en el algoritmo de Kmeans dando como resultado el numero de clusters deseados con los documentos agrupados.

# A continuación se explica el funcionamiento de cada uno.

## TF-IDF
La frecuencia de los documentos - frecuencia inversa de los términos (TF-IDF) es un método de vectorización de características ampliamente utilizado en la minería de textos para reflejar la importancia de un término a un documento en el cuerpo. Denote un término por tt, un documento por dd, y el cuerpo por DD. La frecuencia de términos TF (t, d) es el número de veces que aparece el término tt en el documento dd, mientras que la frecuencia de los documentos DF (t, D) DF es el número de documentos que contiene el término tt. Si solo usamos la frecuencia de los términos para medir la importancia, es muy fácil enfatizar demasiado términos que aparecen muy a menudo pero que contienen poca información sobre el documento, por ejemplo, "A", "el" y "de". Si un término aparece muy a menudo en el cuerpo, significa que no contiene información especial sobre un documento en particular.

## K-means:

El algoritmo K-means es uno de los algoritmos de aprendizaje no supervisado más simples para resolver el problema de la clusterización. El procedimiento aproxima por etapas sucesivas un cierto número (prefijado) de clusters haciendo uso de los centroides de los puntos que deben representar.
El algoritmo se compone de los siguientes pasos:

-Sitúa KK puntos en el espacio en el que "viven" los objetos que se quieren clasificar. Estos puntos representan los centroides iniciales de los grupos.

-Asigna cada objeto al grupo que tiene el centroide más cercano.

-Tras haber asignado todos los objetos, recalcula las posiciones de los KK centroides.

-Repite los pasos 2 y 3 hasta que los centroides se mantengan estables. Esto produce una clasificación de los objetos en grupos que permite dar una métrica entre ellos.

-Este algoritmo de Kmeans fue realizado luego del entedimiento y analisis de varias paginas donde se mostraban ejemplos de este.


# Ejecución programas:

Para correr el programa, se debe ejecutar el siguiente comando: spark-submit --master yarn --deploy-mode cluster --executor-memory 2G --num-executors 4 Practica4.py


# Aportes Externos:
El algoritmo de Jaccard fue sacado de la siguiente pagina:
http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/

# Resultado del programa

Cuando finaliza el programa imprime cada cluster con sus respectivos documentos.


# Bibliografía:

https://www.gutenberg.org/

https://goo.gl/LL4CgA

http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/

https://es.wikipedia.org/wiki/%C3%8Dndice_Jaccard

http://www.cs.us.es/~fsancho/?e=43

