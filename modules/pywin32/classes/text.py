import win32gui
import win32con
import win32ui


class Text:
    x: int
    y: int
    size: int = 10

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self, hdc):
        dpiScale = win32ui.GetDeviceCaps(hdc, win32con.LOGPIXELSX) / 60.0

        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
        lf = win32gui.LOGFONT()
        lf.lfFaceName = "Times New Roman"
        lf.lfHeight = int(round(dpiScale * self.size))
        hf = win32gui.CreateFontIndirect(lf)
        win32gui.SelectObject(hdc, hf)
        rect = (self.x, self.y, self.x, self.y)

        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd162498(v=vs.85).aspx
        win32gui.DrawText(
            hdc,
            'Text on the screen',
            -1,
            rect,
            win32con.DT_CENTER | win32con.DT_NOCLIP | win32con.DT_SINGLELINE | win32con.DT_VCENTER
        )
