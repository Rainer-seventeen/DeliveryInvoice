import tkinter as tk

class RegisterFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 本身就是一个frame对象，不需要创建
        tk.Label(self, text="录入产品").pack()
        self.pack()
