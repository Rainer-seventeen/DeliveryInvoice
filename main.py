# -*- coding: gbk -*-
import tkinter as tk
from Frames.AboutFrame import AboutFrame
from Frames.EditFrame import EditFrame
from Frames.DeleteFrame import DeleteFrame
from Frames.RegisterFrame import RegisterFrame
from Frames.SearchFrame import SearchFrame
from Frames.CreateFrame import CreateFrame


class MainPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry('1000x700')
        self.root.title('����ҳ��')
        self.create_menu()

        # ����ҳ��
        self.create_frame = tk.Frame(self.root)
        self.search_frame = tk.Frame(self.root)
        self.edit_frame = tk.Frame(self.root)
        self.delete_frame = tk.Frame(self.root)
        self.register_frame = tk.Frame(self.root)
        self.about_frame = tk.Frame(self.root)

    def create_menu(self):
        """�����˵�"""

        #�˵�
        menubar = tk.Menu(self.root)
        menubar.add_command(label='�½�',command=self.create_invoice)
        menubar.add_command(label='��ѯ',command=self.search_invoice)
        menubar.add_command(label='�޸�',command=self.edit_invoice)
        menubar.add_command(label='ɾ��',command=self.delete_invoice)
        menubar.add_command(label='¼��',command=self.register_item)
        menubar.add_command(label='����',command=self.show_about)


        self.root.config(menu=menubar)

    def destroy_last_page(self):
        """������һ��ҳ��"""
        # ����ÿ��ҳ�棬���ҳ���Ѿ���������ʾ�ڽ�����
        if hasattr(self, 'create_frame') and self.create_frame.winfo_ismapped():
            self.create_frame.destroy()
        if hasattr(self, 'search_frame') and self.search_frame.winfo_ismapped():
            self.search_frame.destroy()
        if hasattr(self, 'edit_frame') and self.edit_frame.winfo_ismapped():
            self.edit_frame.destroy()
        if hasattr(self, 'delete_frame') and self.delete_frame.winfo_ismapped():
            self.delete_frame.destroy()
        if hasattr(self, 'register_frame') and self.register_frame.winfo_ismapped():
            self.register_frame.destroy()
        if hasattr(self, 'about_frame') and self.about_frame.winfo_ismapped():
            self.about_frame.destroy()

    def create_invoice(self):
        self.destroy_last_page()
        self.create_frame = CreateFrame(self.root)
        self.create_frame.create_ui()


    def search_invoice(self):
        self.destroy_last_page()
        self.search_frame = SearchFrame(self.root)

    def edit_invoice(self):
        """�޸�ҳ�����Ϣ"""
        self.destroy_last_page()
        self.edit_frame = EditFrame(self.root)

    def delete_invoice(self):
        self.destroy_last_page()
        self.delete_frame = DeleteFrame(self.root)

    def register_item(self):
        self.destroy_last_page()
        self.register_frame = RegisterFrame(self.root)

    def show_about(self):
        """����ҳ�����Ϣ"""
        self.destroy_last_page()
        self.about_frame = AboutFrame(self.root)





if __name__ == '__main__':
    root = tk.Tk()
    app = MainPage(master=root)
    app.root.mainloop()
