import win32gui


class Rectangle:
    x: int
    y: int
    x1: int
    y1: int
    color: None

    def __init__(self, x: int, y: int, x1: int, y1: int, color):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.color = color

    def draw(self, hdc):
        for x in range(self.x, self.x1 + 1):
            win32gui.SetPixel(
                hdc,
                x,
                self.y,
                self.color
            )
            win32gui.SetPixel(
                hdc,
                x,
                self.y1,
                self.color
            )

        for y in range(self.y, self.y1 + 1):
            win32gui.SetPixel(
                hdc,
                self.x,
                y,
                self.color
            )
            win32gui.SetPixel(
                hdc,
                self.x1,
                y,
                self.color
            )
