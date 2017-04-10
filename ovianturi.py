import random
try:
    import RPi.GPIO as GPIO

    class OviAnturi:

        def __init__(self):
            self.ovipinni = 11
            GPIO.input(self.ovipinni)

        def mittaa(self):
            if self.ovipinni == 1:
                vastaus = "Ovi on auki."
            else:
                vastaus = "Ovi on kiinni."
            return vastaus
except ImportError:
    print("GPIO-jako toimii vain Raspberry-alustalla t. OviAnturi")
    GPIO = None

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