# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/3}

"""
输入一个数字，对当前数字加一；减一；除以二(如果当前是偶数的话)各算一次操作， 要求把它变成1的最少操作次数。
"""

import random

n = random.randint(0, 99)
print(n)
while True:
    if n < 1:
        break
    elif n % 2 == 0:
        n // 2

    elif n % 2 != 0:
        min(n // 2 + 1, n // 2 - 1)
