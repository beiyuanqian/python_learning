# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/16}

import threading
import time


balance = 500  # 账户余额
r = threading.Lock()  # 声明一把锁
# 这是一把同步锁，同步锁必须上锁与解锁相对，如果上锁后不解锁，再次上锁代码会阻塞
# 如果解锁之后，没有锁的时候，又进行解锁，代码会报错

# 操作账户余额
def foo(num):
    # 声明全局变量
    global balance

    # r.acquire()  # 上锁
    # 将接口取到的值存进自己的系统变量中
    user_balance = balance
    time.sleep(3)  # 防止代码太少，cpu执行速度过快造成串行
    # 计算出结果
    user_balance = user_balance + num
    # 将结果通过接口传递出去
    balance = user_balance
    # r.release()  # 解锁


# 消费300元
t1 = threading.Thread(target=foo, args=[-300])
# 收入10000元
t2 = threading.Thread(target=foo, args=[10000])

# 启动线程
t1.start()
t2.start()

# 阻塞主线程
t1.join()
t2.join()

print("最终余额", balance)





