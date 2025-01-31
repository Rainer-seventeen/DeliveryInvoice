# -*- coding: gbk -*-

def float_to_chinese_uppercase(amount):
    units = ["", "拾", "佰", "仟"]
    big_units = ["", "万", "亿"]
    chinese_numerals = "零壹贰叁肆伍陆柒捌玖"
    fraction_units = ["角", "分"]

    def integer_to_chinese(integer_part):
        result = []
        unit_pos = 0  # 对应units数组位置
        zero_flag = False  # 是否需要插入“零”

        while integer_part > 0:
            current = integer_part % 10
            if current == 0:
                if not zero_flag and len(result) > 0:  # 避免重复零
                    result.append(chinese_numerals[0])
                    zero_flag = True
            else:
                result.append(units[unit_pos])
                result.append(chinese_numerals[current])
                zero_flag = False
            unit_pos = (unit_pos + 1) % 4
            if unit_pos == 0:  # 每四位添加一个大单位
                if integer_part // 10 > 0:  # 避免不必要的大单位
                    result.append(big_units[len(result) // 8])
            integer_part //= 10

        result.reverse()
        return "".join(result).strip("零") or "零"

    def fraction_to_chinese(fraction_part):
        result = []
        for i in range(2):  # 角、分两位小数
            fraction_part *= 10
            digit = int(fraction_part) % 10
            if digit != 0:
                result.append(chinese_numerals[digit] + fraction_units[i])
        return "".join(result) or "整"

    if amount < 0:
        return "负" + float_to_chinese_uppercase(-amount)

    integer_part = int(amount)
    fraction_part = round(amount - integer_part, 2)

    integer_result = integer_to_chinese(integer_part)
    fraction_result = fraction_to_chinese(fraction_part)

    return f"{integer_result}元{fraction_result}"


# # 测试
# print(float_to_chinese_uppercase(1234567890.56))  # 壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾元伍角陆分
# print(float_to_chinese_uppercase(100400.00))  # 壹拾万零肆佰元整
# print(float_to_chinese_uppercase(0.07))  # 零元柒分
