# -*- coding: gbk -*-
"""������еĹ���json�ļ���ȡ��д��ĺ���"""
import json
import os

from info import CURRENT_FOLDER
from info import FILE_ENCODING
from operation import Operation



class Write:
    def __init__(self):
        self.invoice_path = rf"{CURRENT_FOLDER}{r"\invoice.json"}"

        #��ʼ��invoice.json�ļ�
        if not os.path.exists(self.invoice_path):
            with open(self.invoice_path, 'w', encoding= FILE_ENCODING) as f:
                json.dump({"DeliveryOrders": []}, f, ensure_ascii=False, indent=4)

    def add_new_invoice(self,company_name, company_address, company_phone, company_connector, entry_matrix):
        """
        д��json����ڣ������װ����
        :param company_name: ��˾����
        :param company_address: ��˾��ַ
        :param company_phone: ��˾�绰
        :param company_connector:��˾��ϵ��
        :param entry_matrix:�������ͨ��uiֱ�Ӵ��룩
        """
        op = Operation()
        order_list = op.create_new_order(company_name, company_address, company_phone, company_connector, entry_matrix)
        self.write_invoice_json(order_list)

    def write_invoice_json(self, new_order):
        """
        �����ɵ��ֵ�д��json�ļ�
        :param new_order: �ֵ����͵����ݣ���create_new_order()����
        """
        # ����ļ������ڣ������ļ�����ʼ��Ϊһ���յ� delivery orders ����


        # ��ȡ���е� JSON ����
        with open(self.invoice_path, 'r', encoding= FILE_ENCODING) as f:
            data = json.load(f)

        # ����µ��ͻ�������
        data['DeliveryOrders'].append(new_order)

        # д�� JSON �ļ�
        with open(self.invoice_path, 'w', encoding= FILE_ENCODING) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("�µ��ͻ�������ӳɹ���")




company_name = "�Ϻ���A��˾"
address_name = "�ֶ����"
company_phone = "123"
company_connector = "��ϵ��"
output_data = [
    ['��ƷA', '��', '��', '10', '5', '��'],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
]

wt = Write()
wt.add_new_invoice(company_name, address_name, company_phone, company_connector, output_data)