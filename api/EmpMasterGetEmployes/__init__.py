import logging
import pyodbc
import pandas as pd
import azure.functions as func

def main(req: func.HttpRequest)->func.HttpResponse:
    logging.info('Triggered Get Employee python function.')
    dbconString=""
    cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=rewardsdbserver.database.windows.net;"
            "Database=rewardsdbindia;"
            "UID=rwadmin;"
            "PWD=Monika150687;")
    cnxn = pyodbc.connect(cnxn_str)
    # build up our query string
    query = ("SELECT * FROM EmpMaster")

    # execute the query and read to a dataframe in Python
    data = pd.read_sql(query, cnxn)
    return func.HttpResponse(
             data.to_json(orient="index",date_format='iso'),
             status_code=200
        )
