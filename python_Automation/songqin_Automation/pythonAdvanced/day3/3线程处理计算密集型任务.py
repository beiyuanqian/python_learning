# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/14}

import threading
import time


def foo():
    num = 0
    for i in range(10000000):
        num += 1


begin_time = time.time()
"""
# 串行总消耗时长 0.8205559253692627
foo()
foo()
"""

# 并发
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)

t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print("总消耗时长", end_time - begin_time)


