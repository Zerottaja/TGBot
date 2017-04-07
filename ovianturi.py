import random
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("GPIO-jako toimii vain Raspberry-alustalla.")
    GPIO = None


RaspberryPi = False

if RaspberryPi:
    import RPi.GPIO as GPIO


class OviAnturi:

    def __init__(self):
        self.arvo = 0

    def mittaa(self):
        return random.randint(0, 1)
