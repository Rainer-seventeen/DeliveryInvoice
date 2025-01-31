# -*- coding: gbk -*-

# ��ʾ���еĶ�����Ϣ
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
        # ����һ���������
        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=10)  # �������º����ҵļ��
        for i in range(0,10):
            input_frame.columnconfigure(i, weight=1)  # Ȩ��


        # �������ʾ
        company_label = tk.Label(input_frame, text="���빫˾���Բ�ѯ:")
        company_label.grid(row=0, column=0, pady=5, sticky="w")  # �������

        # ���һ�������������Ȩ��
        input_entry = ttk.Entry(input_frame, width=60)
        input_entry.grid(row=0, column=1, columnspan=3, pady=5, sticky="w")  # ������չ

        #����������ť�����������Ҳ�
        button_company = ttk.Button(
            input_frame,
            text="����",
            command=lambda: self.on_search_click(entry_str=input_entry.get())
            )
        button_company.grid(row=0, column=3, pady=5, sticky="e")

        ###########################################################################
        # ��һ�������������һ��treeview�͹�����
        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill=tk.BOTH, expand=True, padx = 10, pady=10)  # �������¼��Ϊ10
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
        self.frame2.pack(fill=tk.BOTH, expand=True, pady=5, padx = 10)
        # �ڶ�������������

        self.created_date_and_time = ''
        self.company_address = ''
        self.company_connector_and_phone = ''


        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.frame2.rowconfigure(3, weight=1)
        self.frame2.rowconfigure(4, weight=1)
        self.frame2.columnconfigure(0, weight=1)

        self.choose_label = tk.Label(self.frame2,text='ѡ�񶩵�����ʾ����')
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
        self.tree_view2.heading('product_name', text='��Ʒ����')
        self.tree_view2.heading('product_standard', text='��Ʒ��׼')
        self.tree_view2.heading('product_unit', text='��λ')
        self.tree_view2.heading('quantity', text='����')
        self.tree_view2.heading('unit_price', text='����')
        self.tree_view2.heading('total_price', text='�ܼ�')
        self.tree_view2.heading('product_description', text='��ע')

        #���2����
        self.tree_view2.grid(row=4, column=0, pady=10, sticky="we", padx=(5,15))

        self.show_orders()
        # ������¼�
        self.tree_view1.bind("<ButtonRelease-1>", self.on_item_click)

        ###########################################################################
        # ������������ڴ���ϵ�в�����ť
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, expand=True, pady=0)  # �������¼��Ϊ10

        for i in range(0,10):
            button_frame.columnconfigure(i, weight=1)  # Ȩ��

        button_company = ttk.Button(
            button_frame,
            text="����������",
            command=self.on_create_click
            )
        button_company.grid(row=0, column=8, pady=5, sticky="ew")


    def show_orders(self, orders=None):
        """
        չʾ����orders������У������ر����չʾ�Ķ������б�
        :param orders: �����orders�б������������ȫ��չʾ
        :return: orders_list: ���ر����չʾ�Ķ������б�
        """
        if orders is None:
            orders = self.orders
        for order in orders:
            # print(order) # DEBUG
            self.tree_view1.insert('', index = 'end', values=(
                order['order_no'], order['company_name'], order['created_date'], order['all_total_price']))

    def show_products(self, order_no = None):
        """
        չʾ�ڶ����б�treeview2���ݣ��Լ�treeview2�Ϸ����ݣ�order_no�Ƕ�����
        :param order_no:
        :return:
        """
        if order_no is None:
            pass

        # ��ձ�������е��Ѿ���ʾ����Ŀ
        for item in self.tree_view2.get_children():
            self.tree_view2.delete(item)
        op = Operation()
        clicked_order = op.find_order_by_order_no(order_no) #��ǰ���������Ŀ

        # ����м�����ʾ
        self.choose_label.grid_forget()
        self.created_date_and_time_label.grid_forget()
        self.company_name_label.grid_forget()
        self.company_address_label.grid_forget()
        self.company_connector_and_phone_label.grid_forget()
        # ������ʾ����
        created_date_and_time = clicked_order['created_date']+' '+clicked_order['created_time']
        company_name = clicked_order['company_name']
        company_address = clicked_order['company_address']
        company_connector_and_phone = clicked_order['company_connector']+' '+clicked_order['company_phone']

        # ��ǰ��Ŀ��ʾ
        self.created_date_and_time_label = tk.Label(self.frame2,text="�������ڼ�ʱ�䣺"+created_date_and_time)
        self.company_name_label = tk.Label(self.frame2,text='��˾���ƣ�'+company_name)
        self.company_address_label = tk.Label(self.frame2,text='��˾��ַ�� '+company_address)
        self.company_connector_and_phone_label = tk.Label(self.frame2,text='��ϵ�˼��绰��'+company_connector_and_phone)
        self.created_date_and_time_label.grid(row=0, column=0, pady=0, sticky="w")
        self.company_name_label.grid(row=1, column=0, pady=0, sticky="w")
        self.company_address_label.grid(row=2, column=0, pady=0, sticky="w")
        self.company_connector_and_phone_label.grid(row=3, column=0, pady=0, sticky="w")

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
        �������һ����񴥷����¼���������ʾ�������
        ���û��ѡ�У���ֵ self.item_is_selected = False
        :param event:
        :return:���û��ѡ�У����� None
        """
        # ��ȡ����������ID

        selected_item = self.tree_view1.selection()

        if selected_item is None: # δѡ��
            for item in self.tree_view2.get_children():
                self.tree_view2.delete(item)
            self.tree_view2.insert("", "end", values=("ѡ�ж�������ʾ����",))
            return None

        # ��ȡ�������ϸ����
        try:
            item_id = selected_item[0] # treeview�ڲ�id����ʽ��I001
        except IndexError:
            return None
        # print(item_id) # DEBUG
        item_values = self.tree_view1.item(item_id, 'values')

        selected_item_id = item_values[0]  # 'Order No' �ǵ�һ��
        # print(order_no) # DEBUG

        if selected_item_id == 'δ�ҵ����': # ѡ���ˡ�δ�ҵ���
            for item in self.tree_view2.get_children():
                self.tree_view2.delete(item)
            self.tree_view2.insert("", "end", values=("ѡ�ж�������ʾ����",))
            return None
        self.show_products(selected_item_id)

    def on_search_click(self, entry_str):
        """
        ����������ť�Ļص�������������ʾtreeview1
        :param entry_str: ������ַ���
        :return:
        """

        self.tree_view1.delete(*self.tree_view1.get_children())
        op = Operation()
        orders_no = op.find_order_no_by_company_name(entry_str)    #�ҵ�������
        # print(orders_no) # DEBUG
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

    def on_create_click(self):
        """
        �����ͻ�����ť�ص����������ݵ�ǰѡ�еĶ��������������ɵȹ���
        :param
        :return:
        """
        selected_item = self.treeview1_click()
        if selected_item is None:
            return
        if not messagebox.askyesno('ȷ��','ȷ�������ͻ����ļ���'):
            return
        op = Operation()
        wt = Write()
        out = op.find_order_by_order_no(selected_item)
        wt.write_docx(out)

    def treeview1_click(self):
        """
        ��һϵ�а�ť���ã����ڷ��ص�ǰtreeview1ѡ�е��Ǹ�������
        :return:ѡ�еĶ����ţ����û������ None
        """
        op = Operation()
        selected_item = self.tree_view1.selection()
        # selected_order_no = 0
        if len(selected_item) == 0 :
            # û��ѡ���κ�һ����Ŀ
            messagebox.showwarning('����', 'δѡ�ж�������ѡ�ж��������ԣ�')
            return None
        else:
            selected_order_id = selected_item[0] # �ڲ�id
            selected_order_no = self.tree_view1.item(selected_order_id, 'values')[0]
        if op.find_order_by_order_no(selected_order_no) is None:
            # û��ѡ����ȷ�Ķ�������
            messagebox.showwarning('����','δѡ�ж�������ѡ�ж��������ԣ�')
            return None
        else:
            print(selected_order_no)
            return selected_order_no


if __name__ == '__main__':
    root = tk.Tk()
    SF = SearchFrame(root)
    SF.on_search_click(entry_str='A')






