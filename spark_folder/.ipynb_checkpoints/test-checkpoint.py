from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("pyspark-run1")
    .master("spark://spark-master:7077")
    .config("spark.executor.memory", "512m")
    .getOrCreate()
)

data = spark.read.csv(path="data/uk-macroeconomic-data.csv", sep=",", header=True)

print(data.show(5))