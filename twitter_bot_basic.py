#!/usr/bin/python
#Import tweepy packages
import tweepy
#Import time packages
import time

#Import custom packages in order to run authorization and read from file
from twitter_auth import TwitterAuth
from twitter_document import TwitterDocument

#instance twitter_auth is an instance of class TwitterAuth()
twitter_auth = TwitterAuth()
api = tweepy.API(twitter_auth.get_Auth_Connection())

#Prints to user's terminal "Enter File Path" to specify what raw input user should enter
print 'Enter File Path'

file_path = raw_input()

twit_test = TwitterDocument(file_path)
twit_test.open_File()
#try/finally will catch exceptions so file connection will close when encountering exception
#Pulls line from .txt file and returns lines broken into tweetable arrays
#Then pulls tweets from array and posts to twitter and waits 60 seconds
try:
    for tweet_array in twit_test:
        for tweet in tweet_array:
            api.update_status(status=tweet)
            time.sleep(60)

finally: 
    twit_test.close_File()


