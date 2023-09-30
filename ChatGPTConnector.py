import requests
import json
import re

def send_gpt_request(api_key, message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': message}]
    }

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        raise Exception(f'Request failed with status code {response.status_code}: {response.text}')

# Set your API key and message
api_key = ''

message = "Give me 5 recipies that can be made using chicken"
# Send the request and print the response
try:
    response = send_gpt_request(api_key, message)
    print("Output text")
    print(response)


except Exception as e:
    print(f'Error: {str(e)}')
