from flask import Flask, render_template, request
import requests

# Set your API key and message
api_key = ''

app = Flask(__name__)

def send_gpt_request(api_key, message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
    # "text-davinci-002",
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


@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # response = call_chatgpt(user_input)
        response = send_gpt_request(api_key, user_input)
        user_input = "User Input: " + user_input
        return render_template('index.html', user_input=user_input, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
