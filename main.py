import requests
import base64
from api_key import API_TOKEN

def ask(prompt: str, image_path: str) -> str:
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    query = {'contents': [
        {'parts': [
            {'text': prompt},
            {'inline_data': {
                'mime_type': 'image/jpeg',
                'data': str(image_data)
            }}
        ]}
    ]}
    resp = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key=' + API_TOKEN,
        json=query)
    if resp.status_code != 200:
        print(resp.text + "- ERROR")
        return ''

    result = None
    try:
        result = resp.json()
    except Exception as e:
        pass
    return result


print(ask("describe the food in the image a format that I can put into a list into a json file  ", 'image3.jpg'))

