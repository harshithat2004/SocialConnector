import tweepy
import requests
from requests_oauthlib import OAuth2

# Replace with your own credentials
consumer_key = "3km4ixzoXn7EQuDFjeCCPlzOD"
consumer_secret = "fkTmMSOLq0NUMhvAAT5ep7Enxwy7Kwami2VSLEZyo2VhWKQPRC"
access_token = "1702941301476618240-eNb0ifL70YzEJfeHXqahEO0rhlkb2g"
access_token_secret = "f0A3qP2MlU3A6i270UyYFa5GppI19Wdoxow69lGJKENYv"

tweet_text = "Posting this tweet from python"

# Twitter API endpoint for posting tweets
tweet_url = "https://api.twitter.com/2/tweets"

# Create an OAuth1 session
auth = OAuth2(
    consumer_key,
    consumer_secret,
    access_token
)

# Data to post as a tweet
tweet_data = {
    "text": tweet_text
}

# Make the POST request to post the tweet
response = requests.post(tweet_url, auth=auth, json=tweet_data)

# Check the response
if response.status_code == 201:
    print("Tweet posted successfully!")
else:
    print("Error posting tweet. Status code:", response.status_code)
    print(response.text)