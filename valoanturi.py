import random


RaspberryPi = False

if RaspberryPi:
    import RPi.GPIO as GPIO


class ValoAnturi:

    def __init__(self):
        self.arvo = 0
        
    def mittaa(self):
        return random.randint(0, 1)
