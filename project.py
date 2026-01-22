import os

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('BASE_URL')
API_KEY = os.getenv('API_KEY')
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'user', 'content': 'Объясни, что такое Deep Learning'}
    ]
}
response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result['choices'][0]['message']['content'])
