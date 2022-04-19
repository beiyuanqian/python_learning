# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/16}

import threading
import time

lockA = threading.Lock()  # 面试官的锁
lockB = threading.Lock()  # 小明的锁

# 面试官
def foo1():
    lockA.acquire()  # 上锁
    print("请解释什么是死锁")
    time.sleep(2)

    lockB.acquire()  # 上锁
    print("发offer")
    time.sleep(2)

    lockA.release()  # 释放锁
    lockB.release()  # 释放锁

# 小明
def foo2():
    lockB.acquire()  # 上锁
    print("请给我发offer")
    time.sleep(2)

    lockA.acquire()  # 上锁
    print("解释了什么是死锁")
    time.sleep(2)

    lockA.release()  # 释放锁
    lockB.release()  # 释放锁


t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()
