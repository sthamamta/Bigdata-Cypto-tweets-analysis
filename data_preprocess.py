#imports
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
import string
string.punctuation


from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer

nltk.download('stopwords')


# stop_words = set(stopwords.words('english'))
stop_words = set(stopwords.words('english')) - set(['not','but'])


import warnings
warnings.filterwarnings('ignore')


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 
from textblob import TextBlob

def preprocess_text(text,remove_stop_words=True, lemmatize_words=False):
    text = str(text)
    text = text.lower()

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ", text)
    text = re.sub(r"\+", " ", text)
    text = re.sub(r"\-", " ", text)
    text = re.sub(r"\=", " ", text)
    text = re.sub(r"\#", " ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(" \d+", " ", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = text.replace("\n", " ")
    text = "".join([i for i in text if i not in string.punctuation])
    
     # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
#     Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        stem_text = [stemmer.stem(w) for w in text]
#         lemmatized_words = [lemmatizer.lemmatize(word) for word in stem_text]
        text = " ".join(stem_text)


    return text


def remove_url(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)

def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree


def prepare_text(text):
    text = remove_punctuation(text)
    text = remove_url(text)
    text = preprocess_text(text)
    return text

def identify_sentiment(text):
    text = prepare_text(text)
    result = TextBlob(text).sentiment
    if(result[0]<0.2):
        return 0
    else:
        return 1
    # try:
    #     return TextBlob(text).sentiment
    # except:
    #     return None
