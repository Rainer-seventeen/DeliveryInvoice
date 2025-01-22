# -*- coding: gbk -*-

# 显示所有的订单信息
import tkinter as tk
from tkinter import ttk
from operation import Operation


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.pack()

        op = Operation()
        self.orders = op.find_order_by_order_no(-1)

        # # 创建一个输入框框架
        # input_frame = tk.Frame(self)
        # input_frame.pack(fill=tk.X, padx=10, pady=10)  # 设置上下和左右的间距
        #
        # # 添加一个输入框
        # self.input_entry = tk.Entry(input_frame)
        # self.input_entry.grid(side="left", fill=tk.X, expand=True)

        # 创建第一个框架来包含第一个treeview和滚动条
        frame1 = tk.Frame(self)
        frame1.pack(fill=tk.BOTH, expand=True, pady=10)  # 设置上下间距为10

        # 第一个表格基本布局
        columns = ("order_no", "company_name", "created_date", "all_total_price")
        self.tree_view1 = ttk.Treeview(frame1, columns=columns, show="headings")
        self.tree_view1.column('order_no', width=150, anchor='center')
        self.tree_view1.column('company_name', width=400, anchor='center')
        self.tree_view1.column('created_date', width=250, anchor='center')
        self.tree_view1.column('all_total_price', width=150, anchor='center')

        self.tree_view1.heading('order_no', text='订单号')
        self.tree_view1.heading('company_name', text='公司名称')
        self.tree_view1.heading('created_date', text='创建日期')
        self.tree_view1.heading('all_total_price', text='订单总价')

        # 创建第一个滚动条
        scrollbar1 = tk.Scrollbar(frame1, orient="vertical", command=self.tree_view1.yview)
        self.tree_view1.configure(yscrollcommand=scrollbar1.set)

        # 布局：第一个treeview填充frame，滚动条放在右侧
        self.tree_view1.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar1.pack(side="right", fill="y")

        # 创建第二个框架来包含第二个treeview和滚动条
        frame2 = tk.Frame(self)
        frame2.pack(fill=tk.BOTH, expand=True,  pady=20)
        # 第二个表格基本布局
        self.tree_view2 = ttk.Treeview(frame2, columns=columns, show="headings")
        self.tree_view2.column('order_no', width=150, anchor='center')
        self.tree_view2.column('company_name', width=400, anchor='center')
        self.tree_view2.column('created_date', width=250, anchor='center')
        self.tree_view2.column('all_total_price', width=150, anchor='center')

        self.tree_view2.heading('order_no', text='订单号')
        self.tree_view2.heading('company_name', text='公司名称')
        self.tree_view2.heading('created_date', text='创建日期')
        self.tree_view2.heading('all_total_price', text='订单总价')

        #表格2布局
        self.tree_view2.pack(side="left", fill=tk.BOTH, expand=True)
        self.show_data()



    def show_data(self,orders = None):
        """
        展示输入orders到表格中
        :param orders: 输入的orders列表，如果不输入则全部展示
        :return:
        """
        if orders is None:
            orders = self.orders
        index = 0
        for order in orders:
            print(order)
            self.tree_view1.insert('', index+1, values=(
                                  order['order_no'],order['company_name'],order['created_date'],order['all_total_price'])
                                  )
        # 订单号，公司名，创建日期，总价



