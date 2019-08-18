from gpiozero import PWMLED
from time import sleep

leds = [PWMLED(i) for i in [14, 15, 18, 23, 24, 25, 8, 7]]

for led in leds:
    led.blink()

while True:
    pass
