import sys
from numpy import array
from math import sqrt
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.feature import HashingTF, IDF

entrada = sys.argv[1] # Carpeta de entrada donde estan los documentos
salida = sys.argv[2] # Carpeta de salida donde se van a guardar los resultados
k = int(sys.argv[3]) # Numero de clusters que se van a crear
iteraciones = 10000

if __name__ == "__main__":
    sc = SparkContext(appName="Practica4")  # Se inicia el contexto Spark
    documents = sc.wholeTextFiles(entrada) # Se obtiene los archivos del dataset como una pareja de (k,v )
    valores = documents.values().map(lambda line: line.split(" ")) # Se guardan en un arreglo las palabras de cada documento separadas por espacio
    nombre_archivos = documents.keys().collect() # se guarda el nombre de los archivos
    hashingTF = HashingTF() # Crea un objeto que va a ejecutar el hashing trick y la frecuencia de término
    tf = hashingTF.transform(valores) # Usa el objeto hash TF para aplicar la función hash con el fin de transformar palabras en su representación numérica y obtener la frecuencia de término
    idf = IDF(minDocFreq=5).fit(tf)  # Calcula el inverso para saber la importancia de las palabras en los documentos
    tfidf = idf.transform(tf) # Calcula la importancia según la frecuencia de las palabras en los documentos
    clusters_model = KMeans.train(tfidf, k, maxIterations=iteraciones) # Entrena el kmeans y calcula los centroides con el vector tfidf

    clusters = clusters_model.predict(tfidf).collect()  # Encuentra el clúster al que pertenece cada uno de los puntos en este modelo.

    resultado = {}

    for i in range(len(clusters)):
        if clusters[i] in resultado.keys():
            resultado[clusters[i]].append(nombre_archivos[i])  # Guarda los resultados en cada cluster
        else:
            resultado[clusters[i]]= [nombre_archivos[i]]

    resultado = sc.parallelize(resultado.items())
    resultado.coalesce(1).saveAsTextFile(salida)
    sc.stop()
