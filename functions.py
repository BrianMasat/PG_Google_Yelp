import findspark
findspark.init()
import pyspark
findspark.find()

import os
import pandas as pd
from functools import reduce
import pyspark
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS

# Configuramos Spark para poder procesar de forma local archivos de gran tamaño
conf = SparkConf().setAppName('appName').setMaster('local') \
    .set("spark.network.timeout", "600s") \
    .set("spark.driver.memory", "12g") \
    .set("spark.executor.memory", "10g") \
    .set("spark.executor.cores", "4") \
    .set("spark.dynamicAllocation.maxExecutors", "2")

sc = SparkContext(conf=conf)
spark = SparkSession(sc)

loaded_model = ALS.load("modelo_als")
business_names = pd.read_parquet("business_names.parquet")

def get_recommendations(user_id):
    user_df = spark.createDataFrame([(user_id,)], ["user_id_int"])
    user_recs = loaded_model.recommendForUserSubset(user_df, 10)
    a = user_recs.select("recommendations")
    rows = a.collect()
    recommendations_dict = {}
    for row in rows:
        recommendations_dict.update(dict(row.recommendations))

    keys = recommendations_dict.keys()
    top10_recs = business_names[business_names['business_id_int'].isin(keys)]['business_name'].tolist()
    names_list = top10_recs[:10]
    return names_list