import configparser
from html import entities
import tweepy
import pandas as pd

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

# search tweets by keyword
keywords= 'ikea'
limit = 10
tweets = tweepy.Cursor(api.search_tweets, q='ikea -filter:retweets', count=100, tweet_mode='extended').items(limit)

# create DataFrame
columns = ['User ID', 'Tweet text','Created at','entities','geo']
data = []

for tweet in tweets:   
    data.append([tweet.user.screen_name, tweet.full_text, tweet.created_at, tweet.entities, tweet.geo])

df = pd.DataFrame(data, columns=columns)

print(df)
df.to_csv('dataquery.csv', encoding='utf-8')





