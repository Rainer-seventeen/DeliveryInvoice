# -*- coding: gbk -*-
import tkinter as tk

class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # �������һ��frame���󣬲���Ҫ����
        tk.Label(self, text="ɾ���ͻ���").pack()
        self.pack()
