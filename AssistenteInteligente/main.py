import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "user",
            "content": "Me conte uma piada sobre IA"
        }
    ]
}
try:

    resp = requests.post(f'{api_url}/chat/completions', headers=headers, json=data)
    body = resp.json()

    text = body['choices'][0]['message']['content']

    print(text)

except Exception as e:
    raise print(e)