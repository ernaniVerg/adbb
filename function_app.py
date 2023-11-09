import azure.functions as func
import logging 
import pandas as pd
import numpy
import pyspark.pandas as ps
from pyspark.sql import SparkSession


#app = func.FunctionApp()
bp = func.Blueprint() 
#@app.function_name(name="HttpTrigger1")
#@app.route(route="req")
@bp.route(route="default_template")

def default_template(req: func.HttpRequest) -> func.HttpResponse: 
    logging.info('Python HTTP trigger function processed a request.') 

    name = req.params.get('text') 
    if not name: 
        try: 
            req_body = req.get_json() 
        except ValueError: 
            pass 
        else: 
            name = req_body.get('text') 

    if name: 
        return func.HttpResponse( 
            f"Hello, {name}. This HTTP-triggered function " 
            f"executed successfully.") 
    else: 
        return func.HttpResponse( 
            "This HTTP-triggered function executed successfully. " 
            "Pass a name in the query string or in the request body for a" 
            " personalized response.", 
            status_code=200 
        ) 