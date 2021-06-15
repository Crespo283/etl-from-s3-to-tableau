from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from os.path import expanduser, join, abspath


def test_spark():

    spark = (
        SparkSession.builder.appName("pyspark-notebook")
        .master("local[*]")
        .config("spark.executor.memory", "512m")
        .getOrCreate()
    )
    df = spark.createDataFrame(
        [
            (1, "foo"),  # create your data here, be consistent in the types.
            (2, "bar"),
        ],
        ["id", "label"],  # add your column names here
    )
    print(df.show())