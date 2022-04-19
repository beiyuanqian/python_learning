# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/17}

import time, re, threading

# def f1():
#     for i in range(0, 5):
#         print('f1正在运行>>>', i)
#         time.sleep(2)
#
#
# def f2():
#     for i in range(0, 5):
#         print('f2正在运行>>>', i)
#         time.sleep(2)

# if __name__ == '__main__':
#     starttime = time.time()
#
#     f1()
#     f2()
#
#     endtime = time.time()
#     print(f'扫描过程耗时：{endtime - starttime}')

import gevent
from gevent import monkey

monkey.patch_all()


def f(num):
    for i in range(0, 2):
        print(f"f{num}-正在运行>>> ", i)
        time.sleep(2)


if __name__ == '__main__':
    starttime = time.time()

    # 创建协程
    g1 = gevent.spawn(f, 1)
    g2 = gevent.spawn(f, 2)
    gevent.joinall([g1, g2])
    # f1()
    # f2()

    endtime = time.time()
    print(f'扫描过程耗时：{endtime - starttime}')
