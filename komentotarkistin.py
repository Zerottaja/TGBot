import autekbot

from ovianturi import OviAnturi
from valoanturi import ValoAnturi


def tarkista_komento(update, teksti, chat):
    ovi = OviAnturi()
    valot = ValoAnturi()

    # Onko lahettaja hallituksessa?
    if onko_hallituksessa(update):
        # /nakki-komennolla kaynnistetaan nakkikone
        if teksti == "/nakki" or (teksti == "/nakki@Autekbot"):
            teksti = autekbot.hallitusnakki()
            return teksti, chat

    # /ovi-komennolla tarkistetaan oven mikrokytkimen tila.
    if teksti == "/ovi" or teksti == "/ovi@Autekbot":
        if ovi.mittaa():
            teksti = "Ovi on AUKI!"
        else:
            teksti = "Ovi on KIINNI!"

    # /valot-komennolla tutkitaan valaistuksen tila.
    elif teksti == "/valot" or teksti == "/valot@Autekbot":
        if valot.mittaa():
            teksti = "Valot ON!"
        else:
            teksti = "Valot POIS!"
    elif (teksti == "/nakki") or (teksti == "/nakki@Autekbot"):
        teksti = "Et ole hallituksessa!"
    else:
        teksti = None
    return teksti, chat


# onko_hallituksessa() tarkistaa lahettajan id:n ja vertaa sita Whitelistiin
def onko_hallituksessa(update):
    if update["message"]["from"]["id"] in autekbot.WHITELIST:
        return True
    return False