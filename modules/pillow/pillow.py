from PIL import ImageGrab


def take_screenshot(save_path: str):
    snapshot = ImageGrab.grab()
    snapshot.save(save_path)

