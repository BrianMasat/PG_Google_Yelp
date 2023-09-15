from pyspark.sql import functions as F
from pyspark.ml.recommendation import ALSModel
import pandas as pd

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.8-bin-hadoop2.7"
import findspark
findspark.init()
import pyspark

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = pyspark.SparkContext('local[*]')

spark = SparkSession.builder.master("local").getOrCreate()

loaded_model = ALSModel.load("modelo_als")
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