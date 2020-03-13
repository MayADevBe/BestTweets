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
    return best_tweets

def print_desc_list(best_tweets):
    for key, value in sorted(best_tweets.items(), key=lambda item: item[1], reverse=True):
        print("%s: %s" % (value, key))
    print()

def main():
    print()
    print("Get the most top tweets from a user!")
    print()
    user = input("Enter the screen name of the user: ")
    days = input("Enter how many days you want to look back: ")
    n = input("Enter the amount tweets you want returned: ")
    print()
    try:
        days = int(days)
        n = int(n)
        time = datetime.now() - timedelta(days=days)
        best_tweets = get_most_liked(user, time, n)
        print_desc_list(best_tweets)
    except ValueError:
        print("Days and amount have to be an int value!")   

main()