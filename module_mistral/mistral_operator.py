import os
import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('MISTRAL_API_KEY', ''),
}

json_data = {
    'model': 'mistral-tiny',
    'messages': [
        {
            'role': 'user',
            'content': 'Who is the most renowned French painter?',
        },
    ],
}

response = requests.post('https://api.mistral.ai/v1/chat/completions', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n    "model": "mistral-tiny",\n    "messages": [{"role": "user", "content": "Who is the most renowned French painter?"}]\n  }'
#response = requests.post('https://api.mistral.ai/v1/chat/completions', headers=headers, data=data)