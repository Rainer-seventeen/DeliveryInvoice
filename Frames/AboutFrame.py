import tkinter as tk

class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 本身就是一个frame对象，不需要创建
        tk.Label(self, text="关于本作：使用tkinter制作").pack()
        tk.Label(self, text="关于作者：Rainer17").pack()
        self.pack()
