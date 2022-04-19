# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/17}
"""
原本卡里余额1000元，现在有两笔交易
1、进账500
2、支出200
"""
import time
import threading

balance = 1000

# # 未用锁时，进程执行顺序不一致，导致结果不正确
# def test(num):
#     global balance  # 使用全局变量
#     # 使用一个变量存放余额
#     userBalance = balance
#     # 进出帐操作
#     userBalance = userBalance + num
#
#     time.sleep(2)  # 模拟处理时间
#     balance = userBalance
#
#
# if __name__ == '__main__':
#     test(500)
#     print("卡里余额为：", balance)
#
#
# if __name__ == '__main__':
#     # 进账500元
#     t1 = threading.Thread(target=test, args=(500,))
#     t2 = threading.Thread(target=test, args=(-200,))
#
#     # 开始
#     t1.start()
#     t2.start()
#     # 阻塞主线程运行
#     t1.join()
#     t2.join()
#     # test(-500)
#     print("卡里余额为：", balance)


# 用锁
lock = threading.Lock()


def test(num):
    # 使用全局变量
    global balance
    # 上锁
    lock.acquire()
    # 使用一个变量存放余额
    userBalance = balance
    # 进出帐操作
    userBalance = userBalance + num
    # 模拟处理时间
    time.sleep(2)
    balance = userBalance
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 进账500元
    t1 = threading.Thread(target=test, args=(500,))
    t2 = threading.Thread(target=test, args=(-200,))

    # 开始
    t1.start()
    t2.start()
    # 阻塞主线程运行
    t1.join()
    t2.join()
    # test(-500)
    print("卡里余额为：", balance)
