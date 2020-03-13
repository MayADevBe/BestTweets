import tweepy
from datetime import datetime
from datetime import timedelta
import config

api = config.get_Api()

def get_most_liked(user, time, n):
    best_tweets = {}
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode="extended").items():
        try:
            #check if retweet
            retweet = tweet.retweeted_status
            #print("Tweet is a retweet")
        except:
            # check if tweet in timeframe
            if tweet.created_at > time:
                #count all interaction
                sum = tweet.retweet_count + tweet.favorite_count 
                try:
                    sum += tweet.reply_count
                except:
                    #print("No Replys")
                    pass
                try:
                    sum += tweet.quote_count
                except:
                    #print("No Quotes")
                    pass
                #get url for dict
                try:
                    url = tweet.entities['media'][0]['expanded_url']
                except:
                    try:
                        url = tweet.entities['urls'][0]['expanded_url']
                    except:
                        print("Couldn't get url")
                        url = f"https://twitter.com/{user}/status/{tweet.id}"
                best_tweets[url] = sum
                #remove min if dict is too big
                if len(best_tweets) > n:
                    min_url = url
                    min_sum = sum
                    for k in best_tweets.keys():
                        if best_tweets[k] < min_sum:
                            min_url = k
                            min_sum = best_tweets[k]
                    del best_tweets[min_url]
            else: 
                break
    print(best_tweets)

time = datetime.now() - timedelta(days=2)
get_most_liked('MayADevBe', time, 10)