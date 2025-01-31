# -*- coding: gbk -*-
import tkinter as tk
import copy
from tkinter import ttk
from tkinter import messagebox
# from venv import create

from operation import Operation
from write import Write
# from info import CURRENT_FOLDER
# from info import WINDOW_WIDTH
from info import WINDOW_LENGTH

class CreateFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        #初始化self总框架
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=12)
        self.columnconfigure(0, weight=1)  # 表格区域列权重为1

        # 初始化数据列表
        self.INIT_STR = '输入产品（如没有则不改）'
        rows = 6
        cols = 6
        self.data = [['' for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            self.data[r][0] = self.INIT_STR

        ###########################################################################
        # 创建输入框框架
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row=0, column=0, sticky='nsew')
        for i in range(0,5):
            self.input_frame.columnconfigure(i, weight=1)  # 权重

        self.entry_company = tk.Entry(self.input_frame, width=60)
        self.entry_company.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展
        name_label_company = tk.Label(self.input_frame, text="公司名称:")
        name_label_company.grid(row=1, column=0, pady=5, sticky="we")  # 靠左对齐

        self.entry_address = tk.Entry(self.input_frame, width=60)
        self.entry_address.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")
        name_label_address = tk.Label(self.input_frame,text='地址名称:')
        name_label_address.grid(row=2, column=0, pady=5, sticky="we")

        self.entry_phone = tk.Entry(self.input_frame, width=60)
        self.entry_phone.grid(row=3, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展
        name_label_phone = tk.Label(self.input_frame, text="客户电话:")
        name_label_phone.grid(row=3, column=0, pady=5, sticky="we")  # 靠左对齐

        self.entry_connector = tk.Entry(self.input_frame, width=60)
        self.entry_connector.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")  # 靠左扩展
        name_label_connector = tk.Label(self.input_frame, text="联系人:")
        name_label_connector.grid(row=4, column=0, pady=5, sticky="we")  # 靠左对齐


        ###########################################################################
        # 创建表格区域
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=1, column=0, sticky="ew")  # 取消垂直扩展

        # 配置表格区域的网格权重
        self.table_frame.rowconfigure(0, weight=1)  # 表格行权重为1
        self.table_frame.columnconfigure(0, weight=1)  # 表格列权重为1

        # 创建Treeview
        columns = ("product_name", "product_standard", "product_unit", "quantity","unit_price","product_description")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.tree.grid(row=0, column=0, sticky="ew")

        # # 滚动条
        # vsb = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        # vsb.grid(row=0, column=1, sticky="ns")  # 滚动条紧贴右侧
        # self.tree.configure(yscrollcommand=vsb.set)


        # 列设置
        self.tree.column('product_name', width=int(0.3 * WINDOW_LENGTH), anchor='center')
        self.tree.column('product_standard', width=int(0.2 * WINDOW_LENGTH), anchor='center')
        self.tree.column('product_unit', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.column('quantity', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.column('unit_price', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.column('product_description', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.heading('product_name', text='产品名称')
        self.tree.heading('product_standard', text='产品标准')
        self.tree.heading('product_unit', text='单位')
        self.tree.heading('quantity', text='数量')
        self.tree.heading('unit_price', text='单价')
        self.tree.heading('product_description', text='备注')

        # 计算表格高度
        # self.adjust_table_height(6)  # 设置显示6行

        # 初始数据
        for row in range(rows):
            self.tree.insert("", "end", values=self.data[row])

        # 事件绑定
        self.tree.bind("<Button-1>", self.on_table_click)

        # 编辑控件
        self.entry_frame = ttk.Frame(self)  # 新增容器框架
        self.entry = ttk.Entry(self.entry_frame)
        # self.btn = ttk.Button(self.entry_frame, text="▼", width=2,
        #                       command=self.show_history_list)
        self.listbox = tk.Listbox(self)  # 下拉列表
        self.current_edit = None

        ###########################################################################
        # 按钮框架
        button_frame = ttk.Frame(self)
        button_frame.grid(row=3, column=0, sticky='ew')
        for i in range(0,10):
            button_frame.columnconfigure(i, weight=1)  # 权重

        save_button = tk.Button(button_frame,text='保存',command=lambda :self.on_save_click())
        save_button.grid(row=0, column=2, pady=5, sticky="w")

    def on_table_click(self, event):
        # 如果当前有正在编辑的单元格，先保存内容
        if self.current_edit:
            self.save_edit(*self.current_edit)  # 保存当前编辑内容

        # 获取位置信息
        row_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)

        if not row_id or column == "#0":
            return

        # 获取坐标
        col_index = int(column[1:]) - 1
        row_index = int(self.tree.index(row_id))
        x, y, width, height = self.tree.bbox(row_id, column)

        # 转换为根窗口坐标
        table_x = self.table_frame.winfo_x()
        table_y = self.table_frame.winfo_y()
        abs_x = table_x + x
        abs_y = table_y + y

        # 设置输入框位置
        self.entry_frame.place(x=abs_x, y=abs_y, width=width, height=height)
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.btn.pack(side=tk.RIGHT, fill=tk.Y)

        # 初始值
        value = self.data[row_index][col_index]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
        self.entry.focus_set()

        # 绑定事件
        self.entry.bind("<Return>", lambda e: self.save_edit(row_id, column, row_index, col_index))
        self.entry.bind("<FocusOut>", lambda e: self.save_edit(row_id, column, row_index, col_index))
        self.current_edit = (row_id, column, row_index, col_index)

    def save_edit(self, row_id, column, row_index, col_index):
        new_value = self.entry.get()
        self.entry_frame.place_forget()
        self.listbox.place_forget()

        self.data[row_index][col_index] = new_value
        self.tree.set(row_id, column=column, value=new_value)

    def on_save_click(self):
        """
        保存按钮的回调函数，触发写入功能
        :return:
        """
        company = self.entry_company.get()
        address = self.entry_phone.get()
        phone = self.entry_phone.get()
        connector = self.entry_connector.get()
        matrix = self.matrix_from_data()
        if not self.check_entry_empty(company, address, phone, connector, matrix):
            return
        if not messagebox.askyesno('确认', '确认保存当前送货单？'):
            return
        wt = Write()
        wt.add_new_invoice(company, address, phone, connector, matrix)
    @staticmethod
    def check_entry_empty(company,address,phone,connector,matrix):
        """
        检查输入是否合法
        :return: True / False
        """
        if company.strip() == "":
            messagebox.showwarning('警告', '公司名称未填写')
            return False
        if address.strip() == "":
            messagebox.showwarning('警告', '公司地址未填写')
            return False
        if phone.strip() == "":
            messagebox.showwarning('警告', '客户电话未填写')
            return False
        if connector.strip() == "":
            messagebox.showwarning('警告', '联系人未填写')
            return False
        for row in range(0,len(matrix)-1):
            is_empty = True
            if matrix[row][0].strip() != "":
                is_empty = False
                if not matrix[row][3].strip().isdigit():
                    messagebox.showwarning('警告', f"第{row + 1}行产品数量不正确")
                if not matrix[row][4].strip().replace('.', '', 1).isdigit():
                    messagebox.showwarning('警告', f"第{row + 1}行产品单价不正确")
                print('Check Entry: PASS') # DEBUG
                return True

        messagebox.showwarning('警告', "至少添加一项产品")
        return False

    def matrix_from_data(self):
        """
        创建一个 matrix 给 on_create_click 使用，
        :return: matrix
        """
        matrix = copy.deepcopy(self.data)
        for row in matrix:
            if row[0] == self.INIT_STR:
                row[0] = ''
        return matrix


