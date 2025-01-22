# -*- coding: gbk -*-

# ��ʾ���еĶ�����Ϣ
import tkinter as tk
from tkinter import ttk
from operation import Operation


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

        # ������һ�������������һ��treeview�͹�����
        frame1 = tk.Frame(self)
        frame1.pack(fill=tk.BOTH, expand=True, pady=10)  # �������¼��Ϊ10

        # ��һ������������
        columns = ("order_no", "company_name", "created_date", "all_total_price")
        self.tree_view1 = ttk.Treeview(frame1, columns=columns, show="headings")
        self.tree_view1.column('order_no', width=150, anchor='center')
        self.tree_view1.column('company_name', width=400, anchor='center')
        self.tree_view1.column('created_date', width=250, anchor='center')
        self.tree_view1.column('all_total_price', width=150, anchor='center')

        self.tree_view1.heading('order_no', text='������')
        self.tree_view1.heading('company_name', text='��˾����')
        self.tree_view1.heading('created_date', text='��������')
        self.tree_view1.heading('all_total_price', text='�����ܼ�')

        # ������һ��������
        scrollbar1 = tk.Scrollbar(frame1, orient="vertical", command=self.tree_view1.yview)
        self.tree_view1.configure(yscrollcommand=scrollbar1.set)

        # ���֣���һ��treeview���frame�������������Ҳ�
        self.tree_view1.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar1.pack(side="right", fill="y")

        # �����ڶ�������������ڶ���treeview�͹�����
        frame2 = tk.Frame(self)
        frame2.pack(fill=tk.BOTH, expand=True,  pady=20)
        # �ڶ�������������
        self.tree_view2 = ttk.Treeview(frame2, columns=columns, show="headings")
        self.tree_view2.column('order_no', width=150, anchor='center')
        self.tree_view2.column('company_name', width=400, anchor='center')
        self.tree_view2.column('created_date', width=250, anchor='center')
        self.tree_view2.column('all_total_price', width=150, anchor='center')

        self.tree_view2.heading('order_no', text='������')
        self.tree_view2.heading('company_name', text='��˾����')
        self.tree_view2.heading('created_date', text='��������')
        self.tree_view2.heading('all_total_price', text='�����ܼ�')

        #���2����
        self.tree_view2.pack(side="left", fill=tk.BOTH, expand=True)
        self.show_data()



    def show_data(self,orders = None):
        """
        չʾ����orders�������
        :param orders: �����orders�б������������ȫ��չʾ
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
        # �����ţ���˾�����������ڣ��ܼ�



