import time
from openpyxl import load_workbook


def kirjaa_hallituspalaute():
    # Avataan hallitustaulukko.
    wb = load_workbook('hallituspalaute.xlsx')
    worksheet = wb.active
    palautteiden_lkm = worksheet.max_row
    worksheet['A{}'.format(palautteiden_lkm + 1)] = \
        "Palautetta saatana! {}.{}.{} @ {}:{}".format(time.localtime()[2],
                                                      time.localtime()[1],
                                                      time.localtime()[0],
                                                      time.localtime()[3],
                                                      time.localtime()[4])
    wb.save('hallituspalaute.xlsx')
    return
