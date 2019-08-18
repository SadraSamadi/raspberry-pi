class Shape:

    def __init__(self):
        pass


class Point(Shape):

    def __init__(self, x, y, vx, vy):
        Shape.__init__(self)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


class Line(Shape):

    def __init__(self, x1, y1, x2, y2):
        Shape.__init__(self)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
