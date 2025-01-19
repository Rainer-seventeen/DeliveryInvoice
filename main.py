import tkinter as tk
from Frames.AboutFrame import AboutFrame

class MainPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry('1000x700')
        self.root.title('处理页面')
        self.create_menu()

        # 关于页面
        self.create_frame = tk.Frame(self.root)
        self.search_frame = tk.Frame(self.root)
        self.edit_frame = tk.Frame(self.root)
        self.delete_frame = tk.Frame(self.root)
        self.register_frame = tk.Frame(self.root)
        self.about_frame = tk.Frame(self.root)

    def create_menu(self):
        """创建菜单"""

        #菜单
        menubar = tk.Menu(self.root)
        menubar.add_command(label='新建',command=self.create_invoice)
        menubar.add_command(label='查询',command=self.search_invoice)
        menubar.add_command(label='修改',command=self.edit_invoice)
        menubar.add_command(label='删除',command=self.delete_invoice)
        menubar.add_command(label='录入',command=self.register_item)
        menubar.add_command(label='关于',command=self.show_about)


        self.root.config(menu=menubar)

    def destroy_last_page(self):
        """销毁上一个页面"""
        # 销毁每个页面，如果页面已经创建并显示在界面上
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
        pass

    def search_invoice(self):
        pass

    def edit_invoice(self):
        pass

    def delete_invoice(self):
        pass

    def register_item(self):
        pass

    def show_about(self):
        """关于页面的信息"""
        self.destroy_last_page()
        self.about_frame = AboutFrame(self.root)





if __name__ == '__main__':
    root = tk.Tk()
    app = MainPage(master=root)
    app.root.mainloop()
