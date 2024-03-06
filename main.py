import requests
from api_key import API_TOKEN


def call(prompt: str) -> str:
    resp = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + API_TOKEN,
        json={'contents': [{'parts': [{'text': prompt}]}]})

    if resp.status_code != 200:
        return ''
    return resp.json().get('candidates')[0].get('content').get('parts')[0].get('text')


thought = call(
    'Are you able to analyze images? Answer in under 300 characters')
print('%d: %s' % (0, thought))
