from data_preprocess import *
import pandas as pd
import matplotlib.pyplot as plt



# text = 'I am feeling very bad today'
# result = identify_sentiment(text)
# print(result[0])


# df_crypto =  pd.read_csv('tweets_with_dates.csv')

# df_crypto['text']= df_crypto['text'].apply(lambda x:prepare_text(x))

# df_crypto.drop(['_id'], axis=1,inplace=True)

# df_crypto['sentiment']= df_crypto['text'].apply(lambda x:identify_sentiment(x))
# print(df_crypto.head())


# print(df_crypto['sentiment'].sum()/len(df_crypto))  # percentage of positive tweets

# from pathlib import Path  
# filepath = Path('sentiment_tweets.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df_crypto.to_csv(filepath)  
# print('file saved')


df_tweet =  pd.read_csv('tweets_may122021.csv')

df_tweet['text']= df_tweet['text'].apply(lambda x:prepare_text(x))

df_tweet.drop(['_id'], axis=1,inplace=True)

# df_tweet['sentiment']= df_tweet['text'].apply(lambda x:identify_sentiment(x))
# print(df_tweet.head())

polarity = 0
positive = 0
wpositive = 0
spositive = 0
negative = 0
wnegative = 0
snegative = 0
neutral = 0

for index, row in df_tweet.iterrows():
    analysis = TextBlob(row['text'])
    # print(analysis.sentiment)  # print tweet's polarity
    polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

    if (analysis.sentiment.polarity == 0):  # adding reaction to find average later
        neutral += 1
    elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
        wpositive += 1
    elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
        positive += 1
    elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
        spositive += 1
    elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
        wnegative += 1
    elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
        negative += 1
    elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
        snegative += 1

plot_list=[spositive,positive,wpositive,neutral,wnegative,negative,snegative]
labels=['strong positive','positive','wpositive','neutral','weak negative','negative','strong negative']

plt.bar(labels, plot_list, align='center')
plt.xticks(rotation = 45)

# plt.xticks(labels) #Replace default x-ticks with xs, then replace xs with labels
# plt.yticks(ys)

plt.savefig('netscore.png')
plt.show()