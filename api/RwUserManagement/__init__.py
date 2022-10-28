import logging
import pyodbc
import pandas as pd
import azure.functions as func
import sys, os

def main(req: func.HttpRequest)->func.HttpResponse:

        try:
                logging.info('Triggered Get Employee python function.')

                id =int(req.route_params.get("id")) 
                logging.info('fetched id.')     

                cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=rewardsdbserver.database.windows.net;"
                        "Database=rewardsdbindia;"
                        "UID=rwadmin;"
                        "PWD=Monika150687;")
                
                cnxn = pyodbc.connect(cnxn_str)
                logging.info('Connected with database.')         

                # build up our query string
                query = ("SELECT * FROM EmpMaster WHERE EmpID = ?")
                # execute the query and read to a dataframe in Python
                data = pd.read_sql(query, cnxn,params=[id])

                logging.info('Retrived data.')        
        except Exception as e:
                logging.info(sys.exc_info())
                return func.HttpResponse(sys.exc_info(),status_code=500)

        return func.HttpResponse(
             data.to_json(orient="index",date_format='iso'),
             status_code=200
        )
