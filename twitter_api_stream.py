import configparser
from html import entities
import tweepy
import pandas as pd
from datetime import datetime,timedelta
from time import time, sleep
import datetime
import pytz
while True:
    sleep(60 - time() % 60)
    # read config
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']

    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    # authenticate
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Define time stream call
    utc=pytz.UTC
    initialtime = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) - timedelta(minutes = 1)
    print(initialtime)


    # search tweets by keyword
    keywords= ['ikea', ' ']
    limit = 10
    tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)


    # create DataFrame
    columns = ['User ID', 'Tweet text','Created at','entities','geo']
    data = []
    for tweet in tweets:   
        if tweet.created_at>=initialtime :
            data.append([tweet.user.screen_name, tweet.full_text, tweet.created_at, tweet.entities, tweet.geo])
    df = pd.DataFrame(data, columns=columns)

    print(df)
    df.to_csv('dataqueryminute.csv', mode='a',header=False)






