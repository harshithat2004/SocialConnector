import tweepy
import requests
from requests_oauthlib import OAuth2

# Replace with your own credentials
consumer_key = "3km4ixzoXn7EQuDFjeCCPlzOD"
consumer_secret = "fkTmMSOLq0NUMhvAAT5ep7Enxwy7Kwami2VSLEZyo2VhWKQPRC"
access_token = "1702941301476618240-eNb0ifL70YzEJfeHXqahEO0rhlkb2g"
access_token_secret = "f0A3qP2MlU3A6i270UyYFa5GppI19Wdoxow69lGJKENYv"
# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Your tweet text
tweet_text = "Hello, Twitter! This is a test tweet from my Python code."
status = api.update_status(status=tweet_text)

# Post the tweet

print("Tweet posted successfully!")