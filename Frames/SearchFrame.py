# -*- coding: gbk -*-

# 显示所有的订单信息
import tkinter as tk
from tkinter import ttk
from unittest import skipIf

from operation import Operation
from info import WINDOW_WIDTH
from info import WINDOW_LENGTH


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.pack()



        op = Operation()
        self.orders = op.find_order_by_order_no(-1)
        self.orders = op.sort_orders_by_order_no(self.orders)

        # TODO 创建一个输入框，完成input_frame对于treeview1显示的数值的控制

        # 创建一个输入框框架
        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=10)  # 设置上下和左右的间距
        for i in range(0,10):
            input_frame.columnconfigure(i, weight=1)  # 第一列权重


        # 输入框提示
        company_label = tk.Label(input_frame, text="输入公司名以查询:")
        company_label.grid(row=0, column=0, pady=5, sticky="w")  # 靠左对齐

        # 添加一个输入框，设置列权重
        input_entry = tk.Entry(input_frame, width=60)
        input_entry.grid(row=0, column=1, columnspan=3, pady=5, sticky="w")  # 靠左扩展

        #创建搜索按钮，在输入框的右侧
        button_company = tk.Button(
            input_frame,
            text="搜索",
            command=lambda: self.on_search_click(entry_str=input_entry.get())
            )
        button_company.grid(row=0, column=4, pady=5, sticky="w")





        ###########################################################################
        # 第一个框架来包含第一个treeview和滚动条
        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill=tk.BOTH, expand=True, pady=10)  # 设置上下间距为10
        # 第一个表格基本布局
        columns1 = ("order_no", "company_name", "created_date", "all_total_price")
        self.tree_view1 = ttk.Treeview(self.frame1, columns=columns1, show="headings")
        self.tree_view1.column('order_no', width=int(0.15 * WINDOW_LENGTH), anchor='center')
        self.tree_view1.column('company_name', width=int(0.4 * WINDOW_LENGTH), anchor='center')
        self.tree_view1.column('created_date', width=int(0.25 * WINDOW_LENGTH), anchor='center')
        self.tree_view1.column('all_total_price', width=int(0.15 * WINDOW_LENGTH), anchor='center')

        self.tree_view1.heading('order_no', text='订单号')
        self.tree_view1.heading('company_name', text='公司名称')
        self.tree_view1.heading('created_date', text='创建日期')
        self.tree_view1.heading('all_total_price', text='订单总价')

        # 创建第一个滚动条
        scrollbar1 = tk.Scrollbar(self.frame1, orient="vertical", command=self.tree_view1.yview)
        self.tree_view1.configure(yscrollcommand=scrollbar1.set)

        # 布局：第一个treeview填充frame，滚动条放在右侧
        self.tree_view1.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar1.pack(side="right", fill="y")

        ###########################################################################
        # 创建第二个框架来包含第二个treeview和滚动条
        self.frame2 = tk.Frame(self)
        self.frame2.pack(fill=tk.BOTH, expand=True,  pady=20)
        # 第二个表格基本布局

        columns2 = ("product_name", "product_standard", "product_unit", "quantity","unit_price", "total_price", "product_description")
        self.tree_view2 = ttk.Treeview(self.frame2, columns=columns2, show="headings")
        self.tree_view2.column('product_name', width=int(0.3 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('product_standard', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('product_unit', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('quantity', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('unit_price', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('total_price', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('product_description', width=int(0.1 * WINDOW_LENGTH), anchor='center')


        self.tree_view2.heading('product_name', text='产品名称')
        self.tree_view2.heading('product_standard', text='产品标准')
        self.tree_view2.heading('product_unit', text='单位')
        self.tree_view2.heading('quantity', text='数量')
        self.tree_view2.heading('unit_price', text='单价')
        self.tree_view2.heading('total_price', text='总价')
        self.tree_view2.heading('product_description', text='备注')

        #表格2布局
        self.tree_view2.pack(side="left", fill=tk.BOTH, expand=True)

        self.show_orders()
        # 鼠标点击事件
        self.tree_view1.bind("<ButtonRelease-1>", self.on_item_click)




    def show_orders(self, orders=None):
        """
        展示输入orders到表格中，并返回表格中展示的订单号列表
        :param orders: 输入的orders列表，如果不输入则全部展示
        :return: orders_list: 返回表格中展示的订单号列表
        """
        if orders is None:
            orders = self.orders
        for order in orders:
            print(order) # DEBUG
            self.tree_view1.insert('', index = 'end', values=(
                order['order_no'], order['company_name'], order['created_date'], order['all_total_price']))

    def show_products(self, order_no = None):
        """
        展示第二个列表treeview2内容，order_no是订单号
        :param order_no:
        :return:
        """
        if order_no is None:
            pass

        # 先清空所有的已经显示的条目
        for item in self.tree_view2.get_children():
            self.tree_view2.delete(item)
        op = Operation()
        clicked_order = op.find_order_by_order_no(order_no) #当前被点击的条目
        products = clicked_order['Products'] # 当前送货单的产品
        for product in products:
            # print(product) # DEBUG
            self.tree_view2.insert('', index = 'end',
                                   values=(
                                            product['product_name'], product['product_standard'],
                                            product['product_unit'], product['quantity'],
                                            product['unit_price'], product['total_price'],
                                            product['product_description']
                                    ))

    def on_item_click(self, event = None):
        """
        鼠标点击触发的事件，涉及到重新显示表格数据
        :param event:
        :return:
        """
        # 获取被点击的项的ID
        selected_item = self.tree_view1.selection()
        if selected_item is None:
            pass
        # 获取该项的详细数据
        item_id = selected_item[0]
        item_values = self.tree_view1.item(item_id, 'values')
        order_no = item_values[0]  # 'Order No' 是第一列
        print(order_no)
        self.show_products(order_no)

    def on_search_click(self, entry_str, event = None):
        """
        设置搜索按钮的回调函数，重新显示treeview1
        :param entry_str: 输入的字符串
        :param event: 无
        :return:
        """

        self.tree_view1.delete(*self.tree_view1.get_children())
        op = Operation()
        orders_no = op.find_order_no_by_company_name(entry_str)    #找到订单号
        # print(orders_no)
        orders_to_show = []
        if len(entry_str) == 0:
            # 如果没输入就全部显示
            orders_to_show = self.orders
        elif len(orders_no) == 0:
            # 如果没有找到结果未找到
            self.tree_view1.insert("", "end", values=("未找到结果",))
            pass
        else:
            for order_no in orders_no:
                orders_to_show.append(op.find_order_by_order_no(order_no))

        orders_to_show = op.sort_orders_by_order_no(orders_to_show)
        self.show_orders(orders_to_show)

        # print(orders_to_show)


if __name__ == '__main__':
    root = tk.Tk()
    SF = SearchFrame(root)
    SF.on_search_click(entry_str='A')






