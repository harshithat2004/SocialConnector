from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with your own API credentials JSON file path
credentials_file = 'dk4learning-e4dd99460a33.json'

# Create an OAuth 2.0 Service Account Credentials object
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
)

# Build the YouTube API service
youtube = build('youtube', 'v3', credentials=credentials)

username1 = 'thanthitv'
username2 = 'News7TamilPRIME'


# Use the search().list() method to search for the channel by username
search_response = youtube.search().list(
    q=username1,
    type='channel',
    part='id'
).execute()
search_response2 = youtube.search().list(
    q=username2,
    type='channel',
    part='id'
).execute()

# Check if any channels were found in the search results
channel_ids=[]
channel_info={}
if 'items' in search_response and len(search_response['items']) > 0:
    channel_id = search_response['items'][0]['id']['channelId']
    channel_ids.append(channel_id)
    channel_info[channel_id]=username1
    print(f"Channel Name: {username1} Channel ID:{channel_id}")
else:
    print("No channel found with the username:", username1)
    exit(1)

if 'items' in search_response2 and len(search_response2['items']) > 0:
    channel_id = search_response2['items'][0]['id']['channelId']
    channel_ids.append(channel_id)
    channel_info[channel_id]=username2
    print(f"Channel Name: {username2} Channel ID:{channel_id}")
else:
    print("No channel found with the username:", username2)
    exit(1)
# List to store channel statistics
channel_stats = []


for channel_id in channel_ids:
    # Use the channels().list() method to retrieve channel details by ID
    channels_response = youtube.channels().list(
        part='statistics',
        id=channel_id
    ).execute()

    # Check if a channel with the given ID exists
    if 'items' in channels_response and len(channels_response['items']) > 0:
        statistics = channels_response['items'][0]['statistics']
        statistics['channelName']= channel_info.get(channel_id)
        channel_stats.append(statistics)
    else:
        print("Channel not found with the ID:", channel_id)

# Print the collected statistics
for idx, stats in enumerate(channel_stats, start=1):
    print(f"Statistics for Channel:",stats.get('channelName','N/A'))
    print("----------------------------")
    print("Subscriber Count:", stats.get('subscriberCount', 'N/A'))
    print("View Count:", stats.get('viewCount', 'N/A'))
    print("Video Count:", stats.get('videoCount', 'N/A'))

    print()