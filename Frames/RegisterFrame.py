# -*- coding: gbk -*-
import tkinter as tk

class RegisterFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # �������һ��frame���󣬲���Ҫ����
        tk.Label(self, text="¼���Ʒ").pack()
        self.pack()
