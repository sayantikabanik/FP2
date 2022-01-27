

import pandas as pd
import csv
import requests



import pandas as pd
import csv
from dagster import op,execute_pipeline,pipeline
import requests

@op
def read_weather_data():
    df_sample = pd.read_excel("FPData v1.2.xlsx")
    return df_sample


@pipeline
def data_pipeline():
    sample = read_weather_data()


if __name__ == "__main__":
    result = execute_pipeline(data_pipeline)
