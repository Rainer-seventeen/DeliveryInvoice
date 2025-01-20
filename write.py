# -*- coding: gbk -*-
"""������еĹ���д���ļ��ĺ���"""
from info import CURRENT_FOLDER
from info import FILE_ENCODING
import json
import os


new_delivery_order = {
    "id": 3,
    "order_no": "DO123458",
    "created_date": "2025-01-21",
    "created_time": "10:00:00",
    "company_name": "Tech Innovations",
    "company_address": "789 Innovation Blvd, Silicon Valley",
    "company_phone": "555-1234-5678",
    "company_connector": "Alice Johnson",
    "all_total_price": 2500.50,
    "Products": [
        {
            "id": 1,
            "product_name": "Smart Watch Model A",
            "product_standard": "32GB Storage, 1GB RAM",
            "product_unit": "Piece",
            "quantity": 15,
            "unit_price": 50.00,
            "product_description": "Latest model with heart-rate monitor",
            "total_price": 750.00
        },
        {
            "id": 2,
            "product_name": "Bluetooth Headphones",
            "product_standard": "Noise Cancelling, Wireless",
            "product_unit": "Piece",
            "quantity": 30,
            "unit_price": 25.00,
            "product_description": "Wireless headphones with active noise cancellation",
            "total_price": 750.00
        }
    ]
}

class Write:
    def __init__(self):
        self.invoice_path = rf"{CURRENT_FOLDER}{r"\invoice.json"}"

    def add_new_delivery_order(self, new_order):
        # ����ļ������ڣ������ļ�����ʼ��Ϊһ���յ� delivery orders ����
        if not os.path.exists(self.invoice_path):
            with open(self.invoice_path, 'w', encoding= FILE_ENCODING) as f:
                json.dump({"DeliveryOrders": []}, f, ensure_ascii=False, indent=4)

        # ��ȡ���е� JSON ����
        with open(self.invoice_path, 'r', encoding= FILE_ENCODING) as f:
            data = json.load(f)

        # ����µ��ͻ�������
        data['DeliveryOrders'].append(new_order)

        # д�� JSON �ļ�
        with open(self.invoice_path, 'w', encoding= FILE_ENCODING) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("�µ��ͻ�������ӳɹ���")
# ���ú������� JSON �ļ�������µ��ͻ���

wt = Write()
wt.add_new_delivery_order(new_delivery_order)