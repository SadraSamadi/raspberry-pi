from random import randint
from gpiozero import LED
from time import sleep

leds = [LED(i) for i in [14, 15, 18, 23, 24, 25, 8, 7]]


def show_num(num):
    bits = bin(num)[2:].zfill(8)
    for index, bit in enumerate(bits):
        if bit is '0':
            leds[7 - index].off()
        elif bit is '1':
            leds[7 - index].on()


try:
    cntr = 0
    while True:
        if cntr < 256:
            show_num(cntr)
        else:
            show_num(randint(0, 255))
        cntr += 1
        if cntr == 512:
            cntr = 0
        sleep(.05)
except KeyboardInterrupt:
    pass
finally:
    for led in leds:
        led.off()
