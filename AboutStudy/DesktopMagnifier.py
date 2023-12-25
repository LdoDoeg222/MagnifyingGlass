from PIL import ImageTk, ImageGrab
import tkinter as tk


class DesktopMagnifier:
    def __init__(self):
        self.root = tk.Tk()

        # self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 1)
        self.root.attributes("-topmost", 1)
        self.root.overrideredirect(True)
        self.canvas = tk.Canvas(
            self.root,
            # width=self.root.winfo_screenwidth(),
            # height=self.root.winfo_screenheight(),
        )
        self.canvas.pack()
        self.canvas.bind("<Motion>", self.onMouseMove)
        self.root.mainloop()

    def onMouseMove(self, event):
        x, y = int(event.x), int(event.y)
        radius = 50
        left, right, bottom, top = x - radius, x + radius, y - radius, y + radius
        screen_shot = ImageGrab.grab()
        screen_shot = screen_shot.crop((left, bottom, right, top))
        screen_shot = screen_shot.resize(
            (200, 200), ImageTk.PhotoImage(screen_shot).paste(screen_shot)
        )
        self.canvas.delete(tk.ALL)
        self.canvas.create_image(
            x, y, anchor=tk.CENTER, image=ImageTk.PhotoImage(screen_shot)
        )
        self.canvas.create_rectangle(left, bottom, right, top, outline="#000000")


if __name__ == "__main__":
    magnifier = DesktopMagnifier()
