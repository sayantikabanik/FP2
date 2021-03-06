# Importing required libraries
import os
import numpy as np
import pandas as pd
import datetime


def clean_comm_name(COMM_NAME):
    try:
        return COMM_NAME.split('. ')[1]
    except:
        return COMM_NAME


def pre_process(df, rainfall_df):
    """
    :param df: commodity raw df
    :param rainfall_df: rainfall raw df
    :return:  combined processed dataframe
    """
    rainfall_df['REGION']='INDIA'
    rainfall_df=rainfall_df.drop(columns={'PARAMETER','ANN'})
    df['COMM_CATEGORY']=pd.Series(np.where(df['COMM_CODE'].apply(lambda x:x%100)==0,df['COMM_NAME'],None))\
                                                            .apply(lambda x:clean_comm_name(x))\
                                                            .fillna(method='ffill')
    df['COMM_CATEGORY']=df['COMM_CATEGORY'].apply(lambda x:x.strip())
    dropped_df=df.drop(columns={'COMM_NAME', 'COMM_CODE', 'COMM_WT','COMM_CATEGORY'})
    # Converting wide-format rainfall data into long format
    new_rainfall_df=pd.DataFrame()
    for col in rainfall_df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
           'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].columns:
        temp_df=rainfall_df[['REGION', 'YEAR']]
        temp_df['Rainfall']=rainfall_df[col]
        temp_df['Month']=col

        new_rainfall_df=new_rainfall_df.append(temp_df,ignore_index=True)
    # Adding date related columns
    new_rainfall_df['Month No']=new_rainfall_df['Month'].apply(lambda x:datetime.datetime.strptime(x, '%b').month)
    new_rainfall_df['Day']=1
    new_rainfall_df['Date']=pd.to_datetime(new_rainfall_df['Month No'].astype(str)+'-'+new_rainfall_df['Day'].astype(str)+'-'+new_rainfall_df['YEAR'].astype(str))

    # Converting wide-format raw data into long-format
    new_df=pd.DataFrame()
    for col in dropped_df.columns:
        temp_df=df[['COMM_NAME','COMM_CODE','COMM_CATEGORY','COMM_WT']]
        temp_df['Monthly Price']=df[col]
        temp_df['Date']=col.split('INDX')[1]

        new_df=new_df.append(temp_df,ignore_index=True)
    # Adding date related columns
    new_df['Day']=1
    new_df['Month']=new_df['Date'].apply(lambda x:x[:2])
    new_df['Year']=new_df['Date'].apply(lambda x:x[2:])
    new_df['Month']=new_df['Month'].astype(int)
    new_df['Year']=new_df['Year'].astype(int)
    new_df['Date']=pd.to_datetime(new_df[['Day','Month','Year']])

    # Filtering Celars, Pulses, Vegetables, Fruits etc. other required categories
    new_df=new_df[['Date','COMM_NAME', 'COMM_CODE', 'COMM_CATEGORY', 'COMM_WT', 'Monthly Price']]
    new_df=new_df[new_df['COMM_CATEGORY'].isin(['CEREALS', 'PULSES','VEGETABLES', 'FRUITS','CONDIMENTS & SPICES','OTHER FOOD ARTICLES'])]
    new_df=new_df[~new_df['COMM_NAME'].isin(['a1. CEREALS','a2. PULSES', 'b1. VEGETABLES','b2. FRUITS','e.  CONDIMENTS & SPICES','f.  OTHER FOOD ARTICLES'])]

    # Combining Raw data and rainfall data
    new_df = new_df.merge(new_rainfall_df[['Date','Rainfall']], on='Date',how='left')
    return new_df

