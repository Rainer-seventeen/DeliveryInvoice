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

        #��ʼ��self�ܿ��
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=12)
        self.columnconfigure(0, weight=1)  # ���������Ȩ��Ϊ1

        # ��ʼ�������б�
        self.INIT_STR = '�����Ʒ����û���򲻸ģ�'
        rows = 6
        cols = 6
        self.data = [['' for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            self.data[r][0] = self.INIT_STR

        ###########################################################################
        # �����������
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row=0, column=0, sticky='nsew')
        for i in range(0,5):
            self.input_frame.columnconfigure(i, weight=1)  # Ȩ��

        self.entry_company = tk.Entry(self.input_frame, width=60)
        self.entry_company.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")  # ������չ
        name_label_company = tk.Label(self.input_frame, text="��˾����:")
        name_label_company.grid(row=1, column=0, pady=5, sticky="we")  # �������

        self.entry_address = tk.Entry(self.input_frame, width=60)
        self.entry_address.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")
        name_label_address = tk.Label(self.input_frame,text='��ַ����:')
        name_label_address.grid(row=2, column=0, pady=5, sticky="we")

        self.entry_phone = tk.Entry(self.input_frame, width=60)
        self.entry_phone.grid(row=3, column=1, columnspan=2, pady=5, sticky="w")  # ������չ
        name_label_phone = tk.Label(self.input_frame, text="�ͻ��绰:")
        name_label_phone.grid(row=3, column=0, pady=5, sticky="we")  # �������

        self.entry_connector = tk.Entry(self.input_frame, width=60)
        self.entry_connector.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")  # ������չ
        name_label_connector = tk.Label(self.input_frame, text="��ϵ��:")
        name_label_connector.grid(row=4, column=0, pady=5, sticky="we")  # �������


        ###########################################################################
        # �����������
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=1, column=0, sticky="ew")  # ȡ����ֱ��չ

        # ���ñ�����������Ȩ��
        self.table_frame.rowconfigure(0, weight=1)  # �����Ȩ��Ϊ1
        self.table_frame.columnconfigure(0, weight=1)  # �����Ȩ��Ϊ1

        # ����Treeview
        columns = ("product_name", "product_standard", "product_unit", "quantity","unit_price","product_description")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        self.tree.grid(row=0, column=0, sticky="ew")

        # # ������
        # vsb = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        # vsb.grid(row=0, column=1, sticky="ns")  # �����������Ҳ�
        # self.tree.configure(yscrollcommand=vsb.set)


        # ������
        self.tree.column('product_name', width=int(0.3 * WINDOW_LENGTH), anchor='center')
        self.tree.column('product_standard', width=int(0.2 * WINDOW_LENGTH), anchor='center')
        self.tree.column('product_unit', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.column('quantity', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.column('unit_price', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.column('product_description', width=int(0.1 * WINDOW_LENGTH), anchor='center')
        self.tree.heading('product_name', text='��Ʒ����')
        self.tree.heading('product_standard', text='��Ʒ��׼')
        self.tree.heading('product_unit', text='��λ')
        self.tree.heading('quantity', text='����')
        self.tree.heading('unit_price', text='����')
        self.tree.heading('product_description', text='��ע')

        # ������߶�
        # self.adjust_table_height(6)  # ������ʾ6��

        # ��ʼ����
        for row in range(rows):
            self.tree.insert("", "end", values=self.data[row])

        # �¼���
        self.tree.bind("<Button-1>", self.on_table_click)

        # �༭�ؼ�
        self.entry_frame = ttk.Frame(self)  # �����������
        self.entry = ttk.Entry(self.entry_frame)
        # self.btn = ttk.Button(self.entry_frame, text="��", width=2,
        #                       command=self.show_history_list)
        self.listbox = tk.Listbox(self)  # �����б�
        self.current_edit = None

        ###########################################################################
        # ��ť���
        button_frame = ttk.Frame(self)
        button_frame.grid(row=3, column=0, sticky='ew')
        for i in range(0,10):
            button_frame.columnconfigure(i, weight=1)  # Ȩ��

        save_button = tk.Button(button_frame,text='����',command=lambda :self.on_save_click())
        save_button.grid(row=0, column=2, pady=5, sticky="w")

    def on_table_click(self, event):
        # �����ǰ�����ڱ༭�ĵ�Ԫ���ȱ�������
        if self.current_edit:
            self.save_edit(*self.current_edit)  # ���浱ǰ�༭����

        # ��ȡλ����Ϣ
        row_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)

        if not row_id or column == "#0":
            return

        # ��ȡ����
        col_index = int(column[1:]) - 1
        row_index = int(self.tree.index(row_id))
        x, y, width, height = self.tree.bbox(row_id, column)

        # ת��Ϊ����������
        table_x = self.table_frame.winfo_x()
        table_y = self.table_frame.winfo_y()
        abs_x = table_x + x
        abs_y = table_y + y

        # ���������λ��
        self.entry_frame.place(x=abs_x, y=abs_y, width=width, height=height)
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.btn.pack(side=tk.RIGHT, fill=tk.Y)

        # ��ʼֵ
        value = self.data[row_index][col_index]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
        self.entry.focus_set()

        # ���¼�
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
        ���水ť�Ļص�����������д�빦��
        :return:
        """
        company = self.entry_company.get()
        address = self.entry_phone.get()
        phone = self.entry_phone.get()
        connector = self.entry_connector.get()
        matrix = self.matrix_from_data()
        if not self.check_entry_empty(company, address, phone, connector, matrix):
            return
        if not messagebox.askyesno('ȷ��', 'ȷ�ϱ��浱ǰ�ͻ�����'):
            return
        wt = Write()
        wt.add_new_invoice(company, address, phone, connector, matrix)
    @staticmethod
    def check_entry_empty(company,address,phone,connector,matrix):
        """
        ��������Ƿ�Ϸ�
        :return: True / False
        """
        if company.strip() == "":
            messagebox.showwarning('����', '��˾����δ��д')
            return False
        if address.strip() == "":
            messagebox.showwarning('����', '��˾��ַδ��д')
            return False
        if phone.strip() == "":
            messagebox.showwarning('����', '�ͻ��绰δ��д')
            return False
        if connector.strip() == "":
            messagebox.showwarning('����', '��ϵ��δ��д')
            return False
        for row in range(0,len(matrix)-1):
            is_empty = True
            if matrix[row][0].strip() != "":
                is_empty = False
                if not matrix[row][3].strip().isdigit():
                    messagebox.showwarning('����', f"��{row + 1}�в�Ʒ��������ȷ")
                if not matrix[row][4].strip().replace('.', '', 1).isdigit():
                    messagebox.showwarning('����', f"��{row + 1}�в�Ʒ���۲���ȷ")
                print('Check Entry: PASS') # DEBUG
                return True

        messagebox.showwarning('����', "�������һ���Ʒ")
        return False

    def matrix_from_data(self):
        """
        ����һ�� matrix �� on_create_click ʹ�ã�
        :return: matrix
        """
        matrix = copy.deepcopy(self.data)
        for row in matrix:
            if row[0] == self.INIT_STR:
                row[0] = ''
        return matrix


