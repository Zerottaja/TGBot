import hallituspalaute
import nakkikone

from ovianturi import OviAnturi
from valoanturi import ValoAnturi
import datetime


def tarkista_komento(update, teksti, chat):
    import autekbot
    ovi = OviAnturi()
    valot = ValoAnturi()

    # /ovi-komennolla tarkistetaan oven mikrokytkimen tila.
    if teksti == "/ovi" or teksti == "/ovi@Autekbot":
        vastaus = ovi.mittaa()

    # /valot-komennolla tutkitaan valaistuksen tila.
    elif teksti == "/valot" or teksti == "/valot@Autekbot":
        vastaus = valot.mittaa()

    # /nakki-komennolla kaynnistetaan nakkikone
    elif teksti == "/nakki" or teksti == "/nakki@Autekbot":
        # Onko lahettaja hallituksessa?
        if onko_hallituksessa(update):
            vastaus = nakkikone.hallitusnakki()
        else:
            vastaus = "Et ole hallituksessa!"

    # /hallituspalaute-komennolla vastaanotetaan palautetta
    elif teksti == "/hallituspalaute" or teksti == \
            "/hallituspalaute@Autekbot":
        vastaus = "Kerro palautteesi tavallisena kirjoituksena alle." \
                  " Se on anonyymi, ellet erikseen allekirjoita palautetta."
        autekbot.odotettavien_lista[chat] = datetime.datetime.now()\
            .replace(microsecond=0)

    # Viesti ei ollut komento
    else:
        # Tarkistataan kuitenkin odotetaanko lahettajalta palautetta
        if chat in autekbot.odotettavien_lista:
            # Taman hetken kellonaika
            aika_nyt = datetime.datetime.now().replace(microsecond=0)
            # Aikaero taman hetken ja hallituspalautekaskyn valilla
            td = aika_nyt - autekbot.odotettavien_lista[chat]
            # Jos aikaero alle 900 s eli 15 min
            if td.seconds <= 900:
                # Kirjataan palaute ylos
                hallituspalaute.kirjaa_hallituspalaute(teksti)
                # Kun palaute on ylhaalla, ei tarvitse odottaa enaa
                del autekbot.odotettavien_lista[chat]
                vastaus = "Kiitos palautteestasi!"
            else:
                # Aikaeron ollessa yli 15 min, aikakatkaistaan odotus
                del autekbot.odotettavien_lista[chat]
                vastaus = "Palautteen odotus aikakatkaistiin " \
                          "(yli 15 min hallituspalaute-käskystä)."
        else:
            vastaus = None

    return vastaus, chat


# onko_hallituksessa() tarkistaa lahettajan id:n ja vertaa sita Whitelistiin
def onko_hallituksessa(update):
    import autekbot
    if update["message"]["from"]["id"] in autekbot.WHITELIST:
        return True
    return False
