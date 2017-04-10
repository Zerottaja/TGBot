import random
try:
    import RPi.GPIO as GPIO

    class OviAnturi:

        def __init__(self):
            self.ovipinni = 11
            GPIO.input(self.ovipinni)

        def mittaa(self):
            return random.randint(0, 1)
except ImportError:
    print("GPIO-jako toimii vain Raspberry-alustalla t. OviAnturi")
    GPIO = None

    class OviAnturi:

        def __init__(self):
            self.arvo = 0

        def mittaa(self):
            return random.randint(0, 1)
