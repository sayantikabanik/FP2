import pandas as pd
import numpy as np
from dagster import pipeline, solid, execute_pipeline
import requests
import datetime
import calendar

def clean_comm_name(COMM_NAME):
    try:
        return COMM_NAME.split('. ')[1]
    except:
        return COMM_NAME
@solid
def read_commodity_data_raw():
    df_commodity = pd.read_excel("Rawdata.xls")
    return df_commodity

@solid
def read_rainfall_data_raw():
    df_rainfall = pd.read_csv("Rainfall_2020.csv")
    return df_rainfall

@solid
def process_data(df, rainfall_df):
    rainfall_df['REGION'] = 'INDIA'
    # rainfall_df=historical_rainfall_df.append(latest_rainfall_df,ignore_index=True)
    rainfall_df = rainfall_df.drop(columns={'PARAMETER', 'ANN'})
    # Filling categories
    df['COMM_CATEGORY'] = pd.Series(np.where(df['COMM_CODE'].apply(lambda x: x % 100) == 0, df['COMM_NAME'], None)) \
        .apply(lambda x: clean_comm_name(x)) \
        .fillna(method='ffill')
    # Trimming data values
    df['COMM_CATEGORY'] = df['COMM_CATEGORY'].apply(lambda x: x.strip())
    # Dropping unnecessary columns
    dropped_df = df.drop(columns={'COMM_NAME', 'COMM_CODE', 'COMM_WT', 'COMM_CATEGORY'})
    # rainfall_df=rainfall_df.drop(columns={'ANNUAL','Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'})

    # Converting wide-format rainfall data into long format
    new_rainfall_df = pd.DataFrame()
    for col in rainfall_df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                            'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].columns:
        temp_df = rainfall_df[['REGION', 'YEAR']]
        temp_df['Rainfall'] = rainfall_df[col]
        temp_df['Month'] = col

        new_rainfall_df = new_rainfall_df.append(temp_df, ignore_index=True)
    # Adding date related columns
    new_rainfall_df['Month No'] = new_rainfall_df['Month'].apply(lambda x: datetime.datetime.strptime(x, '%b').month)
    new_rainfall_df['Day'] = 1
    new_rainfall_df['Date'] = pd.to_datetime(
        new_rainfall_df['Month No'].astype(str) + '-' + new_rainfall_df['Day'].astype(str) + '-' + new_rainfall_df[
            'YEAR'].astype(str))

    # Converting wide-format raw data into long-format
    new_df = pd.DataFrame()
    for col in dropped_df.columns:
        temp_df = df[['COMM_NAME', 'COMM_CODE', 'COMM_CATEGORY', 'COMM_WT']]
        temp_df['Monthly Price'] = df[col]
        temp_df['Date'] = col.split('INDX')[1]

        new_df = new_df.append(temp_df, ignore_index=True)
    # Adding date related columns
    new_df['Day'] = 1
    new_df['Month'] = new_df['Date'].apply(lambda x: x[:2])
    new_df['Year'] = new_df['Date'].apply(lambda x: x[2:])
    new_df['Month'] = new_df['Month'].astype(int)
    new_df['Year'] = new_df['Year'].astype(int)
    new_df['Date'] = pd.to_datetime(new_df[['Day', 'Month', 'Year']])

    # Filtering Celars, Pulses, Vegetables, Fruits etc. other required categories
    new_df = new_df[['Date', 'COMM_NAME', 'COMM_CODE', 'COMM_CATEGORY', 'COMM_WT', 'Monthly Price']]
    new_df = new_df[new_df['COMM_CATEGORY'].isin(
        ['CEREALS', 'PULSES', 'VEGETABLES', 'FRUITS', 'CONDIMENTS & SPICES', 'OTHER FOOD ARTICLES'])]
    new_df = new_df[~new_df['COMM_NAME'].isin(
        ['a1. CEREALS', 'a2. PULSES', 'b1. VEGETABLES', 'b2. FRUITS', 'e.  CONDIMENTS & SPICES',
         'f.  OTHER FOOD ARTICLES'])]

    # Combining Raw data and rainfall data
    new_df = new_df.merge(new_rainfall_df[['Date', 'Rainfall']], on='Date', how='left')
    new_df.to_excel('processed_data.xlsx', index=False)
    return new_df

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
    processed_data = process_data(commodity_data,rainfall_data)
    data_check(processed_data)
    test_cases(processed_data)


if __name__ == "__main__":
    result = execute_pipeline(data_pipeline)
