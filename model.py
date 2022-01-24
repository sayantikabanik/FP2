import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Dump a ML model, therefore, we use a pickle format for this
import pickle
import matplotlib.pyplot as plt
from datetime import datetime
import statsmodels.api as sm
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
import imageio
import os
from statsmodels.graphics.tsaplots import plot_acf
# import statsmodels.api as sm

# df_result = pd.read_csv('products.csv')
# #print(df.head())
#
# mod = sm.OLS(exog=df_result[['Positive Tweets', 'Negative Tweets']], endog=df_result['Sales USD'])
# res = mod.fit()
#print(res.summary())

# X = df_result[['Positive Tweets','Negative Tweets']]
# y = df_result['Sales USD']
# pred_y = res.predict(X)

# print(y)
# print(pred_y)
# print(res.predict([122,4]))

# pickle.dump( res , open('final_model.pkl','wb') )
__model = pickle.load(open('model.pkl','rb'))

print(__model.predict(["Wheat","CEREALS",40.9,4,2021,1]))