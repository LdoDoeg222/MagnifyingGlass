# 截全屏存储

from PIL import ImageGrab


class ScreenCapture:
    def __init__(self):
        self.screen_shot = None

    def capture(self):
        self.screen_shot = ImageGrab.grab()


if __name__ == "__main__":
    capture = ScreenCapture()
    capture.capture()
    capture.screen_shot.save("ScreenShot.png")
