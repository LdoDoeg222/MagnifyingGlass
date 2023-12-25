import tkinter as tk
from PIL import ImageGrab, ImageTk

baseW, baseH = 150, 90  # 基础长宽
rate = 4  # 放大倍率


class Viewer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        w, h = baseW * rate, baseH * rate
        self.wm_attributes("-topmost", 1)  # 设置置顶
        self.title("桌面透视工具 By Dy镝（取景框默认生成在左上角）")
        self.geometry("{}x{}".format(w, h))  # 窗口位置

        self.scanner = Scanner(self)
        self.after(func=self.run, ms=10)
        self.canvas = tk.Canvas(self, width=w, height=h)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

    def run(self):
        global immg
        x, y = self.scanner.winfo_x(), self.scanner.winfo_y()
        w, h = self.scanner.w, self.scanner.h
        # 绘制
        grabber = ImageGrab.grab((x, y, x + w, y + h))
        # 需求补充：左半屏不放大，右半屏幕放大
        if x <= 960:
            resize_grabber = grabber
        else:
            resize_grabber = grabber.resize((rate * w, rate * h))
        immg = ImageTk.PhotoImage(resize_grabber)
        self.canvas.create_image(rate * w / 2, rate * h / 2, image=immg)
        self.after(func=self.run, ms=10)


class Scanner(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        w, h = self.w, self.h = baseW, baseH
        color = (255, 255, 0)
        dash = (30, 10)
        self.attributes("-alpha", 0.2)  # 透明度
        self.attributes("-topmost", 1)
        self.overrideredirect(True)  # 取消窗口菜单

        # 虚线框
        canvas = self.canvas = tk.Canvas(self, width=w, height=h)
        canvas.pack()
        canvas.create_line(0, 0, w, 0, width=6, dash=dash)
        canvas.create_line(0, 0, 0, h, width=6, dash=dash)
        canvas.create_line(w, h, w, 0, width=6, dash=dash)
        canvas.create_line(w, h, 0, h, width=6, dash=dash)

        self.geometry("{}x{}".format(w, h))

        # 绑定鼠标
        self.bind("<ButtonPress-1>", self.start_dragging)
        self.bind("<ButtonRelease-1>", self.stop_dragging)
        self.bind("<B1-Motion>", self.do_dragging)

        self.x = 0
        self.y = 0
        # self.after(func=self.run, ms=10)

    def start_dragging(self, event):  # 记录起点 x, y
        self.x = event.x
        self.y = event.y

    def stop_dragging(self, event):  # 归零
        self.x = 0
        self.y = 0

    def do_dragging(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        # print(f"+{self.x}+{self.y}")  # 窗内触点绝对 xy
        # print(f"+{event.x}+{event.y}")  # 窗内移动绝对 xy
        # print(f"+{self.winfo_x()}+{self.winfo_y()}")  # 窗口之于屏幕 xy
        # print(f"+{deltax}+{deltay}")  # 相对 xy
        self.geometry(f"+{new_x}+{new_y}")

    # def run(self):
    #     global immg
    #     x, y = self.winfo_x(), self.winfo_y()
    #     xx = ImageGrab.grab((x, y, x + self.w, y + self.h))
    #     immg = ImageTk.PhotoImage(xx)
    #     self.canvas.create_image(rate * self.w / 2, rate * self.h / 2, image=immg)
    #     self.after(func=self.run, ms=10)


if __name__ == "__main__":
    glass = Viewer()
    glass.mainloop()
