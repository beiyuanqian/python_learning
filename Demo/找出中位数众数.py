# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/3}

"""
 输入一串数字，找出他们中的众数，再在众数中找中位数
"""

import collections

num_list = [10, 11, 21, 19, 21, 17, 21, 16, 21, 18, 15, 17, 17, 17]
print(num_list)
# 寻找众数
data = collections.Counter(num_list)
dict_list = dict(data)
# print(dict_list)
max_list = []
mode_val = [key for key, value in dict_list.items() if value == max(list(data.values()))]
print("  列表的众数是 " + ', '.join(map(str, mode_val)))

# 寻找中位数
max_list.sort()
if len(max_list) % 2 == 0:
    first_num = num_list[len(num_list) // 2 - 1]
    second_num = num_list[len(num_list) // 2]
    median = (first_num + second_num) / 2
else:
    median = num_list[len(num_list) // 2]
print("  列表的中位数是 " + str(median))
