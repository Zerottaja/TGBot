import json
import requests

TOKEN = "308527009:AAFPg5p53k-I0iYuWJNU-eDJTRGutg2Xx_8"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
WHITELIST = {21942357, 152093174}


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

paivitykset = get_updates()
viime_paiv = len(paivitykset["result"]) - 1
if paivitykset["result"][viime_paiv]["message"]["from"]["id"] in WHITELIST:
    teksti, chat = get_last_chat_id_and_text(paivitykset)
    send_message(teksti, chat)
else:
    chat = get_last_chat_id_and_text(paivitykset)[1]
    send_message("Who are you?", chat)
