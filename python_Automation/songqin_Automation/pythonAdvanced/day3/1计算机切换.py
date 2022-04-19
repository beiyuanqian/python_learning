# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/14}

import threading


def foo(something, num):  # 定义每个线程要执行的函数
    for i in range(num):
        print("CPU正在", something)


# 创建线程实例，target指向任务函数，args为target指向的任务参数
t1 = threading.Thread(target=foo, args=("看电影", 2))  # 生成了一个线程实例
t2 = threading.Thread(target=foo, args=("听音乐", 5))  # 生成了另一个线程实例

# 启动线程
t1.start()
t2.start()
