import hallituspalaute

from ovianturi import OviAnturi
from valoanturi import ValoAnturi
import datetime


def tarkista_komento(update, teksti, chat):
    import autekbot
    ovi = OviAnturi()
    valot = ValoAnturi()

    # /ovi-komennolla tarkistetaan oven mikrokytkimen tila.
    if teksti == "/ovi" or teksti == "/ovi@Autekbot":
        if ovi.mittaa():
            vastaus = "Ovi on AUKI!"
        else:
            vastaus = "Ovi on KIINNI!"

    # /valot-komennolla tutkitaan valaistuksen tila.
    elif teksti == "/valot" or teksti == "/valot@Autekbot":
        if valot.mittaa():
            vastaus = "Valot ON!"
        else:
            vastaus = "Valot POIS!"

    # /nakki-komennolla kaynnistetaan nakkikone
    elif teksti == "/nakki" or teksti == "/nakki@Autekbot":
        # Onko lahettaja hallituksessa?
        if onko_hallituksessa(update):
            vastaus = autekbot.hallitusnakki()
        else:
            vastaus = "Et ole hallituksessa!"

    # /hallituspalaute-komennolla vastaanotetaan palautetta
    elif teksti == "/hallituspalaute" or teksti == \
            "/hallituspalaute@Autekbot":
        vastaus = "Kerro palautteesi tavallisena kirjoituksena alle." \
                  " Se on anonyymi, ellet erikseen allekirjoita palautetta."
        autekbot.odotettavien_lista[chat] = datetime.datetime.now()

    # Viesti ei ollut komento
    else:
        # Tarkistataan kuitenkin odotetaanko lahettajalta palautetta
        if chat in autekbot.odotettavien_lista:
            # Kirjataan palaute ylos
            hallituspalaute.kirjaa_hallituspalaute(teksti)
            # Kun palaute on ylhaalla, ei tarvitse odottaa enaa
            del autekbot.odotettavien_lista[chat]
            vastaus = "Kiitos palautteestasi!"
        else:
            vastaus = None

    return vastaus, chat


# onko_hallituksessa() tarkistaa lahettajan id:n ja vertaa sita Whitelistiin
def onko_hallituksessa(update):
    import autekbot
    if update["message"]["from"]["id"] in autekbot.WHITELIST:
        return True
    return False
