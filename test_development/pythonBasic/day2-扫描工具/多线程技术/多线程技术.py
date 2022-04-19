# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/15}
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
    # 创建线程,threading.Thread(target=,args=),
    # target=指带定义的线程要做的事情是什么，一般是一个函数或者方法，只能传递函数名
    # args=这个函数或者方法需要传入的参数，是一个元组类型
    t1 = threading.Thread(target=test, args=('上课',))
    t2 = threading.Thread(target=test, args=('喝水',))
    # test('上课')
    # test('喝水')
    # 启动线程
    t1.start()
    t2.start()
    #主线程执行的时候，并没有去等待子线程t1,t2执行完成，希望主线程退出前，检查下子线程是否运行完，子线程运行完，主线程再退出
    t1.join()
    t2.join()
    end_time = time.time()
    print(f'耗时>>>{end_time - start_time}')
