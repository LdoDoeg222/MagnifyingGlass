# 最现代放大镜

import tkinter
from PIL import ImageGrab, ImageTk
from pynput import mouse


control = mouse.Controller()
glass = tkinter.Tk()
# screenW = tk.winfo_screenwidth()
# screenH = tk.winfo_screenheight()
glass.geometry("500x300")
glass.wm_attributes("-topmost", 1)  # [0]

glass.overrideredirect(True)  # 不显示标题栏 # [1]

hw, hh = 100, 60
rate = 4
halfrate = rate / 2
dash = (30, 10)


def glassRun():
    global immg  #   [2]全局化图像对象，避免销毁导致闪烁
    x, y = control.position  #   [3]获取鼠标坐标
    scanX, scanY = 0, 0  #   扫描窗左上点
    # xx = ImageGrab.grab((scanX, scanY, scanX + hw, scanY + hh))
    xx = ImageGrab.grab((x - hw, y - hh, x + hw, y + hh))
    # xx = ImageGrab.grab((hw - hw, hh - hh, hw + hw, hh + hh))
    xxx = xx.resize((rate * hw, rate * hh))
    immg = ImageTk.PhotoImage(xxx)  # 全屏抓取
    canvas.create_image(halfrate * hw, halfrate * hh, image=immg)  #   [4]画布从中心点开始绘制
    glass.geometry(
        "{}x{}+{}+{}".format(rate * hw, rate * hh, x + hw, y + hh)
    )  # [5]不断刷新放大镜窗口的位置
    # tk.geometry(
    #     "{}x{}+{}+{}".format(10 * hw, 10 * hh, x + hw, y + hh)
    # )  # [5]不断刷新放大镜窗口的位置
    glass.after(func=glassRun, ms=10)


glass.after(func=glassRun, ms=10)
scanner = tkinter.Toplevel(glass)
scanner.overrideredirect(True)  # 不显示标题栏 # [1]
scanner.geometry("{}x{}".format(hw, hh))
canvas = scanner.canvas = tkinter.Canvas(scanner, width=hw, height=hh)
canvas.pack()
canvas.create_line(0, 0, hw, 0, width=6, dash=dash)
canvas.create_line(0, 0, 0, hh, width=6, dash=dash)
canvas.create_line(hw, hh, hw, 0, width=6, dash=dash)
canvas.create_line(hw, hh, 0, hh, width=6, dash=dash)


def scannerRun():
    scanner.geometry("{}x{}".format(hw, hh))
    scanner.after(func=scannerRun, ms=10)


scanner.x = 0
scanner.y = 0


scanner.after(func=scannerRun, ms=10)
canvas = tkinter.Canvas(glass, width=hw * rate, height=hh * rate)  # 创建白色画布
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)  # 画布放置至窗体
glass.mainloop()
