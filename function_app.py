import azure.functions as func
#import logging 
import pandas as pd
import numpy
#import pyspark.pandas as ps
from pyspark.sql import SparkSession

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="req")

def main(req: func.HttpRequest) -> str:
    spark = SparkSession.builder.appName("Exemplo").getOrCreate()
    data = req.params.get("text")
    ref = spark.read.csv(data,header = True)
    return f"{print(ref.show())}"
    #return "Hello, man ok!"