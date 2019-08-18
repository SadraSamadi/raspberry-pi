from graphic.panel import Panel
from graphic.shape import Point
from threading import Thread
from gpiozero import Buzzer
from time import sleep


class MyPanel(Panel):

    def __init__(self):
        Panel.__init__(self, 12, 9)
        self._point = Point(0, 0, 20, 20)
        self._buz = Buzzer(26)

    def render(self, canvas, delta):
        canvas.off_all()
        # canvas.draw_text(self.x, 1, 'SHAHAB')
        # self.x += -10 * delta
        # if self.x < -35:
        #     self.x = 13
        # # canvas.draw_char(0, 1, 'A')
        # canvas.draw_char(6, 1, 'B')
        canvas.on(self._point.x, self._point.y)
        self._point.x += self._point.vx * delta
        self._point.y += self._point.vy * delta
        if self._point.x <= 0:
            self._collision()
            self._point.vx = abs(self._point.vx)
        if self._point.x >= self.width - 1:
            self._collision()
            self._point.vx = -abs(self._point.vx)
        if self._point.y <= 0:
            self._collision()
            self._point.vy = abs(self._point.vy)
        if self._point.y >= self.height - 1:
            self._collision()
            self._point.vy = -abs(self._point.vy)

    def _collision(self):
        thread = Thread(target=self._play_sound)
        thread.start()

    def _play_sound(self):
        self._buz.on()
        sleep(.05)
        self._buz.off()
