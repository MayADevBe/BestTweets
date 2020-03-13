import tweepy
import time
import config

api = config.get_Api()

def get_most_liked(time, user):
    for tweet in api.user_timeline(screen_name=user).items(1):
        print(tweet)