# -*- coding: gbk -*-

# 显示所有的订单信息
import tkinter as tk
from operator import index
from tkinter import ttk
from tkinter import messagebox

# import info
from operation import Operation
from write import Write
# from info import WINDOW_WIDTH
from info import WINDOW_LENGTH


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.pack(expand=True, fill=tk.BOTH)



        op = Operation()
        self.orders = op.find_order_by_order_no(-1)
        self.orders = op.sort_orders_by_order_no(self.orders)

        ###########################################################################
        # 创建一个输入框框架
        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=10)  # 设置上下和左右的间距
        for i in range(0,10):
            input_frame.columnconfigure(i, weight=1)  # 权重


        # 输入框提示
        company_label = tk.Label(input_frame, text="输入公司名以查询:")
        company_label.grid(row=0, column=0, pady=5, sticky="w")  # 靠左对齐

        # 添加一个输入框，设置列权重
        input_entry = ttk.Entry(input_frame, width=60)
        input_entry.grid(row=0, column=1, columnspan=3, pady=5, sticky="w")  # 靠左扩展

        #创建搜索按钮，在输入框的右侧
        button_company = ttk.Button(
            input_frame,
            text="搜索",
            command=lambda: self.on_search_click(entry_str=input_entry.get())
            )
        button_company.grid(row=0, column=3, pady=5, sticky="e")

        ###########################################################################
        # 第一个框架来包含第一个treeview和滚动条
        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill=tk.BOTH, expand=True, padx = 10, pady=10)  # 设置上下间距为10
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
        self.frame2.pack(fill=tk.BOTH, expand=True, pady=5, padx = 10)
        # 第二个表格基本布局

        self.created_date_and_time = ''
        self.company_address = ''
        self.company_connector_and_phone = ''


        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.frame2.rowconfigure(3, weight=1)
        self.frame2.rowconfigure(4, weight=1)
        self.frame2.columnconfigure(0, weight=1)

        self.choose_label = tk.Label(self.frame2,text='选择订单以显示详情')
        self.choose_label.grid(row=0, column=0, pady=5, sticky="w")
        self.created_date_and_time_label = tk.Label()
        self.company_name_label = tk.Label()
        self.company_address_label = tk.Label()
        self.company_connector_and_phone_label = tk.Label()



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
        self.tree_view2.grid(row=4, column=0, pady=10, sticky="we", padx=(5,15))

        self.show_orders()
        # 鼠标点击事件
        self.tree_view1.bind("<ButtonRelease-1>", self.on_item_click)

        ###########################################################################
        # 第三个框架用于创建系列操作按钮
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, expand=True, pady=0)  # 设置上下间距为10

        for i in range(0,10):
            button_frame.columnconfigure(i, weight=1)  # 权重

        button_company = ttk.Button(
            button_frame,
            text="创建订货单",
            command=self.on_create_click
            )
        button_company.grid(row=0, column=8, pady=5, sticky="ew")


    def show_orders(self, orders=None):
        """
        展示输入orders到表格中，并返回表格中展示的订单号列表
        :param orders: 输入的orders列表，如果不输入则全部展示
        :return: orders_list: 返回表格中展示的订单号列表
        """
        if orders is None:
            orders = self.orders
        for order in orders:
            # print(order) # DEBUG
            self.tree_view1.insert('', index = 'end', values=(
                order['order_no'], order['company_name'], order['created_date'], order['all_total_price']))

    def show_products(self, order_no = None):
        """
        展示第二个列表treeview2内容，以及treeview2上方内容，order_no是订单号
        :param order_no:
        :return:
        """
        if order_no is None:
            pass

        # 清空表格中所有的已经显示的条目
        for item in self.tree_view2.get_children():
            self.tree_view2.delete(item)
        op = Operation()
        clicked_order = op.find_order_by_order_no(order_no) #当前被点击的条目

        # 清空中间栏显示
        self.choose_label.grid_forget()
        self.created_date_and_time_label.grid_forget()
        self.company_name_label.grid_forget()
        self.company_address_label.grid_forget()
        self.company_connector_and_phone_label.grid_forget()
        # 定义显示内容
        created_date_and_time = clicked_order['created_date']+' '+clicked_order['created_time']
        company_name = clicked_order['company_name']
        company_address = clicked_order['company_address']
        company_connector_and_phone = clicked_order['company_connector']+' '+clicked_order['company_phone']

        # 当前条目显示
        self.created_date_and_time_label = tk.Label(self.frame2,text="创建日期及时间："+created_date_and_time)
        self.company_name_label = tk.Label(self.frame2,text='公司名称：'+company_name)
        self.company_address_label = tk.Label(self.frame2,text='公司地址： '+company_address)
        self.company_connector_and_phone_label = tk.Label(self.frame2,text='联系人及电话：'+company_connector_and_phone)
        self.created_date_and_time_label.grid(row=0, column=0, pady=0, sticky="w")
        self.company_name_label.grid(row=1, column=0, pady=0, sticky="w")
        self.company_address_label.grid(row=2, column=0, pady=0, sticky="w")
        self.company_connector_and_phone_label.grid(row=3, column=0, pady=0, sticky="w")

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
        鼠标点击第一个表格触发的事件，重新显示表格数据
        如果没有选中：赋值 self.item_is_selected = False
        :param event:
        :return:如果没有选中，返回 None
        """
        # 获取被点击的项的ID

        selected_item = self.tree_view1.selection()

        if selected_item is None: # 未选中
            for item in self.tree_view2.get_children():
                self.tree_view2.delete(item)
            self.tree_view2.insert("", "end", values=("选中订单以显示详情",))
            return None

        # 获取该项的详细数据
        try:
            item_id = selected_item[0] # treeview内部id，格式：I001
        except IndexError:
            return None
        # print(item_id) # DEBUG
        item_values = self.tree_view1.item(item_id, 'values')

        selected_item_id = item_values[0]  # 'Order No' 是第一列
        # print(order_no) # DEBUG

        if selected_item_id == '未找到结果': # 选中了“未找到”
            for item in self.tree_view2.get_children():
                self.tree_view2.delete(item)
            self.tree_view2.insert("", "end", values=("选中订单以显示详情",))
            return None
        self.show_products(selected_item_id)

    def on_search_click(self, entry_str):
        """
        设置搜索按钮的回调函数，重新显示treeview1
        :param entry_str: 输入的字符串
        :return:
        """

        self.tree_view1.delete(*self.tree_view1.get_children())
        op = Operation()
        orders_no = op.find_order_no_by_company_name(entry_str)    #找到订单号
        # print(orders_no) # DEBUG
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

    def on_create_click(self):
        """
        创建送货单按钮回调函数，根据当前选中的订单启动后续生成等功能
        :param
        :return:
        """
        selected_item = self.treeview1_click()
        if selected_item is None:
            return
        if not messagebox.askyesno('确认','确认生成送货单文件？'):
            return
        op = Operation()
        wt = Write()
        out = op.find_order_by_order_no(selected_item)
        wt.write_docx(out)

    def treeview1_click(self):
        """
        被一系列按钮调用，用于返回当前treeview1选中的那个订单号
        :return:选中的订单号，如果没有则是 None
        """
        op = Operation()
        selected_item = self.tree_view1.selection()
        # selected_order_no = 0
        if len(selected_item) == 0 :
            # 没有选中任何一个条目
            messagebox.showwarning('警告', '未选中订单，请选中订单后重试！')
            return None
        else:
            selected_order_id = selected_item[0] # 内部id
            selected_order_no = self.tree_view1.item(selected_order_id, 'values')[0]
        if op.find_order_by_order_no(selected_order_no) is None:
            # 没有选中正确的订单名称
            messagebox.showwarning('警告','未选中订单，请选中订单后重试！')
            return None
        else:
            print(selected_order_no)
            return selected_order_no


if __name__ == '__main__':
    root = tk.Tk()
    SF = SearchFrame(root)
    SF.on_search_click(entry_str='A')






