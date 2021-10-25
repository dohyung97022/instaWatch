class Rectangle:
    x: int
    y: int
    x1: int
    y1: int

    def __init__(self, x: int = 0, y: int = 0, x1: int = 0, y1: int = 0):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    @property
    def w(self):
        return self.x1 - self.x

    @property
    def h(self):
        return self.y1 - self.y
