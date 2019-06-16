#!/usr/bin/python

import json
import sys
import logging
import tweepy
import pandas as pd
import numpy as np


#  https://github.com/bpb27/trump-tweet-archive/blob/master/server_scripts/get_trump.py
#  https://github.com/maxbbraun/trump2cash
#  http://www.trumptwitterarchive.com/
#  https://www.freecodecamp.org/news/learn-python-by-analyzing-donald-trumps-tweets-ccdf156cb5a3/


#import twittertwitter_api = twitter.Api(consumer_key="YOUR_CONSUMER_KEY", consumer_secret="YOUR_CONSUMER_SECRET",  access_token_key="YOUR_ACCESS_TOKEN", access_token_secret="YOUR_ACCESS_TOKEN_SECRET",  tweet_mode='extended')twitter_api.VerifyCredentials()
#last_tweet = twitter_api.GetUserTimeline(screen_name="realDonaldTrump", count=10)


# We import our access keys:
from credentials import *    # This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()


#  refactor credentials files into one, both already in .gitignore.