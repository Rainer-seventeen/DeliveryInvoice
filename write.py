# -*- coding: gbk -*-
"""存放所有的关于json文件读取和写入的函数"""
import json
import os

from info import CURRENT_FOLDER
from info import FILE_ENCODING
from operation import Operation



class Write:
    def __init__(self):
        self.invoice_path = rf"{CURRENT_FOLDER}{r"\invoice.json"}"

        #初始化invoice.json文件
        if not os.path.exists(self.invoice_path):
            with open(self.invoice_path, 'w', encoding= FILE_ENCODING) as f:
                json.dump({"DeliveryOrders": []}, f, ensure_ascii=False, indent=4)

    def add_new_invoice(self,company_name, company_address, company_phone, company_connector, entry_matrix):
        """
        写入json总入口，对外封装函数
        :param company_name: 公司名称
        :param company_address: 公司地址
        :param company_phone: 公司电话
        :param company_connector:公司联系人
        :param entry_matrix:输入矩阵（通过ui直接传入）
        """
        op = Operation()
        order_list = op.create_new_order(company_name, company_address, company_phone, company_connector, entry_matrix)
        self.write_invoice_json(order_list)

    def write_invoice_json(self, new_order):
        """
        将生成的字典写入json文件
        :param new_order: 字典类型的数据，由create_new_order()创建
        """
        # 如果文件不存在，创建文件并初始化为一个空的 delivery orders 数组


        # 读取已有的 JSON 数据
        with open(self.invoice_path, 'r', encoding= FILE_ENCODING) as f:
            data = json.load(f)

        # 添加新的送货单数据
        data['DeliveryOrders'].append(new_order)

        # 写回 JSON 文件
        with open(self.invoice_path, 'w', encoding= FILE_ENCODING) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("新的送货单已添加成功！")




company_name = "上海市A公司"
address_name = "浦东大道"
company_phone = "123"
company_connector = "联系人"
output_data = [
    ['产品A', '无', '无', '10', '5', '无'],
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