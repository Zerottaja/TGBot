#!/usr/bin/python
# -*- coding: utf8 -*-

try:
    import RPi.GPIO as GPIO

    class OviAnturi:

        def __init__(self):
            GPIO.setmode(GPIO.BOARD)
            # Maaritetaan pinni 11 inputiksi
            self.ovipinni = 11
            GPIO.setup(self.ovipinni, GPIO.IN)

        def mittaa(self):
            # Tarkistetaan pinnin tila ja palautetaan vastaus
            if not self.ovipinni:
                vastaus = "Ovi on auki."
            else:
                vastaus = "Ovi on kiinni."

            return vastaus

except ImportError:
    print("GPIO-jako toimii vain Raspberry-alustalla t. OviAnturi")
    GPIO = None
    import random

    class OviAnturi:

        def __init__(self):
            self.ovipinni = 11

        def mittaa(self):
            self.ovipinni = random.randint(0, 1)
            if self.ovipinni == 1:
                vastaus = "Ovi on auki."
            else:
                vastaus = "Ovi on kiinni."
            return vastaus
