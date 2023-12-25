import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# # 绘制实线
canvas.create_line(0, 0, 200, 200, width=2)

# # 绘制虚线
canvas.create_line(0, 100, 200, 300, width=2, dash=(10,5))

root.mainloop()
