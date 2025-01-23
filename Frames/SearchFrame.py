# -*- coding: gbk -*-

# ��ʾ���еĶ�����Ϣ
import tkinter as tk
from tkinter import ttk
from operation import Operation
from info import WINDOW_WIDTH
from info import WINDOW_LENGTH


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.pack()



        op = Operation()
        self.orders = op.find_order_by_order_no(-1)


        # # ����һ���������
        # input_frame = tk.Frame(self)
        # input_frame.pack(fill=tk.X, padx=10, pady=10)  # �������º����ҵļ��
        #
        # # ���һ�������
        # self.input_entry = tk.Entry(input_frame)
        # self.input_entry.grid(side="left", fill=tk.X, expand=True)

        ###########################################################################
        # ������һ�������������һ��treeview�͹�����
        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill=tk.BOTH, expand=True, pady=10)  # �������¼��Ϊ10
        # ��һ������������
        columns1 = ("order_no", "company_name", "created_date", "all_total_price")
        self.tree_view1 = ttk.Treeview(self.frame1, columns=columns1, show="headings")
        self.tree_view1.column('order_no', width=int(0.15 * WINDOW_LENGTH), anchor='center')
        self.tree_view1.column('company_name', width=int(0.4 * WINDOW_LENGTH), anchor='center')
        self.tree_view1.column('created_date', width=int(0.25 * WINDOW_LENGTH), anchor='center')
        self.tree_view1.column('all_total_price', width=int(0.15 * WINDOW_LENGTH), anchor='center')

        self.tree_view1.heading('order_no', text='������')
        self.tree_view1.heading('company_name', text='��˾����')
        self.tree_view1.heading('created_date', text='��������')
        self.tree_view1.heading('all_total_price', text='�����ܼ�')

        # ������һ��������
        scrollbar1 = tk.Scrollbar(self.frame1, orient="vertical", command=self.tree_view1.yview)
        self.tree_view1.configure(yscrollcommand=scrollbar1.set)

        # ���֣���һ��treeview���frame�������������Ҳ�
        self.tree_view1.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar1.pack(side="right", fill="y")

        ###########################################################################
        # �����ڶ�������������ڶ���treeview�͹�����
        self.frame2 = tk.Frame(self)
        self.frame2.pack(fill=tk.BOTH, expand=True,  pady=20)
        # �ڶ�������������

        columns2 = ("product_name", "product_standard", "product_unit", "quantity","unit_price", "total_price", "product_description")
        self.tree_view2 = ttk.Treeview(self.frame2, columns=columns2, show="headings")
        self.tree_view2.column('product_name', width=int(0.3 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('product_standard', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('product_unit', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('quantity', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('unit_price', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('total_price', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree_view2.column('product_description', width=int(0.1 * WINDOW_LENGTH), anchor='center')


        self.tree_view2.heading('product_name', text='��Ʒ����')
        self.tree_view2.heading('product_standard', text='��Ʒ��׼')
        self.tree_view2.heading('product_unit', text='��λ')
        self.tree_view2.heading('quantity', text='����')
        self.tree_view2.heading('unit_price', text='����')
        self.tree_view2.heading('total_price', text='�ܼ�')
        self.tree_view2.heading('product_description', text='��ע')

        #���2����
        self.tree_view2.pack(side="left", fill=tk.BOTH, expand=True)

        self.show_orders()
        # ������¼�
        self.tree_view1.bind("<ButtonRelease-1>", self.on_item_click)




    def show_orders(self, orders=None):
        """
        չʾ����orders������У������ر����չʾ�Ķ������б�
        :param orders: �����orders�б������������ȫ��չʾ
        :return: orders_list: ���ر����չʾ�Ķ������б�
        """
        if orders is None:
            orders = self.orders
        index = 0
        for order in orders:
            print(order) # DEBUG
            self.tree_view1.insert('', index + 1, values=(
                order['order_no'], order['company_name'], order['created_date'], order['all_total_price']))

    def show_products(self, order_no = None):
        """
        չʾ�ڶ����б�treeview2���ݣ�order_no�Ƕ�����
        :param order_no:
        :return:
        """
        if order_no is None:
            pass

        # ��������е��Ѿ���ʾ����Ŀ
        for item in self.tree_view2.get_children():
            self.tree_view2.delete(item)
        op = Operation()
        clicked_order = op.find_order_by_order_no(order_no) #��ǰ���������Ŀ
        products = clicked_order['Products'] # ��ǰ�ͻ����Ĳ�Ʒ
        index = 0
        for product in products:
            print(product) # DEBUG
            self.tree_view2.insert('', index + 1,
                                   values=(
                                            product['product_name'], product['product_standard'],
                                            product['product_unit'], product['quantity'],
                                            product['unit_price'], product['total_price'],
                                            product['product_description']
                                    ))

    def on_item_click(self, event = None):
        """
        ������������¼����漰��������ʾ�������
        :param event:
        :return:
        """
        # ��ȡ����������ID
        selected_item = self.tree_view1.selection()
        if selected_item is None:
            pass
        # ��ȡ�������ϸ����
        item_id = selected_item[0]
        item_values = self.tree_view1.item(item_id, 'values')
        order_no = item_values[0]  # 'Order No' �ǵ�һ��
        print(order_no)
        self.show_products(order_no)







