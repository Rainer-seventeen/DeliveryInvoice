# -*- coding: gbk -*-
import tkinter as tk

class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 本身就是一个frame对象，不需要创建
        tk.Label(self, text="查找送货单").pack()
        self.pack()
