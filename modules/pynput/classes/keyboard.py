from pynput import keyboard
from typing import Callable


class MultipleKeys:
    ctrl_s = '<ctrl>+s'


class Keyboard:
    class Detect:

        @staticmethod
        def multiple_key(multiple_keys: str, run_on_detect: Callable):
            def on_activate():
                run_on_detect()
                listener.stop()

            def for_canonical(f):
                return lambda k: f(listener.canonical(k))

            hot_key = keyboard.HotKey(
                keyboard.HotKey.parse(multiple_keys), on_activate
            )

            with keyboard.Listener(
                    on_press=for_canonical(hot_key.press),
                    on_release=for_canonical(hot_key.release)
            ) as listener:
                listener.join()
