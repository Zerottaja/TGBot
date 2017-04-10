import random
try:
    import RPi.GPIO as GPIO

    class ValoAnturi:

        def __init__(self):
            self.kattopinni = 13
            self.bilepinni = 15
            GPIO.input(self.kattopinni)
            GPIO.input(self.bilepinni)

        def mittaa(self):
            if self.kattopinni == 0 and self.bilepinni == 0:
                vastaus = "Kaikki valot ovat pois."
            elif self.kattopinni == 0 and self.bilepinni == 1:
                vastaus = "Bilevalot ovat päällä!"
            elif self.kattopinni == 1 and self.bilepinni == 0:
                vastaus = "Valot ovat päällä."
            else:
                vastaus = "Sekä katto- että bilevalot ovat päällä..?"
            return vastaus

except ImportError:
    print("GPIO-jako toimii vain Raspberry-alustalla t. ValoAnturi")
    GPIO = None

    class ValoAnturi:

        def __init__(self):
            self.kattopinni = 13
            self.bilepinni = 15

        def mittaa(self):
            self.kattopinni = random.randint(0, 1)
            self.bilepinni = random.randint(0, 1)

            if self.kattopinni == 0 and self.bilepinni == 0:
                vastaus = "Kaikki valot ovat pois."
            elif self.kattopinni == 0 and self.bilepinni == 1:
                vastaus = "Bilevalot ovat päällä!"
            elif self.kattopinni == 1 and self.bilepinni == 0:
                vastaus = "Valot ovat päällä."
            else:
                vastaus = "Sekä katto- että bilevalot ovat päällä..?"
            return vastaus
