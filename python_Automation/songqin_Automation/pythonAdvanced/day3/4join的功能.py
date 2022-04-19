# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/14}

import threading
import time


def foo():
    time.sleep(3)
    print("阳光明媚")


t1 = threading.Thread(target=foo)
t1.start()
# t1.join()  # 在线程t1结束运行之前，阻塞主线程，不让继续往下运行

print("主代码最后一行代码")
print("最后的最后")





