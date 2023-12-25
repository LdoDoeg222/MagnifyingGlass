# 实体窗、虚体可拖拽边边窗、双窗口

import tkinter as tk
import tkinter.ttk as ttk


class Example(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)


class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.wm_geometry("400x400")

        self.label = tk.Label(self, text="Grab the lower-right corner to resize")
        self.label.pack(side="top", fill="both", expand=True)
        

        self.grip = ttk.Sizegrip(self)
        self.grip.place(relx=1.0, rely=1.0, anchor="se")
        self.grip2 = ttk.Sizegrip(self)
        self.grip2.place(x=0, rely=1.0, anchor="sw")
        # self.grip3 = ttk.Sizegrip(self)
        # self.grip3.place(relx=0, rely=1.0, anchor="sw")
        self.grip4 = ttk.Sizegrip(self)
        self.grip4.place(x=0, y=0, anchor="nw")
        # self.grip.lift(self.label)
        self.grip.bind("<B1-Motion>", self.OnMotion)

    def OnMotion(self, event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry("%sx%s" % ((x1 - x0), (y1 - y0)))
        return


app = Example()
app.mainloop()
