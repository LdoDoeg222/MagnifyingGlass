# 虚线
import sys

import pyautogui
import cv2
import numpy as np

from PySide6.QtWidgets import QApplication, QWidget
import dash

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from PIL import ImageGrab


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


def draw_Rect(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("坐标 x=:{0}, y=:{1}".format(x, y))
    if event == cv2.EVENT_MOUSEMOVE:
        print("坐标 x=:{0}, y=:{1}".format(x, y))
    if event == cv2.EVENT_LBUTTONUP:
        print("坐标 x=:{0}, y=:{1}".format(x, y))


class ScreenCapture:
    def __init__(self):
        self.screen_shot = None

    def capture(self):
        self.screen_shot = ImageGrab.grab()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # img = pyautogui.screenshot(region=[600, 100, 200, 100])
    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    # cv2.imshow("ScreenShot", img)
    # cv2.waitKey(0)
    # screenWidth, screenHeight = pyautogui.size()
    # mouseX, mouseY = pyautogui.position()
    # pyautogui.PAUSE = 1
    # pyautogui.FAILSAFE = True
    x0, y0, x1, y1 = 0, 0, 512, 512

    color = (255, 0, 0)
    img = np.zeros((x1, y1, 3), np.uint8)
    cv2.namedWindow("image", (cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO))
    cv2.setMouseCallback("image", draw_Rect)
    dash.drawline(img, (x0, y0), (x1, y0), color, 3, "dashed", 16)

    cv2.imshow("image", img)
    cv2.waitKey(0)
    # capture = ScreenCapture()
    # capture.capture()
    # capture.screen_shot.save("ScreenShot.png")

    # widget = Widget()
    # widget.show()

    # sys.exit(app.exec())
