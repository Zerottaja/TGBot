import time
from openpyxl import load_workbook


def kirjaa_hallituspalaute(palaute):
    # Avataan hallitustaulukko.
    wb = load_workbook('hallituspalaute.xlsx')
    worksheet = wb.active
    palautteiden_lkm = worksheet.max_row
    kirjattava = "{} {}.{}.{} @ {}:{}".format(palaute, time.localtime()[2],
                                              time.localtime()[1],
                                              time.localtime()[0],
                                              time.localtime()[3],
                                              time.localtime()[4])
    worksheet['A{}'.format(palautteiden_lkm + 1)] = kirjattava

    try:
        wb.save('hallituspalaute.xlsx')
    except IOError or PermissionError:
        print("Ei voitu tallentaa palautetta: '" + kirjattava + "'")

    return


def raportti():
    # Avataan hallitustaulukko.
    wb = load_workbook('hallituspalaute.xlsx')
    worksheet = wb.active
    palautteiden_lkm = worksheet.max_row
    if palautteiden_lkm <= 6:
        alaraja = 2
    else:
        alaraja = palautteiden_lkm - 5
    palautettava = ""
    for i in range(alaraja, palautteiden_lkm + 1):
        palautettava = palautettava + worksheet['A{}'.format(i)].value + "\n"

    return palautettava
