# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/9/25}
# 随机数
import random

print(int(random.random()*10000))
print(random.randint(0,1000))

# 时间戳,从1970-01-01 00：00：00到现在所经历过的毫秒数
import time
print(int(time.time()*10000000))
