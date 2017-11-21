from __future__ import print_function
from numpy import array
from math import sqrt
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.feature import HashingTF, IDF

if __name__ == "__main__":
    k = 4  # Este indica el numero de centroides del kmeans
    sc = SparkContext(appName="TFIDFExample")  # Se inicia el contexto Spark
    documents = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/*.txt") # Se obtiene los archivos del datasets como una pareja de (k,v )
    valores = documents.values().map(lambda line: line.split(" ")) # Se guardan en un arreglo las palabras de cada documento separadas por espacio
    nombre_archivos = documents.keys().collect() # se guarda el nombre de los archivos
    hashingTF = HashingTF()
    tf = hashingTF.transform(valores) # Se calcula la frecuencia de cada palabra dentro de un documento Di
    idf = IDF().fit(tf)  # Calcula el inverso para saber la importancia de las palabras
    tfidf = idf.transform(tf) #
    clusters_model = KMeans.train(tfidf, 4, maxIterations=10) # Entrena el kmeans y calcula los centroides con el vector tfidf

    clusters = clusters_model.predict(tfidf).collect()  # Encuentra el clúster al que pertenece cada uno de los puntos en este modelo.

    resultado = {}

    for i in range(len(clusters)):
        if clusters[i] in resultado.keys():
            resultado[clusters[i]].append(nombre_archivos[i])
        else:
            resultado[clusters[i]]= [nombre_archivos[i]]

    resultado = sc.parallelize(resultado.items())
    resultado.coalesce(1).saveAsTextFile("hdfs:///user/sgalean7/archivos4")
    sc.stop()
