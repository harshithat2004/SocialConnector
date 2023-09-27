from google.oauth2 import service_account
from googleapiclient.discovery import build
import re

# Replace with your own API credentials JSON file path
credentials_file = 'dk4learning-e4dd99460a33.json'

# Create an OAuth 2.0 Service Account Credentials object
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
)

# Build the YouTube API service
youtube = build('youtube', 'v3', credentials=credentials)

username = 'MoneyPechu'

# Use the search().list() method to search for the channel by username
search_response = youtube.search().list(
    q=username,
    type='channel',
    part='id'
).execute()

# Check if any channels were found in the search results
channel_id=''
if 'items' in search_response and len(search_response['items']) > 0:
    channel_id = search_response['items'][0]['id']['channelId']
    print("Channel ID:", channel_id)
else:
    print("No channel found with the username:", username)
    exit(1)

# Use the channels().list() method to retrieve channel details by ID
channels_response = youtube.channels().list(
    part='snippet,statistics',
    id=channel_id
).execute()

# Check if a channel with the given ID exists
if 'items' in channels_response and len(channels_response['items']) > 0:
    channel = channels_response['items'][0]

    # Print channel details
    # print("Channel ID:", channel['id'])
    print("Channel Title:", channel['snippet']['title'])
    print("Channel Description:", channel['snippet']['description'])
    print("Subscriber Count:", channel['statistics']['subscriberCount'])
    print("View Count:", channel['statistics']['viewCount'])
    print("Video Count:", channel['statistics']['videoCount'])
else:
    print("Channel not found with the ID:", channel_id)