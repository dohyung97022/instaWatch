import win32api
import win32con
import win32gui
import threading


class Win32Gui:
    draw_elements = []
    draw_thread = None
    wndClassAtom = None
    WM_QUIT = False

    @classmethod
    def draw(cls):
        wndClass = win32gui.WNDCLASS()
        wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wndClass.lpfnWndProc = cls.lpfnWndProc
        wndClass.hInstance = win32api.GetModuleHandle()
        wndClass.hCursor = win32gui.LoadCursor(None, win32con.IDC_ARROW)
        wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        wndClass.lpszClassName = 'MyWindowClassName'

        if cls.wndClassAtom is None:
            cls.wndClassAtom = win32gui.RegisterClass(wndClass)
        wndClassAtom = cls.wndClassAtom

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms632600(v=vs.85).aspx
        style = win32con.WS_DISABLED | win32con.WS_POPUP | win32con.WS_VISIBLE

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms632680(v=vs.85).aspx
        hWindow = win32gui.CreateWindowEx(
            exStyle,
            wndClassAtom,
            None,  # WindowName
            style,
            0,  # x
            0,  # y
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN),  # width
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN),  # height
            None,  # hWndParent
            None,  # hMenu
            wndClass.hInstance,
            None  # lpParam
        )

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633540(v=vs.85).aspx
        win32gui.SetLayeredWindowAttributes(hWindow, 0x00ffffff, 255, win32con.LWA_COLORKEY | win32con.LWA_ALPHA)

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633545(v=vs.85).aspx
        win32gui.SetWindowPos(
            hWindow,
            win32con.HWND_TOPMOST,
            0,  # x
            0,  # y
            0,  # width
            0,  # height
            win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW
        )
        while not Win32Gui.WM_QUIT:
            win32gui.PumpWaitingMessages()

    @staticmethod
    def lpfnWndProc(hWnd, message, wParam, lParam):
        if message == win32con.WM_PAINT:
            hdc, paintStruct = win32gui.BeginPaint(hWnd)

            for draw_process in Win32Gui.draw_elements:
                draw_process.draw(hdc)

            win32gui.EndPaint(hWnd, paintStruct)
            return 0

        elif message == win32con.WM_DESTROY:
            print('Closing the window.')
            win32gui.PostQuitMessage(0)
            return 0

        else:
            return win32gui.DefWindowProc(hWnd, message, wParam, lParam)

    @classmethod
    def draw_thread_start(cls):
        if Win32Gui.draw_thread is not None:
            return
        Win32Gui.draw_thread = threading.Thread(target=cls.draw)
        Win32Gui.draw_thread.setDaemon(True)
        Win32Gui.draw_thread.start()

    @classmethod
    def draw_thread_stop(cls):
        if Win32Gui.draw_thread is None:
            return
        Win32Gui.WM_QUIT = True
        Win32Gui.draw_thread.join()
        Win32Gui.WM_QUIT = False
        Win32Gui.draw_thread = None
