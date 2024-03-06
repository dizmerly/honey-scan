import requests
from api_key import API_TOKEN
import PIL.Image

def call(prompt: str) -> str:
    resp = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + API_TOKEN,
        json={'contents': [{'parts': [{'text': prompt}]}]})

    if resp.status_code != 200:
        return ''
    return resp.json().get('candidates')[0].get('content').get('parts')[0].get('text')


question = call(
    'Are you able to process images?')
print('%d: %s' % (0, question))
