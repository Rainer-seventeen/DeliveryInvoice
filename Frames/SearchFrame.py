# -*- coding: gbk -*-
import tkinter as tk

class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # �������һ��frame���󣬲���Ҫ����
        tk.Label(self, text="�����ͻ���").pack()
        self.pack()
