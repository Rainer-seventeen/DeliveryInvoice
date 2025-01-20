# -*- coding: gbk -*-
import tkinter as tk
from venv import create

from info import CURRENT_FOLDER

class CreateFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # �������һ��frame���󣬲���Ҫ����
        # tk.Label(self, text="�����ͻ���").pack()
        # self.pack()


    def create_ui(self):
        # ------ Company ������� ------
        dropdown_var_company = tk.StringVar()
        entry_company = tk.Entry(self.master, width=60)

        # # �����˵�
        # dropdown_menu_company = tk.OptionMenu(self.master, dropdown_var_company, "������ʷ��¼")
        # dropdown_menu_company.grid(row=0, column=3, columnspan=2, pady=5, sticky="w")  # �������

        # # �󶨹�˾�����߼�
        # bind_dropdown_action(dropdown_var_company, entry_company)

        # ��ǩ
        name_label_company = tk.Label(self.master, text="��˾����:")
        name_label_company.grid(row=0, column=0, pady=5, sticky="we")  # �������

        # �����
        entry_company.grid(row=0, column=1, columnspan=2, pady=5, sticky="w")  # ������չ

        # �ύ��ť������������Ҳ�
        button_company = tk.Button(self.master, text="�ύ��˾")
        button_company.grid(row=0, column=5, padx=10, pady=5, sticky="we")  # ��������ұ�


        #############################################################################
        # ------ Address ������� ------
        dropdown_var_address = tk.StringVar()
        entry_address = tk.Entry(self.master, width=60)

        # # �����˵�
        # dropdown_menu_address = tk.OptionMenu(self.master, dropdown_var_address, "������ʷ��¼")
        # dropdown_menu_address.grid(row=2, column=3, columnspan=2, pady=5, sticky="w")  # �������
        #
        # # �󶨵�ַ�����߼�
        # bind_dropdown_action(dropdown_var_address, entry_address)

        # ��ǩ
        name_label_address = tk.Label(self.master, text="��ַ����:")
        name_label_address.grid(row=2, column=0, pady=5, sticky="we")  # �������

        # �����
        entry_address.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")  # ������չ

        # �ύ��ť���������ͬ��ͬ���Ҳ�
        button_address = tk.Button(self.master,text="�ύ��ַ",)
        button_address.grid(row=2, column=5, padx=10, pady=5, sticky="we")  # ��������ұ�

        # # ȷ�ϰ�ť�����ַ�ύ��ťͬ���Ҳ�
        # confirm_address = tk.Button(
        #     root,
        #     text="ȷ�ϵ�ַ",
        #     command=lambda: print_to_console(entry_address.get())
        # )
        # confirm_address.grid(row=3, column=5, padx=10, pady=5, sticky="we")  # ���ύ��ť�ұ�
        #############################################################################
        # �绰����ϵ�������
        name_label_phone = tk.Label(self.master, text="�ͻ��绰:")
        name_label_phone.grid(row=3, column=0, pady=5, sticky="we")  # �������
        entry_phone = tk.Entry(self.master, width=60)
        entry_phone.grid(row=3, column=1, columnspan=2, pady=5, sticky="w")  # ������չ

        name_label_connector = tk.Label(self.master, text="��ϵ��:")
        name_label_connector.grid(row=4, column=0, pady=5, sticky="we")  # �������
        entry_connector = tk.Entry(self.master, width=60)
        entry_connector.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")  # ������չ

        #############################################################################
        # ------ ����6x8����򲼾� ------
        input_vars = []
        labels = ("��Ʒ����", "����ͺ�", "��λ", "����", "����", "��ע")
        for i in range(6):
            name_label_company = tk.Label(self.master, text=labels[i])
            name_label_company.grid(row=5, column=i, pady=5, sticky="we")  # �������

        file_path = rf"{CURRENT_FOLDER}{r"\output.txt"}"  # txt�ļ���·��
        # ��� 6x8 �����
        for i in range(8):  # 8��
            row_vars = []
            for j in range(6):  # ÿ��6��
                var = tk.StringVar()
                entry = tk.Entry(self.master, textvariable=var, width=30)
                entry.grid(row=6 + i, column=j, padx=5, pady=5, sticky="w")
                row_vars.append(var)
            input_vars.append(row_vars)

        confirm_export = tk.Button(self.master,text="������������")
        confirm_export.grid(row=14, column=4, columnspan=1, pady=10, sticky="we")

        file_path_docx = rf"{CURRENT_FOLDER}{r"\framework.docx"}"  # word ģ���ļ�·��
        output_path = rf"{CURRENT_FOLDER}{r"\���ɺ��ͻ���.docx"}"
        button_generate_docx = tk.Button(
            self.master,
            text="�����ͻ���",
            command=lambda: tk.messagebox.askyesno(
                "ȷ�ϵ���",
                "ȷ���Ѿ��������ݣ������ͻ�����"
            )
        )
        button_generate_docx.grid(row=16, column=4, columnspan=1, pady=10, sticky="we")  # ��������ұ�

        button_import_database = tk.Button(
            self.master,
            text="�������ݿ�",

            command=lambda: tk.messagebox.askyesno(
                "ȷ�ϵ���",
                "��ȷ���Ƿ�д�����ݿ⣿"
            )
        )
        button_import_database.grid(row=17, column=4, columnspan=1, pady=10, sticky="we")  # ������