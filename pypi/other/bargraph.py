from gpiozero import LEDBarGraph, LEDBoard
from time import sleep

bargraph = LEDBoard(3, 4, 17, 27, 22, 10, 9, 11, 7, 12)

try:
    bargraph.blink()
    while True:
        # for led in bargraph.leds:
        #     bargraph.off()
        #     led.on()
        sleep(.1)
except KeyboardInterrupt:
    pass
finally:
    bargraph.close()
