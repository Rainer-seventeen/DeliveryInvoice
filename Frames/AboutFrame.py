# -*- coding: gbk -*-
import tkinter as tk

class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # �������һ��frame���󣬲���Ҫ����
        tk.Label(self, text="���ڱ�����ʹ��tkinter����").pack()
        tk.Label(self, text="�������ߣ�Rainer17").pack()
        self.pack()
