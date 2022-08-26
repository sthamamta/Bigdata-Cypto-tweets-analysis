import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from sklearn import metrics
import statsmodels.api as sm
from scipy import stats
import sys


df = pd.read_csv('tweets_volume.csv')
print(df.head())

df_new = df.loc[:, df.columns.drop(['_id', 'start'])]
print(df_new.head())

df_new['end'] =pd.to_datetime(df_new.end)
df_new['end'] = df_new['end'].dt.date
df_new.sort_values(by='end')
# df_new.sort('end') 
print(df_new.head(20))

df_new.set_index('end').plot()
df_new.plot(x='end', y='tweet_count')

