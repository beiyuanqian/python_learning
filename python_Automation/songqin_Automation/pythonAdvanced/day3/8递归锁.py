# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/16}

import threading
import time

lockR = threading.RLock()  # 递归锁
# 递归锁内部维护着一把锁和一个计数器，每次上锁，计数器加一，每次解锁，计数器减一，
# 计数器可以大于零，或等于零，但不能小于零


# 面试官
def foo1():
    lockR.acquire()  # 上锁
    print("请解释什么是死锁")
    time.sleep(2)

    lockR.acquire()  # 上锁
    print("发offer")
    time.sleep(2)

    lockR.release()  # 释放锁
    lockR.release()  # 释放锁


# 小明
def foo2():
    lockR.acquire()  # 上锁
    print("请给我发offer")
    time.sleep(2)

    lockR.acquire()  # 上锁
    print("解释了什么是死锁")
    time.sleep(2)

    lockR.release()  # 释放锁
    lockR.release()  # 释放锁


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()
