import requests
import base64
from api_key import API_TOKEN
import json


itemList = []

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        json.dump(data, fp)

path = './'
fileName = 'items'
data={}


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


# item = (ask("describe the grocery in the image in the format (What type of item it is , What the item is), for the purpose of \ "
#           "storing in a list. \ "
#           , './images/c1.png'))
item = (ask("who is the wierder person in the image? "
          , './images/c1.png'))

# print(item)


text = item.get('candidates')[0].get('content').get('parts')[0].get('text')
itemList.append(text)

# print(type(text))

print(itemList)

data['Food'] = text
writeToJSONFile(path, fileName, text)