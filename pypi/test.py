from graphic.graphic import Graphic
from my_panel import MyPanel
from time import sleep

panel = MyPanel()
graphic = Graphic(panel)

try:
    graphic.start()
    while True:
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    graphic.stop()
