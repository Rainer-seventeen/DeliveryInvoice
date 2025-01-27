# -*- coding: gbk -*-

def float_to_chinese_uppercase(amount):
    units = ["", "ʰ", "��", "Ǫ"]
    big_units = ["", "��", "��"]
    chinese_numerals = "��Ҽ��������½��ƾ�"
    fraction_units = ["��", "��"]

    def integer_to_chinese(integer_part):
        result = []
        unit_pos = 0  # ��Ӧunits����λ��
        zero_flag = False  # �Ƿ���Ҫ���롰�㡱

        while integer_part > 0:
            current = integer_part % 10
            if current == 0:
                if not zero_flag and len(result) > 0:  # �����ظ���
                    result.append(chinese_numerals[0])
                    zero_flag = True
            else:
                result.append(units[unit_pos])
                result.append(chinese_numerals[current])
                zero_flag = False
            unit_pos = (unit_pos + 1) % 4
            if unit_pos == 0:  # ÿ��λ���һ����λ
                if integer_part // 10 > 0:  # ���ⲻ��Ҫ�Ĵ�λ
                    result.append(big_units[len(result) // 8])
            integer_part //= 10

        result.reverse()
        return "".join(result).strip("��") or "��"

    def fraction_to_chinese(fraction_part):
        result = []
        for i in range(2):  # �ǡ�����λС��
            fraction_part *= 10
            digit = int(fraction_part) % 10
            if digit != 0:
                result.append(chinese_numerals[digit] + fraction_units[i])
        return "".join(result) or "��"

    if amount < 0:
        return "��" + float_to_chinese_uppercase(-amount)

    integer_part = int(amount)
    fraction_part = round(amount - integer_part, 2)

    integer_result = integer_to_chinese(integer_part)
    fraction_result = fraction_to_chinese(fraction_part)

    return f"{integer_result}Ԫ{fraction_result}"


# # ����
# print(float_to_chinese_uppercase(1234567890.56))  # Ҽʰ������Ǫ������ʰ½����Ǫ�ư۾�ʰԪ���½��
# print(float_to_chinese_uppercase(100400.00))  # Ҽʰ��������Ԫ��
# print(float_to_chinese_uppercase(0.07))  # ��Ԫ���
