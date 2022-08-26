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

df = pd.read_csv('data/BTC-final.csv')
df_tweets = pd.read_csv('data/tweets_final.csv')



# df_tweets = df_tweets.loc[::-1].reset_index(drop=True) dont use this

print(len(df_tweets))
print(len(df))

df_new = df_tweets.loc[:, df_tweets.columns.drop(['_id', 'start','end'])]


df_new[['bit_coin_date', 'closing_price']] = df[['Date', 'Close']].to_numpy()

# print (df.head())
# print(df_tweets.head())

df_new = df_new.dropna(how='all')


X = df_new[['tweet_count']]
y = df_new['closing_price']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


regressor = LinearRegression()
regressor.fit(X_train, y_train)

#print the coefficients
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

# make prediction
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df.head())

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))



# print(pd.isnull(y_train))
# sys.exit()


# check the statistics
X2 = sm.add_constant(X_train)
est = sm.OLS(y_train.astype(float), X2)
est2 = est.fit()
print(est2.summary())


r2 = regressor.score(X_test, y_test)
print(r2)


#plot

X_train=X_train.squeeze()
y_train = y_train.to_numpy(dtype=float)
# print(X_train.shape)
# print(X_train.dtype)
# print(y_train.dtype)
# sys.exit()
plt.plot(X_train, y_train, 'o')
m, b = np.polyfit(X_train, y_train, 1)
plt.plot(y_train, m*X_train + b)

print(df_new.head())