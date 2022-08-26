# This script aims to count the total number of each cryptocurrencies mentioned in all tweets included in the CSV file
# To run this script, use the command on your terminal: python crypto_mapreduce.py crypto_count.csv
#
# Authors: Rafael Del Carmen, Mamata Shrestha

from mrjob.job import MRJob
from mrjob.step import MRStep
from pymongo import MongoClient


#Add or modify the list depending on which cryptocurrencies are relevant to be analyzed
crypto_list = ["bitcoin", "ethereum", "tether", "binance", "XRP", "cardano", "solano", "dogecoin"]
client = MongoClient('localhost', 27017)

# The purpose of this function is to make a db collection that holds the output of the mapreduce. This can be used for graphs
# def Add_to_trend_history_db(key, value):
#     try:
#         db = client.tweets
#         tweets_collection = db.trend_history
#         tweets_collection.insert_one({"name" : key, "mentions": value})
#     except:
#         print("unable to store into DB")


class Crypto_map_reduce(MRJob):

    #Mapper function 
    def mapper(self, _, line):
        for keyword in crypto_list:
            if keyword in line:
                yield keyword, 1
    #Reducer function
    def reducer(self, key, values):
        # Add_to_trend_history_db(key, sum(values))
        yield key, sum(values)

if __name__ == "__main__":
    Crypto_map_reduce.run()
