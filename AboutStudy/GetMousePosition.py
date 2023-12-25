# 获取鼠标位置

import pyautogui

while True:
    x, y = pyautogui.position()
    print('X: %s, Y: %s' % (x, y))