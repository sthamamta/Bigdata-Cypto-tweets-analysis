#This script is currently tested using this dataset: https://www.kaggle.com/datasets/fabioturazzi/cryptocurrency-tweets-with-sentiment-analysis by Fabio Turazzi

import pandas as pd
df = pd.read_csv("tweets_sentiment.csv")

#Get only relevant columns, such as tweet, negative, neutral, and positive columns
relevant_columns = df[['tweet','neg','neu','pos']]

#Get the column between neg,neu,pos and save them to a new column name 'max'
relevant_columns['max'] = relevant_columns[['neg','neu','pos']].idxmax(axis=1)

#Drop rows if the 'max' column is neutral. only need positive or negative
relevant_columns = relevant_columns[relevant_columns['max'] != 'neu']
print(relevant_columns['max'])

#convert 'max' column into numbers and save into a new column 'sentiment_value'
relevant_columns['sentiment_value'] = relevant_columns['max'].factorize()

# print(relevant_columns['max'].value_counts())

