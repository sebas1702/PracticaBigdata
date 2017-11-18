from __future__ import print_function
from numpy import array
from math import sqrt
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.feature import HashingTF, IDF

if __name__ == "__main__":
    sc = SparkContext(appName="TFIDFExample")  # SparkContext

    documents = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/19*.txt")
    valores = documents.values().map(lambda line: line.split(" "))
    nombre_archivos = documents.keys().collect()
    hashingTF = HashingTF()
    tf = hashingTF.transform(valores)
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)
    clusters_model = KMeans.train(tfidf, 3, maxIterations=10)
    clusters = clusters_model.predict(tfidf).collect()

    resultado = {}

    for i in range(len(clusters)):
        if clusters[i] in resultado.keys():
            resultado[clusters[i]].append(nombre_archivos[i])
        else:
            resultado[clusters[i]]= [nombre_archivos[i]]

    resultado = sc.parallelize(resultado.items())
    resultado.coalesce(1).saveAsTextFile("hdfs:///user/sgalean7/archivos2")
    sc.stop()
