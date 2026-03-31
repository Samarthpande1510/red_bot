import tweepy
import tkinter as tk
from tkinter import messagebox


consumer_key = 'nUsIgviIICH4SRWxIjkYdCoMF'
consumer_secret = 'mAZwwp9qIjGLIiS3Ltre2872Y6VAeKgc4Y0YHS2FrXFiASrABm'
access_token = '1468028219869646848-gOqPmYGNS0kwriumoUjmf0PLe57qWF'
access_token_secret = 'tlDHfpYQrAuScwQnhnsUGTpOjoiEk8XkdUTyILcJVIFKx'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth) # <--- THIS LINE IS LIKELY MISSING OR MISSPELLED

# 3. Your search logic
search_term = "cats"
numberOfTweets = 2

# Now 'api' exists and the Cursor can find it
for tweet in tweepy.Cursor(api.search_tweets, q=search_term).items(numberOfTweets):
    try:
        tweet.retweet()
        print("Retweeted!")
    except Exception as e:
        print(e)
