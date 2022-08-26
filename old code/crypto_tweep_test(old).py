# This script collects tweets and saves it to a local mongoDB database. 
# IMPORTANT_NOTE: Modify the keys and tokens and use your keys and tokens.
# Authors: Rafael Del Carmen, Mamatha Shrestha
import collections
from bson.code import Code
from re import RegexFlag
import tweepy
from tweepy import Stream
from pymongo import MongoClient
from tweepy import Stream
from tweepy import OAuthHandler
import json
import datetime

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

cryptoList = ["bitcoin", "ethereum", "tether", "binance", "XRP", "cardano", "solano", "dogecoin"]
client = MongoClient('localhost', 27017)


class listener(Stream):
    def on_status(self, status):
        # print(status.text)
        try:
            db = client.tweets
            tweets_collection = db.tweets_collection
            tweets_collection.insert_one({"text" : str(status.text), "date" : str(status.created_at)})
            print("insert success ")
        except:
            print("fail to insert into db")
    def on_error(self, status_code):
        if status_code == 420:
            print("error 420: disconnecting the stream")
            return False
        else:
            print("Error: %s", status_code)

cryptoStream = listener(consumer_key, consumer_secret, access_token,access_token_secret)
cryptoStream.filter(track=cryptoList)
