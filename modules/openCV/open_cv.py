import cv2
import numpy
from .classes.rectangle import Rectangle

DETECT_DEFAULT_THRESHOLD = 0.9


# 찾은 이미지들의 상하좌우 포인트를 돌려줍니다.
def detect(detect_img_path: list[str], from_img_path: str, threshold: float = DETECT_DEFAULT_THRESHOLD) \
        -> list[Rectangle]:
    img_rgb = cv2.imread(from_img_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(detect_img_path, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    res_rectangle_list = []
    for pt in zip(*loc[::-1]):
        rectangle = Rectangle(pt[0], pt[1], pt[0] + w, pt[1] + h)
        res_rectangle_list.append(rectangle)
    return res_rectangle_list
