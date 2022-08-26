# This script collects tweets and saves it to a local mongoDB database. 
# IMPORTANT_NOTE: Modify the keys and tokens and use your keys and tokens.
# Authors: Rafael Del Carmen, Mamata Shrestha
from ast import Try
import collections
from crypt import crypt
from bson.code import Code
from re import RegexFlag
from pandas import to_datetime
import tweepy
from tweepy import Stream
from pymongo import MongoClient
from tweepy import OAuthHandler
import json
import datetime

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

client = MongoClient('localhost', 27017)
start_date = '2022-01-01T00:00:00Z'
end_date = '2022-04-29T00:00:00Z'

auth = tweepy.OAuthHandler(
            consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# api = tweepy.API(auth)
# if api.verify_credentials:
#     print('success authentication')
# else:
#     print("authentication error")


# try:
#     for page in tweepy.Cursor(api.search_30_day, label="bigdata30",query="bitcoin").pages(1):
#         tweets = []
#         db = client.tweets
#         tweets_collection = db.tweets_collection
#         for tweet in page:
#             text=tweet.text
#             date=tweet.created_at
#             tweets.append({"text" : str(text), "date" : str(date)})
#         tweets_collection.insert_many(tweets)
# except tweepy.TweepyException as e:
#     print(e)
#     print("query failed")
try:
    twitter_client = tweepy.Client(bearer_token="",consumer_secret="", consumer_key="")
    print('success authentication')
except tweepy.TweepyException as e:
    print(e)
    print("authentication error")
    
try:
    db = client.tweets
    crypto_count_collection = db.crypto_count
    for response in tweepy.Paginator(twitter_client.get_all_tweets_count,query="bitcoin", end_time=end_date, granularity="day", start_time=start_date, limit=4):
        crypto_count_collection.insert_many(response.data)
except tweepy.TweepyException as e:
    print(e)

try:
    db = client.tweets
    tweets_collection = db.tweets_collection
    tweets = []
    for response in tweepy.Paginator(twitter_client.search_all_tweets,query="bitcoin",tweet_fields=['text', 'created_at'],end_time=end_date,max_results=500,start_time=start_date, limit=100):
        for tweet in response[0]:
            text=tweet.text
            date=tweet.created_at
            tweets_collection.insert_one({"text" : str(text), "date" : str(date)})
except tweepy.HTTPException as e:
    print(e)
    print("query failed")

print("done")
