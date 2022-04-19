# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/3}

""" 输入十个数字，五个为一组,分两组，每组里的数字相加，问两组的差最少为多少"""

import random

num_list = [random.randint(1, 99) for i in range(10)]
num_list.sort()
num_list_1 = num_list[:5]
num_list_2 = num_list[5:]
print(num_list_1)
print(num_list_2)

sum_1 = num_list_1[0] + num_list_1[1] + num_list_2[-1] + num_list_2[-2]
print(sum_1)
sum_2 = num_list_1[-1] + num_list_1[-2] + num_list_2[0] + num_list_2[1]
print(sum_2)
if sum_1 > sum_2:
    sum_1 = sum_1 + min(num_list_1[2], num_list_2[2])
    sum_2 = sum_2 + max(num_list_1[2], num_list_2[2])
else:
    sum_2 = sum_2 + min(num_list_1[2], num_list_2[2])
    sum_1 = sum_1 + max(num_list_1[2], num_list_2[2])
print(sum_1, sum_2)
print(abs(sum_1 - sum_2))
