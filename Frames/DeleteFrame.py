import tkinter as tk

class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 本身就是一个frame对象，不需要创建
        tk.Label(self, text="删除送货单").pack()
        self.pack()
