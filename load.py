import pandas as pd
from sqlalchemy import create_engine
import json

cred = "credentials.json"
data = "nba_data.csv"


# loading credentials

with open(cred) as f:
    cred = json.load(f)


def load_data_dataframe(data):
    ''' loads data from local directory to the dataframe.
        insert those rows to a postgres database according to the
        credentials file'''
    df = pd.read_csv("nba_data.csv", header=None, sep=',')
    return df


def load_data_to_psql():
    engine = create_engine(cred["URL"])
    df = pd.read_csv("nba_data.csv", header=None, sep=r'\s{2,}', engine='python')
    df.to_sql("nba_data", engine)
    return True


load_data_to_psql()