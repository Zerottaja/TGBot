import random
try:
    import RPi.GPIO as GPIO

    class ValoAnturi:

        def __init__(self):
            self.arvo = 0

        def mittaa(self):
            return random.randint(0, 1)
except ImportError:
    print("GPIO-jako toimii vain Raspberry-alustalla t. ValoAnturi")
    GPIO = None

    class ValoAnturi:

        def __init__(self):
            self.arvo = 0

        def mittaa(self):
            return random.randint(0, 1)
