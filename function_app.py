import azure.functions as func
#import pandas as pd
#import numpy
#import pyspark.pandas as ps
#from pyspark.sql import SparkSession


app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="req")

def main(req: func.HttpRequest) -> str:
    user = req.params.get("text")
    return f"Hello, {user}!"
    #return "Hello, man ok!"