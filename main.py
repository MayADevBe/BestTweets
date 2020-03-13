import tweepy
from datetime import datetime
from datetime import timedelta
import config

api = config.get_Api()

def get_most_liked(user, time):
    best_tweets = {}
    for tweet in api.user_timeline(screen_name=user, count=3):
        try:
            #check if retweet
            retweet = tweet.retweeted_status
            print("Tweet is a retweet")
        except:
            # check if tweet in timeframe
            if tweet.created_at > time:
                #count all interaction
                sum = tweet.retweet_count + tweet.favorite_count 
                try:
                    sum += tweet.reply_count
                except:
                    print("No Replys")
                try:
                    sum += tweet.quote_count
                except:
                    print("No Quotes")
                try:
                    url = tweet.entities['media'][0]['expanded_url']
                except:
                    try:
                        url = tweet.entities['urls'][0]['expanded_url']
                    except:
                        print("Couldn't get url")
                        break
                best_tweets[url] = sum
            else: 
                break
    print(best_tweets)

time = datetime.now() - timedelta(days=365)
get_most_liked('MayADevBe', time)