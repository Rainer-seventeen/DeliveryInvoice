import tkinter as tk
from venv import create

from info import CURRENT_FOLDER

class CreateFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 本身就是一个frame对象，不需要创建
        # tk.Label(self, text="创建送货单").pack()
        # self.pack()


    def create_ui(self):
        # ------ Company 输入组件 ------
        dropdown_var_company = tk.StringVar()
        entry_company = tk.Entry(self.master, width=60)

        # # 下拉菜单
        # dropdown_menu_company = tk.OptionMenu(self.master, dropdown_var_company, "暂无历史记录")
        # dropdown_menu_company.grid(row=0, column=3, columnspan=2, pady=5, sticky="w")  # 靠左对齐

        # # 绑定公司下拉逻辑
        # bind_dropdown_action(dropdown_var_company, entry_company)

        # 标签
        name_label_company = tk.Label(self.master, text="公司名称:")
        name_label_company.grid(row=0, column=0, pady=5, sticky="we")  # 靠左对齐

        # 输入框
        entry_company.grid(row=0, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展

        # 提交按钮，放在输入框右侧
        button_company = tk.Button(self.master, text="提交公司")
        button_company.grid(row=0, column=5, padx=10, pady=5, sticky="we")  # 靠输入框右边


        #############################################################################
        # ------ Address 输入组件 ------
        dropdown_var_address = tk.StringVar()
        entry_address = tk.Entry(self.master, width=60)

        # # 下拉菜单
        # dropdown_menu_address = tk.OptionMenu(self.master, dropdown_var_address, "暂无历史记录")
        # dropdown_menu_address.grid(row=2, column=3, columnspan=2, pady=5, sticky="w")  # 靠左对齐
        #
        # # 绑定地址下拉逻辑
        # bind_dropdown_action(dropdown_var_address, entry_address)

        # 标签
        name_label_address = tk.Label(self.master, text="地址名称:")
        name_label_address.grid(row=2, column=0, pady=5, sticky="we")  # 靠左对齐

        # 输入框
        entry_address.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展

        # 提交按钮，与输入框同列同行右侧
        button_address = tk.Button(self.master,text="提交地址",)
        button_address.grid(row=2, column=5, padx=10, pady=5, sticky="we")  # 靠输入框右边

        # # 确认按钮，与地址提交按钮同行右侧
        # confirm_address = tk.Button(
        #     root,
        #     text="确认地址",
        #     command=lambda: print_to_console(entry_address.get())
        # )
        # confirm_address.grid(row=3, column=5, padx=10, pady=5, sticky="we")  # 靠提交按钮右边
        #############################################################################
        # 电话与联系人输入框
        name_label_phone = tk.Label(self.master, text="客户电话:")
        name_label_phone.grid(row=3, column=0, pady=5, sticky="we")  # 靠左对齐
        entry_phone = tk.Entry(self.master, width=60)
        entry_phone.grid(row=3, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展

        name_label_connector = tk.Label(self.master, text="联系人:")
        name_label_connector.grid(row=4, column=0, pady=5, sticky="we")  # 靠左对齐
        entry_connector = tk.Entry(self.master, width=60)
        entry_connector.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展

        #############################################################################
        # ------ 批量6x8输入框布局 ------
        input_vars = []
        labels = ("产品名称", "规格型号", "单位", "数量", "单价", "备注")
        for i in range(6):
            name_label_company = tk.Label(self.master, text=labels[i])
            name_label_company.grid(row=5, column=i, pady=5, sticky="we")  # 靠左对齐

        file_path = rf"{CURRENT_FOLDER}{r"\output.txt"}"  # txt文件的路径
        # 添加 6x8 输入框
        for i in range(8):  # 8行
            row_vars = []
            for j in range(6):  # 每行6个
                var = tk.StringVar()
                entry = tk.Entry(self.master, textvariable=var, width=30)
                entry.grid(row=6 + i, column=j, padx=5, pady=5, sticky="w")
                row_vars.append(var)
            input_vars.append(row_vars)

        confirm_export = tk.Button(self.master,text="导出所有数据")
        confirm_export.grid(row=14, column=4, columnspan=1, pady=10, sticky="we")

        file_path_docx = rf"{CURRENT_FOLDER}{r"\framework.docx"}"  # word 模板文件路径
        output_path = rf"{CURRENT_FOLDER}{r"\生成后送货单.docx"}"
        button_generate_docx = tk.Button(
            self.master,
            text="生成送货单",
            command=lambda: tk.messagebox.askyesno(
                "确认导入",
                "确认已经导出数据，生成送货单？"
            )
        )
        button_generate_docx.grid(row=16, column=4, columnspan=1, pady=10, sticky="we")  # 靠输入框右边

        button_import_database = tk.Button(
            self.master,
            text="导入数据库",

            command=lambda: tk.messagebox.askyesno(
                "确认导入",
                "请确认是否写入数据库？"
            )
        )
        button_import_database.grid(row=17, column=4, columnspan=1, pady=10, sticky="we")  # 靠输入