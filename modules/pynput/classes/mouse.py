from pynput import mouse
from modules.common.classes.rectangle import Rectangle
from modules.pynput.classes.point import Point


class ButtonType:
    left = mouse.Button.left
    right = mouse.Button.right


class Mouse:
    class Control:
        controller = mouse.Controller()

        @classmethod
        def move(cls, x: int, y: int):
            cls.controller.position = (x, y)

        @classmethod
        def move_relative(cls, x: int, y: int):
            cls.controller.move = (x, y)

        @classmethod
        def press(cls, button_type: ButtonType = ButtonType.left):
            cls.controller.press(button_type)

        @classmethod
        def release(cls, button_type: ButtonType = ButtonType.left):
            cls.controller.release(button_type)

        @classmethod
        def double_press(cls, button_type: ButtonType = ButtonType.left):
            cls.controller.click(button_type, 2)

        @classmethod
        def scroll(cls, amount: int):
            cls.controller.scroll(0, amount)

    class Detect:

        @staticmethod
        def drag(button_type: ButtonType = ButtonType.left) -> Rectangle:
            rectangle = Rectangle()

            def on_click(x, y, button, pressed):
                if button == button_type:
                    if pressed:
                        rectangle.x = x
                        rectangle.y = y
                    else:
                        rectangle.x1 = x
                        rectangle.y1 = y
                        return False

            with mouse.Listener(
                    on_move=None,
                    on_click=on_click,
                    on_scroll=None) as listener:
                listener.join()

            return rectangle

        @staticmethod
        def press(button_type: ButtonType = ButtonType.left) -> Point:
            point = Point()

            def on_click(x, y, button, pressed):
                if pressed and button == button_type:
                    point.x = x
                    point.y = y
                    return False

            with mouse.Listener(
                    on_move=None,
                    on_click=on_click,
                    on_scroll=None) as listener:
                listener.join()

            return point
