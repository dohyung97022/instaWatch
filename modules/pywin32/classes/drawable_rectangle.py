import win32gui
from .color import Color
from modules.common.classes.rectangle import Rectangle


class DrawableRectangle(Rectangle):
    color: Color.red

    def __init__(self, rectangle: Rectangle, color: Color = Color.red):
        Rectangle.__init__(self, rectangle.x, rectangle.y, rectangle.x1, rectangle.y1)
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
