from threading import Thread
from gpiozero import LEDBoard
from time import sleep, time
from .canvas import Canvas


class Graphic:
    WIDTH = 12
    HEIGHT = 9
    RENDER_DELAY = .001
    FPS = 60
    TPF = float(1) / FPS

    def __init__(self, panel):
        self._panel = panel
        if self._panel.width not in range(Graphic.WIDTH + 1) and self._panel.height not in range(Graphic.HEIGHT + 1):
            raise SystemError('Panel size is illegal!')
        self._running = True
        self._coms = LEDBoard(2, 3, 4, 17, 27, 22, 10, 9, 11)
        self._segs = LEDBoard(14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21)
        self._canvas = Canvas(self._panel.width, self._panel.height)
        self._render_thread = Thread(target=self.render)
        self._update_thread = Thread(target=self.update)

    def render(self):
        while self._running:
            for i in range(self._panel.height):
                self._segs.value = self._canvas.matrix[i]
                com = self._coms.leds[i]
                com.on()
                sleep(Graphic.RENDER_DELAY)
                com.off()

    def update(self):
        last = time()
        while self._running:
            start = time()
            current = time()
            self._panel.render(self._canvas, current - last)
            last = current
            try:
                sleep(start + Graphic.TPF - time())
            except IOError:
                pass

    def start(self):
        self._coms.off()
        self._segs.on()
        self._render_thread.start()
        self._update_thread.start()

    def stop(self):
        self._running = False
        self._render_thread.join()
        self._update_thread.join()
        self._segs.close()
        self._coms.close()
