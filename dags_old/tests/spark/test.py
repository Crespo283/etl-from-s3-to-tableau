from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from os.path import expanduser, join, abspath


# warehouse_location = abspath("spark-warehouse")

sparkConf = SparkConf()
sparkConf.setMaster("spark://spark-master:7077")
sparkConf.setAppName("pyspark-4")
# sparkConf.set("spark.executor.memory", "2g")
# sparkConf.set("spark.driver.memory", "2g")
# sparkConf.set("spark.executor.cores", "1")
# sparkConf.set("spark.driver.cores", "1")
# sparkConf.set("spark.dynamicAllocation.enabled", "false")
# sparkConf.set("spark.shuffle.service.enabled", "false")
# sparkConf.set("spark.sql.warehouse.dir", warehouse_location)
spark = SparkSession.builder.config(conf=sparkConf).getOrCreate()
sc = spark.sparkContext

# data = spark.read.csv(
#     path="dags/data/uk-macroeconomic-data.csv", sep=",", header=True
# )

print("ESTOY AQUI¿¿")
df = spark.createDataFrame(
    [
        (1, "foo"),  # create your data here, be consistent in the types.
        (2, "bar"),
    ],
    ["id", "label"],  # add your column names here
)
print(df.show())