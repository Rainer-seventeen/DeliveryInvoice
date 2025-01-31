# -*- coding: gbk -*-
import tkinter as tk

import info
from Frames.AboutFrame import AboutFrame
from Frames.EditFrame import EditFrame
from Frames.DeleteFrame import DeleteFrame
from Frames.RegisterFrame import RegisterFrame
from Frames.SearchFrame import SearchFrame
from Frames.CreateFrame import CreateFrame


class MainPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry(f'{info.WINDOW_LENGTH}x{info.WINDOW_WIDTH}') # WINDOW_LENGTH ,WINDOW_WIDTH
        self.root.title('处理页面')
        self.create_menu()

        # 关于页面
        self.create_frame = tk.Frame(self.root)
        self.search_frame = tk.Frame(self.root)
        self.edit_frame = tk.Frame(self.root)
        self.delete_frame = tk.Frame(self.root)
        self.register_frame = tk.Frame(self.root)
        self.about_frame = tk.Frame(self.root)

        self.search_invoice()

    def create_menu(self):
        """创建菜单"""

        #菜单
        menubar = tk.Menu(self.root)
        menubar.add_command(label='查询',command=self.search_invoice)
        menubar.add_command(label='创建',command=self.create_invoice)
        menubar.add_command(label='修改',command=self.edit_invoice)
        # menubar.add_command(label='删除',command=self.delete_invoice)
        menubar.add_command(label='录入',command=self.register_item)
        menubar.add_command(label='关于',command=self.show_about)


        self.root.config(menu=menubar)

    def destroy_last_page(self):
        """销毁上一个页面"""

        self.about_frame.destroy()
        self.edit_frame.destroy()
        self.delete_frame.destroy()
        self.register_frame.destroy()
        self.search_frame.destroy()
        self.create_frame.destroy()

    def create_invoice(self):
        self.destroy_last_page()
        self.create_frame = CreateFrame(self.root)


    def search_invoice(self):
        self.destroy_last_page()
        self.search_frame = SearchFrame(self.root)

    def edit_invoice(self):
        """修改页面的信息"""
        self.destroy_last_page()
        self.edit_frame = EditFrame(self.root)

    # def delete_invoice(self):
    #     self.destroy_last_page()
    #     self.delete_frame = DeleteFrame(self.root)

    def register_item(self):
        self.destroy_last_page()
        self.register_frame = RegisterFrame(self.root)

    def show_about(self):
        """关于页面的信息"""
        self.destroy_last_page()
        self.about_frame = AboutFrame(self.root)





if __name__ == '__main__':
    root = tk.Tk()
    app = MainPage(master=root)
    app.root.mainloop()
