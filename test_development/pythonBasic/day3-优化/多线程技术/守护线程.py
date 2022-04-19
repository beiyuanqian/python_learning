# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/17}

import time
import threading


def test(something):
    print(f'我开始>>>{something}')
    time.sleep(2)
    print(f'我结束>>>{something}')


"""
场景：
    1- IO密集型，如sleep,requests,socket
    2- 
"""
if __name__ == '__main__':
    start_time = time.time()

    # 创建线程
    t1 = threading.Thread(target=test, args=('上课',))
    t2 = threading.Thread(target=test, args=('喝水',))

    # 启动线程
    t1.start()
    t2.start()

    for one in range(2):
        print("主线程在运行!>>>", one)
        time.sleep(1)

    end_time = time.time()
    print(f'耗时>>>{end_time - start_time}')

if __name__ == '__main__':
    start_time = time.time()

    # 创建线程
    t1 = threading.Thread(target=test, args=('上课',))
    t2 = threading.Thread(target=test, args=('喝水',))

    # 启动线程
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    for one in range(2):
        print("主线程在运行!>>>", one)
        time.sleep(1)

    end_time = time.time()
    print(f'耗时>>>{end_time - start_time}')

if __name__ == '__main__':
    start_time = time.time()

    # 创建线程
    t1 = threading.Thread(target=test, args=('上课',))
    t2 = threading.Thread(target=test, args=('喝水',))

    # 守护线程，主线程想要结束可以直接退出，不需要等待子线程
    t1.setDaemon(True)
    t2.setDaemon(True)

    # 启动线程
    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

    for one in range(2):
        print("主线程在运行!>>>", one)
        time.sleep(1)

    end_time = time.time()
    print(f'耗时>>>{end_time - start_time}')

"""
使用场景
1、只有t1.start()，没有t1.join()和t1.setDaemon(True)
    效果：所有线程全部运行，会出现主线程结束后，子线程继续运行，直到结束！
2、只有t1.start()和t1.join()，没有t1.setDaemon(True)
    效果：主线程结束前会等待所有的子线程全部运行完成再结束---阻塞
3、只有t1.setDaemon(True)和t1.start()，没有t1.join()
    效果：主线程结完成，所有子线程都中断
"""