# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/15}
import time
import threading


def test():
    num = 0
    for one in range(100000):
        num += 1


if __name__ == '__main__':
    start_time = time.time()
    test()
    test()
    end_time = time.time()
    print(f'耗时-常规>>>{end_time - start_time}')

    start_time = time.time()
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test)
    # 启动线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print(f'耗时-多线程>>>{end_time - start_time}')
