char_map = {
    ' ': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    'A': [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ],
    'B': [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
    ],
    'S': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    'H': [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ]
}


class Canvas:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._matrix = []
        for y in range(self._height):
            row = []
            for x in range(self._width):
                row.append(1)
            self._matrix.append(row)

    def set(self, x, y, value):
        x = int(round(x))
        y = int(round(y))
        if x in range(0, self._width) and y in range(0, self._height):
            self._matrix[y][x] = 1 if value == 0 else 0

    def on(self, x, y):
        self.set(x, y, 1)

    def off(self, x, y):
        self.set(x, y, 0)

    def set_all(self, value):
        for y in range(self._height):
            for x in range(self._width):
                self.set(x, y, value)

    def on_all(self):
        self.set_all(1)

    def off_all(self):
        self.set_all(0)

    def draw_char(self, x, y, ch):
        data = char_map[ch]
        for i, line in enumerate(data):
            for j, value in enumerate(line):
                self.set(j + x, i + y, value)

    def draw_text(self, x, y, text):
        for i, ch in enumerate(text):
            self.draw_char(x + 6 * i, y, ch)

    @property
    def matrix(self):
        return self._matrix
