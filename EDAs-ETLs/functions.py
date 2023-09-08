import pandas as pd
import findspark
findspark.init()
import pyspark
findspark.find()

import os
from functools import reduce
import pyspark
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALSModel

conf = SparkConf().setAppName('appName').setMaster('local') \
    .set("spark.network.timeout", "600s") \
    .set("spark.driver.memory", "12g") \
    .set("spark.executor.memory", "10g") \
    .set("spark.executor.cores", "4") \
    .set("spark.dynamicAllocation.maxExecutors", "2")

sc = SparkContext(conf=conf)
spark = SparkSession(sc)

loaded_model = ALSModel.load("modelo_als")

def get_recommendations(user_id):
    user_df = spark.createDataFrame([(user_id,)], ["user_id_int"])

    user_recs = loaded_model.recommendForUserSubset(user_df, 10)

    user_recs_pandas = user_recs.toPandas()

    recommendations_dict = {}
    for row in user_recs_pandas.itertuples():
        user_id = row.user_id_int
        recommendations = [(int(rec.business_id), float(rec.rating)) for rec in row.recommendations]
        recommendations_dict[user_id] = recommendations

    return recommendations_dict