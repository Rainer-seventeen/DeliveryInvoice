# -*- coding: gbk -*-
"""用于创建所有的数据操作函数"""

import os
import json

from info import CURRENT_FOLDER
from info import FILE_ENCODING


class Operation:
    def __init__(self):

        self.invoice_path = rf"{CURRENT_FOLDER}{r"\invoice.json"}"

        # 初始化invoice.json文件
        if not os.path.exists(self.invoice_path):
            with open(self.invoice_path, 'w', encoding=FILE_ENCODING) as f:
                json.dump({"DeliveryOrders": []}, f, ensure_ascii=False, indent=4)



    def create_new_order(self, company_name, company_address, company_phone, company_connector, entry_matrix):
        """
        创建一个新的订单字典，供写入 JSON 文件的函数使用。

        参数:
            company_name (str): 公司名称
            company_address (str): 公司地址
            company_phone (str): 公司电话
            company_connector (str): 公司联系人
            products (list): 产品列表，每个产品为一个字典，包含产品详细信息

        返回:
            dict: 格式化后的订单字典
        """
        # 1. 获取订单号
        order_no = self.get_next_order_no()

        # 2. 创建日期和时间
        created_date, created_time = self.generate_current_time()

        # 3. 创建products列表
        products = self.create_products_list(input_matrix = entry_matrix)

        # 3. 计算总金额
        all_total_price = sum(product['quantity'] * product['unit_price'] for product in products)

        # 4. 格式化订单字典
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

        # 5. 格式化产品列表
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
        根据输入的矩阵形式生成 products 列表。

        参数:
            entry_matrix (list): 包含产品信息的矩阵，每行代表一个产品，每列代表以下字段：
                [product_name, product_standard, product_unit, quantity, unit_price, product_description]

        返回:
            list: 符合格式的 products 列表。
        """
        products_list = []
        for idx, entry in enumerate(input_matrix, start=1):
            # 跳过空的 product_name 行
            if not entry[0].strip():
                continue

            # 提取各列数据，处理空值和类型转换
            product_name = entry[0].strip()
            product_standard = entry[1].strip()
            product_unit = entry[2].strip()
            quantity = int(entry[3].strip()) if entry[3].strip().isdigit() else 0
            unit_price = float(entry[4].strip()) if entry[4].strip().replace('.', '', 1).isdigit() else 0.0
            product_description = entry[5].strip()

            # 计算总价
            total_price = round(quantity * unit_price, 2)

            # 创建产品条目
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
        生成年份和月份，格式为 YYYYMM，并在后面添加 '0001'。当前

        返回:
            str: 格式化的字符串，例如 '2024010001'
        """
        from datetime import datetime
        now = datetime.now()
        year_month = now.strftime("%Y%m")
        result = f"{year_month}0001"

        return result

    @staticmethod
    def generate_current_time():
        """
        返回当前日期和时间分别的字符串表示

        返回:
            tuple: (当前日期, 当前时间)，日期格式 "YYYY-MM-DD"，时间格式 "HH:MM:SS"
        """
        from datetime import datetime
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        return current_date, current_time

    def get_next_order_no(self):
        """
        获取 DeliveryOrder 列表中 order_no 字段的最大值，并在其基础上生成下一个值。

        返回:
            str: 下一个可用的 order_no（10位字符串）
        """
        current_min_id = Operation.generate_current_year_month()
        try:
            # 读取现有的 JSON 数据
            with open(self.invoice_path, 'r', encoding=FILE_ENCODING) as f:
                data = json.load(f)

            # 查找最大订单号
            max_order_no = None
            for order in data['DeliveryOrders']:
                order_no = order['order_no']
                if max_order_no is None or int(order_no) > int(max_order_no):
                    max_order_no = order_no

            # 如果最大订单号为空，说明表格是空的，返回当前生成的最小值
            if max_order_no is None:
                return current_min_id  # 空表时返回当前年月

            # 如果当前最大值已经比当前生产的年月值小，说明是新的一个月/年的第一个单子，使用生成的数值
            if int(max_order_no) < int(current_min_id):
                return current_min_id

            # 将 order_no 转换为整数并加 1
            next_order_no = int(max_order_no) + 1
            # 格式化为 10 位字符串
            return f"{next_order_no:010}"

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def find_order_by_order_no(self, order_no):
        """
        根据订单号查找 JSON 文件中的订单条目。
        如果输入-1表示返回所有的订单
        :param order_no:要查找的订单号。-1(int)代表所有订单
        :return: 对应的订单字典，如果未找到，返回 None。

        """
        if not os.path.exists(self.invoice_path):
            print("文件不存在！")
            return None

        try:
            # 读取 JSON 文件内容
            with open(self.invoice_path, 'r', encoding=FILE_ENCODING) as f:
                data = json.load(f)

            # 输入参数是-1则返回所有的订单
            orders = data.get("DeliveryOrders", [])
            if order_no == -1:
                return orders

            # 遍历查找匹配的订单号
            for order in orders:

                if str(order["order_no"]) == str(order_no):
                    return order

            print("未找到匹配的订单号！")
            return None
        except json.JSONDecodeError:
            print("JSON 文件解析失败！")
            return None
        except Exception as e:
            print(f"发生错误: {e}")
            return None

    def find_order_no_by_company_name(self, company_name):
        """
        根据公司名字查找 JSON 文件中的所有订单号。

        参数:
            company_name (str): 要查找的公司名字。

        返回:
            list: 包含所有匹配订单号的列表，如果未找到，返回空列表。
        """
        if not os.path.exists(self.invoice_path):
            print("文件不存在！")
            return []

        try:
            # 读取 JSON 文件内容
            with open(self.invoice_path, 'r', encoding=FILE_ENCODING) as f:
                data = json.load(f)

            # 遍历查找匹配的公司名字
            matching_order_nos = [
                order["order_no"]
                for order in data.get("DeliveryOrders", [])
                if company_name.lower() in order["company_name"].lower()
            ]

            if not matching_order_nos:
                print(f'未找到公司名包含"{company_name}"的订单！')
            return matching_order_nos
        except json.JSONDecodeError:
            print("JSON 文件解析失败！")
            return []
        except Exception as e:
            print(f"发生错误: {e}")
            return []

    @staticmethod
    def sort_orders_by_order_no(orders):
        """输入orders列表，返回排序后的值"""
        sorted_orders = sorted(orders, key=lambda x: x['order_no'])
        return sorted_orders
# TODO 需要UI实现一个搜索功能，搜索名字，显示找到订单的“总价”，“日期”，“订单号”

if __name__ == "__main__":
    operation = Operation()
    print(operation.find_order_by_order_no('A'))
