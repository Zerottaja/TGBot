from openpyxl import load_workbook
from openpyxl import Workbook


def lisaa_kayttaja(kayttaja_id):

    if not etsi_kayttaja(kayttaja_id):
        try:
            # Avataan id-taulukko.
            wb = load_workbook('WHITELIST.xlsx')
        except FileNotFoundError:
            wb = Workbook()
        worksheet = wb.active
        kayttajien_lkm = worksheet.max_row
        worksheet['A{}'.format(kayttajien_lkm + 1)] = kayttaja_id
        wb.save('WHITELIST.xlsx')

    return


def etsi_kayttaja(kayttaja_id):
    try:
        # Avataan id-taulukko.
        wb = load_workbook('WHITELIST.xlsx')
    except FileNotFoundError:
        return False
    worksheet = wb.active
    korkein_rivi = worksheet.max_row
    print(korkein_rivi)
    if korkein_rivi == 1:
        return False

    i = 2
    while i <= korkein_rivi:
        print("loop: " + str(i))
        if kayttaja_id == worksheet['A{}'.format(i)].value:
            return True
        elif worksheet['A{}'.format(i)].value is None:
            print(1)
            worksheet['A{}'.format(i)].value \
                = worksheet['A{}'.format(korkein_rivi)].value
            worksheet['A{}'.format(korkein_rivi)].value = None
            korkein_rivi = korkein_rivi - 1
            wb.save('WHITELIST.xlsx')
        i = i + 1
    print("nope")
    print(worksheet['A9'].value)

    return False

# TODO: excel-listan siirto muuttujalistaan, jotta  exceliä ei
# tarvitse joka kerta onko_hallituksessa() avata
