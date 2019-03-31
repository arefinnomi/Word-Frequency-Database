import requests
from requests import ConnectionError

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
params = dict(
        key="trnsl.1.1.20180816T201124Z.3c913b3ba23668cf.459effb2db9c2b5931025beaf86320de019abb24",
        format="plain",
        lang="en-bn",
        text=""
    )


def get_translation(english_word):
    bangla_word = ""
    params['text'] = english_word
    try:
        resp = requests.get(url=url, params=params)
        data = resp.json()

        if data['code'] == 200:
            bangla_word = data['text'][0]
    except ConnectionError as e:
        bangla_word = ''
    return bangla_word
