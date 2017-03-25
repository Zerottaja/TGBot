import json
import requests
import time
import random
from openpyxl import load_workbook

###################################################################################
#  --------------------------------  @Autekbot  --------------------------------  #
#  --------------------------------  Samu Ampio --------------------------------  #
###################################################################################

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
        url = URL + "sendMessage?text=I don't know " \
                    "how to say that.. :o&chat_id={}".format(chat_id)
    get_url(url)
    return


# onko_hallituksessa() tarkistaa lahettajan id:n ja vertaa sita Whitelistiin
def onko_hallituksessa(paivitykset):
    # Viimeisin viesti on listan viimeinen...
    viim_paiv = len(paivitykset["result"]) - 1
    if paivitykset["result"][viim_paiv]["message"]["from"]["id"] in WHITELIST:
        return True
    return False


# hallitusnakki() lukee botin tyokansiossa olevan hallitus-excelin
# ja arpoo nimien joukosta yhden seka palauttaa sen.
def hallitusnakki():
    # Avataan hallitustaulukko.
    worksheet = load_workbook('hallitus.xlsx').active
    # Tarkistetaan montako nimea on listassa
    # ja arvotaan luku 1 ja maksimin valilta.
    arpa = random.randrange(1, worksheet.max_row)
    # Kaivetaan arpalukua vastaava yhteystieto ja palautetaan se.
    nakkinimi = worksheet['A{}'.format(arpa)].value
    return nakkinimi


def main():
    edellinen_paiv = None
    while True:
        # Haetaan paivitykset serverilta.
        paivitykset = get_updates()
        # Viimeisin viesti on listan viimeinen...
        viim_paiv = len(paivitykset["result"]) - 1
        # Onko uusin viesti eri kuin viimeksi?
        if edellinen_paiv != viim_paiv:
            # Onko lahettaja hallituksessa?
            if onko_hallituksessa(paivitykset):
                # Tallennetaan teksti ja chat_id muuttujiin
                teksti, chat = get_last_chat_id_and_text(paivitykset)
                # /nakki komennolla kaynnistetaan nakkikone
                if teksti == "/nakki":
                    teksti = hallitusnakki()
                send_message(teksti, chat)
            else:
                # Tuntemattomat saavat kylmaa katta
                chat = get_last_chat_id_and_text(paivitykset)[1]
                send_message("Who are you? O_o", chat)
            # Paivitetaan tieto viimeisimmasta viestista
            edellinen_paiv = viim_paiv
        # Odotetaan hyvan maun nimissa vahan aikaa
        time.sleep(0.5)

main()
