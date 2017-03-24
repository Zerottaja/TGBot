import json
import requests
import time

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
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    try:
        text = updates["result"][last_update]["message"]["text"]
        return text, chat_id
    except KeyError or UnicodeEncodeError:
        return "I'm blind, you need to speak. U_U", chat_id


def send_message(text, chat_id):
    try:
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    except UnicodeEncodeError:
        url = URL + "sendMessage?text=I don't know how to say that.. :o&chat_id={}".format(chat_id)
    get_url(url)


def main():
    edellinen_paiv = None
    while True:
        paivitykset = get_updates()
        viim_paiv = len(paivitykset["result"]) - 1
        if edellinen_paiv != viim_paiv:
            if paivitykset["result"][viim_paiv]["message"]["from"]["id"] in WHITELIST:
                teksti, chat = get_last_chat_id_and_text(paivitykset)
                send_message(teksti, chat)
            else:
                chat = get_last_chat_id_and_text(paivitykset)[1]
                send_message("Who are you? O_o", chat)
        time.sleep(0.5)
        edellinen_paiv = viim_paiv
main()
