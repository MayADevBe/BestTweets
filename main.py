import tweepy
from datetime import datetime
from datetime import timedelta
import config

api = config.get_Api()

def get_most_liked(user, time):
    best_tweets = {}
    for tweet in api.user_timeline(screen_name=user, count=3):
        try:
            retweet = tweet.retweeted_status
            print("Tweet is a retweet")
        except:
            if tweet.created_at > time and tweet.retweeted == False:
                sum = tweet.retweet_count + tweet.favorite_count 
                try:
                    sum += tweet.reply_count
                except:
                    print("No Replys")
                try:
                    sum += tweet.quote_count
                except:
                    print("No Quotes")
                best_tweets[tweet.id] = sum
                print(tweet.id, tweet.text, sum)
    print(best_tweets)
time = datetime.now() - timedelta(days=365)
get_most_liked('MayADevBe', time)