import win32gui
from .color import Color


class Line:
    x: int
    y: int
    x1: int
    y1: int
    color: Color.red

    def __init__(self, x: int, y: int, x1: int, y1: int, color: Color = Color.red):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw(self, hdc):
        for x in range(self.x, self.x1 + 1):
            for y in range(self.y, self.y1 + 1):
                win32gui.SetPixel(
                    hdc,
                    x,
                    y,
                    self.color
                )
