# -*- coding: gbk -*-

# ��ʾ���еĶ�����Ϣ
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

        # TODO ����һ����������input_frame����treeview1��ʾ����ֵ�Ŀ���

        # ����һ���������
        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=10)  # �������º����ҵļ��
        for i in range(0,10):
            input_frame.columnconfigure(i, weight=1)  # ��һ��Ȩ��


        # �������ʾ
        company_label = tk.Label(input_frame, text="���빫˾���Բ�ѯ:")
        company_label.grid(row=0, column=0, pady=5, sticky="w")  # �������

        # ���һ�������������Ȩ��
        input_entry = tk.Entry(input_frame, width=60)
        input_entry.grid(row=0, column=1, columnspan=3, pady=5, sticky="w")  # ������չ

        #����������ť�����������Ҳ�
        button_company = tk.Button(
            input_frame,
            text="����",
            command=lambda: self.on_search_click(entry_str=input_entry.get())
            )
        button_company.grid(row=0, column=4, pady=5, sticky="w")





        ###########################################################################
        # ��һ�������������һ��treeview�͹�����
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
        for order in orders:
            print(order) # DEBUG
            self.tree_view1.insert('', index = 'end', values=(
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

    def on_search_click(self, entry_str, event = None):
        """
        ����������ť�Ļص�������������ʾtreeview1
        :param entry_str: ������ַ���
        :param event: ��
        :return:
        """

        self.tree_view1.delete(*self.tree_view1.get_children())
        op = Operation()
        orders_no = op.find_order_no_by_company_name(entry_str)    #�ҵ�������
        # print(orders_no)
        orders_to_show = []
        if len(entry_str) == 0:
            # ���û�����ȫ����ʾ
            orders_to_show = self.orders
        elif len(orders_no) == 0:
            # ���û���ҵ����δ�ҵ�
            self.tree_view1.insert("", "end", values=("δ�ҵ����",))
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






