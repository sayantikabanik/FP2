import pandas as pd
import numpy as np
from dagster import pipeline, solid, execute_pipeline
from forecasting_framework.utils.pre_processing import pre_process


@solid
def read_commodity_data_raw():
    df_commodity = pd.read_excel("forecasting_framework/data/Rawdata.xls")
    return df_commodity


@solid
def read_rainfall_data_raw():
    df_rainfall = pd.read_csv("forecasting_framework/data/Rainfall_2020.csv")
    return df_rainfall


@solid
def process_data(df, rainfall_df):
    final_df = pre_process(df, rainfall_df)
    final_df.to_excel('processed_data.xlsx', index=False)
    return final_df


@solid
def data_check(context, processed_df):
    mean_rainfall = processed_df['Rainfall'].mean()
    total_commodities = processed_df['COMM_NAME'].value_counts()
    total_category = processed_df['COMM_CATEGORY'].value_counts()
    context.log.info(f"mean_rainfall: {mean_rainfall}")
    context.log.info(f"total_commodities: {total_commodities}")
    context.log.info(f"total_category: {total_category}")


@solid
def test_cases(processed_df):
    isinstance(processed_df['Date'], pd.datetime)
    isinstance(processed_df['COMM_NAME'], object)
    isinstance(processed_df['COMM_CODE'], int)
    isinstance(processed_df['COMM_CATEGORY'], object)
    isinstance(processed_df['COMM_WT'], float)
    isinstance(processed_df['Monthly Price'], float)
    isinstance(processed_df['Rainfall'], float)


@pipeline
def data_pipeline():
    commodity_data = read_commodity_data_raw()
    rainfall_data = read_rainfall_data_raw()
    processed_data = process_data(commodity_data, rainfall_data)
    data_check(processed_data)
    test_cases(processed_data)


if __name__ == "__main__":
    result = execute_pipeline(data_pipeline)
