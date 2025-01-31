# -*- coding: gbk -*-
"""存放所有的关于json文件读取和写入的函数"""
import json
import os
from docx import Document

from info import CURRENT_FOLDER
from info import FILE_ENCODING
from operation import Operation
from ChineseUppercase import float_to_chinese_uppercase
from tkinter import messagebox



class Write:
    def __init__(self):
        self.invoice_path = rf"{CURRENT_FOLDER}{r"\invoice.json"}"
        self.framework_path = rf"{CURRENT_FOLDER}{r"\framework.docx"}"
        self.output_path = rf"{CURRENT_FOLDER}{r"\生成后送货单.docx"}"

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

    def write_docx(self, input_dict):
        """

        :param input_dict: 输入的字典类型的数据
        :return:
        """
        # Step 1: 获取数据，在字典中
        titled_price = float_to_chinese_uppercase(input_dict["all_total_price"])
        # Step 2: 打开模板文档
        doc = Document(self.framework_path)

        # Step 3: 替换普通公司信息字段
        # 遍历表格中的所有单元格进行替换
        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                if "<id>" in run.text:  # 检查是否有占位符
                    run.text = run.text.replace("<id>", input_dict["order_no"])
        for table in doc.tables:  # 遍历每个表格
            for row in table.rows:  # 遍历每行
                for cell in row.cells:  # 遍历每个单元格
                    # 遍历单元格内的段落进行替换
                    for paragraph in cell.paragraphs:
                        paragraph.text = paragraph.text.replace("<company_name>", input_dict["company_name"])
                        paragraph.text = paragraph.text.replace("<company_address>", input_dict["company_address"])
                        paragraph.text = paragraph.text.replace("<company_phone>", input_dict["company_phone"])
                        paragraph.text = paragraph.text.replace("<connector>", input_dict["company_connector"])
                        paragraph.text = paragraph.text.replace("<date>", input_dict["created_date"])
                        paragraph.text = paragraph.text.replace("<id>", input_dict["order_no"])
                        paragraph.text = paragraph.text.replace("<all_total_price>", str(input_dict["all_total_price"]))
                        paragraph.text = paragraph.text.replace("<titled_total_price>", titled_price)


        # Step 4: 替换所有 <xx> 占位符
        # # 替换段落中的占位符
        # for paragraph in doc.paragraphs:
        #     for run in paragraph.runs:
        #         if "<" in run.text:  # 检查是否有占位符
        #             run.text = replace_product_placeholder(run.text, products)
        #
        # 替换表格中的占位符
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:  # 遍历单元格中的段落
                        for run in paragraph.runs:  # 遍历段落中的 Run 对象
                            if "<" in run.text:  # 检查是否含有占位符
                                run.text = self.replace_product_placeholder(run.text, input_dict["Products"])

        # Step 5: 保存替换后的文档
        doc.save(self.output_path)
        print(f"生成的新文档已保存至: {self.output_path}")
        if messagebox.askyesno('完成','文件已经成功生成，是否现在打开？'):
            os.startfile(self.output_path)

    @staticmethod
    def replace_product_placeholder(text, input_list):

        products_matrix = []
        for product in input_list:
            product_list = [product["product_name"],product["product_standard"],product["product_unit"],
                    product["quantity"],product["unit_price"],product["product_description"],
                    product["total_price"],product["id"]]

            products_matrix.append(product_list)
        # print(products_matrix)

        import re

        # 正则匹配 <xx> 格式
        pattern = r"<(\d)(\d)>"  # 匹配 <00> 到 <99> 的占位符
        matches = re.findall(pattern, text)

        # 替换所有匹配的占位符
        for match in matches:
            row, col = int(match[0]), int(match[1])  # 提取行和列索引
            if row < len(products_matrix) and col < len(products_matrix[row]):
                text = text.replace(f"<{row}{col}>", str(products_matrix[row][col]))
            else:
                # 如果索引超范围，替换为空字符串
                text = text.replace(f"<{row}{col}>", "")
        return text
if __name__ == '__main__':

    op = Operation()
    out = op.find_order_by_order_no(order_no= 2025010001)
    wt = Write()
    wt.write_docx(out)
