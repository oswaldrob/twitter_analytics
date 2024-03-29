#!/usr/bin/python

import json
import sys
import logging
import tweepy
import pandas as pd
import numpy as np
import pprint


#  https://github.com/bpb27/trump-tweet-archive/blob/master/server_scripts/get_trump.py
#  https://github.com/maxbbraun/trump2cash
#  http://www.trumptwitterarchive.com/
#  https://www.freecodecamp.org/news/learn-python-by-analyzing-donald-trumps-tweets-ccdf156cb5a3/


# Import creds:
#  (refactor credentials files into one) - credentials.py & .cred.json - both already in .gitignore.

from credentials import *    # I have a local file with all the OAuth API key details.

# API  setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Use tweepy for Oauth handler authentication and keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication
    api = tweepy.API(auth)
    return api

# Create an grabtweets object
grabtweets = twitter_setup()


# Create a tweet list
tweets = grabtweets.user_timeline(screen_name="realDonaldTrump", count=200, tweet_mode="extended")
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# Print the most recent 5 tweets:
print("Most recent 10 tweets (with times):\n")
for tweet in tweets[:10]:
    print(tweet.full_text, tweet.created_at, end = "\n\n")



# Full text example of each tweet object
pprint.pprint(tweets[0].__dict__)