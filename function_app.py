import azure.functions as func
#import logging 
import pandas as pd
import numpy
#import pyspark.pandas as ps
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from urllib.request import urlretrieve

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="req")

def main(req: func.HttpRequest) -> str:
    spark = SparkSession.builder.appName("Exemplo").getOrCreate()
    url = req.params.get("text")
    filename = "data.zip"
    path, headers = urlretrieve(url, filename)
    ref = spark.read.csv(path,header = True)
    return ref.show()
    #return "Hello, man ok!"