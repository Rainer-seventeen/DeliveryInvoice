# -*- coding: gbk -*-
"""���ڴ������е����ݲ�������"""

import os
import json

from info import CURRENT_FOLDER
from info import FILE_ENCODING


class Operation:
    def __init__(self):

        self.invoice_path = rf"{CURRENT_FOLDER}{r"\invoice.json"}"

        # ��ʼ��invoice.json�ļ�
        if not os.path.exists(self.invoice_path):
            with open(self.invoice_path, 'w', encoding=FILE_ENCODING) as f:
                json.dump({"DeliveryOrders": []}, f, ensure_ascii=False, indent=4)



    def create_new_order(self, company_name, company_address, company_phone, company_connector, entry_matrix):
        """
        ����һ���µĶ����ֵ䣬��д�� JSON �ļ��ĺ���ʹ�á�

        ����:
            company_name (str): ��˾����
            company_address (str): ��˾��ַ
            company_phone (str): ��˾�绰
            company_connector (str): ��˾��ϵ��
            products (list): ��Ʒ�б�ÿ����ƷΪһ���ֵ䣬������Ʒ��ϸ��Ϣ

        ����:
            dict: ��ʽ����Ķ����ֵ�
        """
        # 1. ��ȡ������
        order_no = self.get_next_order_no()

        # 2. �������ں�ʱ��
        created_date, created_time = self.generate_current_time()

        # 3. ����products�б�
        products = self.create_products_list(input_matrix = entry_matrix)

        # 3. �����ܽ��
        all_total_price = sum(product['quantity'] * product['unit_price'] for product in products)

        # 4. ��ʽ�������ֵ�
        new_order = {
            "order_no": order_no,
            "created_date": created_date,
            "created_time": created_time,
            "company_name": company_name,
            "company_address": company_address,
            "company_phone": company_phone,
            "company_connector": company_connector,
            "all_total_price": round(all_total_price, 2),
            "Products": []
        }

        # 5. ��ʽ����Ʒ�б�
        for idx, product in enumerate(products, start=1):
            product_entry = {
                "id": idx,
                "product_name": product.get("product_name", ""),
                "product_standard": product.get("product_standard", ""),
                "product_unit": product.get("product_unit", ""),
                "quantity": product.get("quantity", 0),
                "unit_price": product.get("unit_price", 0.0),
                "product_description": product.get("product_description", ""),
                "total_price": round(product.get("quantity", 0) * product.get("unit_price", 0.0), 2)
            }
            new_order["Products"].append(product_entry)

        return new_order

    @staticmethod
    def create_products_list(input_matrix):
        """
        ��������ľ�����ʽ���� products �б�

        ����:
            entry_matrix (list): ������Ʒ��Ϣ�ľ���ÿ�д���һ����Ʒ��ÿ�д��������ֶΣ�
                [product_name, product_standard, product_unit, quantity, unit_price, product_description]

        ����:
            list: ���ϸ�ʽ�� products �б�
        """
        products_list = []
        for idx, entry in enumerate(input_matrix, start=1):
            # �����յ� product_name ��
            if not entry[0].strip():
                continue

            # ��ȡ�������ݣ������ֵ������ת��
            product_name = entry[0].strip()
            product_standard = entry[1].strip()
            product_unit = entry[2].strip()
            quantity = int(entry[3].strip()) if entry[3].strip().isdigit() else 0
            unit_price = float(entry[4].strip()) if entry[4].strip().replace('.', '', 1).isdigit() else 0.0
            product_description = entry[5].strip()

            # �����ܼ�
            total_price = round(quantity * unit_price, 2)

            # ������Ʒ��Ŀ
            product_entry = {
                "id": idx,
                "product_name": product_name,
                "product_standard": product_standard,
                "product_unit": product_unit,
                "quantity": quantity,
                "unit_price": unit_price,
                "product_description": product_description,
                "total_price": total_price
            }
            products_list.append(product_entry)

        return products_list

    @staticmethod
    def generate_current_year_month():
        """
        ������ݺ��·ݣ���ʽΪ YYYYMM�����ں������ '0001'����ǰ

        ����:
            str: ��ʽ�����ַ��������� '2024010001'
        """
        from datetime import datetime
        now = datetime.now()
        year_month = now.strftime("%Y%m")
        result = f"{year_month}0001"

        return result

    @staticmethod
    def generate_current_time():
        """
        ���ص�ǰ���ں�ʱ��ֱ���ַ�����ʾ

        ����:
            tuple: (��ǰ����, ��ǰʱ��)�����ڸ�ʽ "YYYY-MM-DD"��ʱ���ʽ "HH:MM:SS"
        """
        from datetime import datetime
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        return current_date, current_time

    def get_next_order_no(self):
        """
        ��ȡ DeliveryOrder �б��� order_no �ֶε����ֵ�������������������һ��ֵ��

        ����:
            str: ��һ�����õ� order_no��10λ�ַ�����
        """
        current_min_id = Operation.generate_current_year_month()
        try:
            # ��ȡ���е� JSON ����
            with open(self.invoice_path, 'r', encoding=FILE_ENCODING) as f:
                data = json.load(f)

            # ������󶩵���
            max_order_no = None
            for order in data['DeliveryOrders']:
                order_no = order['order_no']
                if max_order_no is None or int(order_no) > int(max_order_no):
                    max_order_no = order_no

            # �����󶩵���Ϊ�գ�˵������ǿյģ����ص�ǰ���ɵ���Сֵ
            if max_order_no is None:
                return current_min_id  # �ձ�ʱ���ص�ǰ����

            # �����ǰ���ֵ�Ѿ��ȵ�ǰ����������ֵС��˵�����µ�һ����/��ĵ�һ�����ӣ�ʹ�����ɵ���ֵ
            if int(max_order_no) < int(current_min_id):
                return current_min_id

            # �� order_no ת��Ϊ�������� 1
            next_order_no = int(max_order_no) + 1
            # ��ʽ��Ϊ 10 λ�ַ���
            return f"{next_order_no:010}"

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def find_order_by_order_no(self, order_no):
        """
        ���ݶ����Ų��� JSON �ļ��еĶ�����Ŀ��
        �������-1��ʾ�������еĶ���
        :param order_no:Ҫ���ҵĶ����š�-1(int)�������ж���
        :return: ��Ӧ�Ķ����ֵ䣬���δ�ҵ������� None��

        """
        if not os.path.exists(self.invoice_path):
            print("�ļ������ڣ�")
            return None

        try:
            # ��ȡ JSON �ļ�����
            with open(self.invoice_path, 'r', encoding=FILE_ENCODING) as f:
                data = json.load(f)

            # ���������-1�򷵻����еĶ���
            orders = data.get("DeliveryOrders", [])
            if order_no == -1:
                return orders

            # ��������ƥ��Ķ�����
            for order in orders:

                if str(order["order_no"]) == str(order_no):
                    return order

            print("δ�ҵ�ƥ��Ķ����ţ�")
            return None
        except json.JSONDecodeError:
            print("JSON �ļ�����ʧ�ܣ�")
            return None
        except Exception as e:
            print(f"��������: {e}")
            return None

    def find_order_no_by_company_name(self, company_name):
        """
        ���ݹ�˾���ֲ��� JSON �ļ��е����ж����š�

        ����:
            company_name (str): Ҫ���ҵĹ�˾���֡�

        ����:
            list: ��������ƥ�䶩���ŵ��б����δ�ҵ������ؿ��б�
        """
        if not os.path.exists(self.invoice_path):
            print("�ļ������ڣ�")
            return []

        try:
            # ��ȡ JSON �ļ�����
            with open(self.invoice_path, 'r', encoding=FILE_ENCODING) as f:
                data = json.load(f)

            # ��������ƥ��Ĺ�˾����
            matching_order_nos = [
                order["order_no"]
                for order in data.get("DeliveryOrders", [])
                if company_name.lower() in order["company_name"].lower()
            ]

            if not matching_order_nos:
                print(f'δ�ҵ���˾������"{company_name}"�Ķ�����')
            return matching_order_nos
        except json.JSONDecodeError:
            print("JSON �ļ�����ʧ�ܣ�")
            return []
        except Exception as e:
            print(f"��������: {e}")
            return []

    @staticmethod
    def sort_orders_by_order_no(orders):
        """����orders�б�����������ֵ"""
        sorted_orders = sorted(orders, key=lambda x: x['order_no'])
        return sorted_orders
# TODO ��ҪUIʵ��һ���������ܣ��������֣���ʾ�ҵ������ġ��ܼۡ��������ڡ����������š�

if __name__ == "__main__":
    operation = Operation()
    print(operation.find_order_by_order_no('A'))
