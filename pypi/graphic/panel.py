class Panel:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def render(self, canvas, delta):
        pass

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
