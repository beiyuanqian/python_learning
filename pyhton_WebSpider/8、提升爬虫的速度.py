# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/15}

# 多线程爬虫
# # 以单线程（单进程）的方式抓取1000个网页
# import requests
# import time
#
# link_list = []
# with open(r'D:\PYproject\pyhton爬虫\alexa - 副本.txt', 'r')as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1].replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
# for eachone in link_list:
#     try:
#         r = requests.get(eachone)
#         print(r.status_code, eachone)
#     except Exception as e:
#         print('ERROE', e)
# end = time.time()
# print('串行的总时间为：', end - start)

# python使用多线程的两种方法
# # （1）函数式：调用_thread模块中的start_new_thread()函数产生新线程
# import _thread
# import time
#
#
# # 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 3:
#         time.sleep(delay)
#         count += 1
#         print(threadName, time.ctime())
#
#
# _thread.start_new_thread(print_time, ('Thread-1', 1))
# _thread.start_new_thread(print_time, ('Thread-2', 2))
# print('Main Finished')

# # （2）类包装式：调用Threading库创建线程，从threading.Thread继承
# import threading
# import time
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print('Starting' + self.name)
#         print_time(self.name, self.delay)
#         print('Exiting' + self.name)
#
#
# def print_time(threadName, delay):
#     counter = 0
#     while counter < 3:
#         time.sleep(delay)
#         print(threadName, time.ctime())
#         counter += 1
#
#
# threads = []
# # 创建新线程
# thread1 = myThread('Thread-1', 1)
# thread2 = myThread('Thread-2', 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print('Exiting Main Thread')

# # 将多线程的代码应用在获取1000个网页上
# import requests
# import threading
# import time
#
# link_list = []
# with open(r'D:\PYproject\pyhton爬虫\alexa - 副本.txt', 'r')as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1].replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, link_range):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.link_range = link_range
#
#     def run(self):
#         print('Starting ' + self.name)
#         crawler(self.name, self.link_range)
#         print('Exiting ' + self.name)
#
#
# def crawler(threadName, link_range):
#     for i in range(link_range[0], link_range[1] + 1):
#         try:
#             r = requests.get(link_list[i], timeout=20)
#             print(threadName, r.status_code, link_list[i])
#         except Exception as e:
#             print(threadName, 'ERROR：', e)
#
#
# thread_list = []
# link_range_list = [(0, 20), (21, 40), (41, 60), (61, 80), (81, 100)]
# # 创建新线程
# for i in range(1, 6):
#     thread = myThread('Thread-' + str(i), link_range_list[i - 1])
#     thread.start()
#     thread_list.append(thread)
# # 等待所有线程完成
# for thread in thread_list:
#     thread.join()
# end = time.time()
# print('简单多线程爬虫的总时间为：', end - start)
# print('Exiting Main Thread')

# # 使用Queue的多线程爬虫，Queue模块中提供了同步的、线程安全的队列类，
# # 包括FIFO（先入先出）队列Queue、LIFO（后入先出）队列LifoQueue和优先级队列PriorityQueue
# import threading
# import requests
# import time
# import queue as Queue
#
# link_list = []
# with open(r'D:\PYproject\pyhton爬虫\alexa - 副本.txt', 'r')as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1].replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, q):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.q = q
#
#     def run(self):
#         print('Starting ' + self.name)
#         while True:
#             try:
#                 crawler(self.name, self.q)
#             except:
#                 break
#         print('Exiting ' + self.name)
#
#
# def crawler(threadName, q):
#     # 获取队列中的链接
#     url = q.get(timeout=2)
#     try:
#         r = requests.get(url, timeout=20)
#         print(q.qsize(), threadName, r.status_code, url)
#     except Exception as e:
#         print(q.qsize(), threadName, url, 'ERROR：', e)
#
#
# threadList = ['Thread-1', 'Thread-2', 'Thread-3', 'Thread-4', 'Thread-5']
# # 建立队列对象，然后将这个对象传入myThread中
# workQueue = Queue.Queue(100)
# threads = []
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(tName, workQueue)
#     thread.start()
#     threads.append(thread)
# # 填充队列，为什么填充队列不放在创建线程之前就可以用？？？？？？
# for url in link_list:
#     workQueue.put(url)
# # 等待所有线程完成
# for t in threads:
#     t.join()
# end = time.time()
# print('Queue多线程爬虫的总时间为：', end - start)
# print('Exiting Main Thread')

# # 多进程爬虫，需要用到multiprocess库，有两种方法：
# # (1)使用Process+Queue的方法
# from multiprocessing import cpu_count, Process, Queue
# import time
# import requests
#
# print('计算机CPU的核心数量', cpu_count())
# link_list = []
# with open(r'D:\PYproject\pyhton爬虫\alexa - 副本.txt', 'r')as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1].replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
#
#
# class MyProcess(Process):
#     def __init__(self, q):
#         Process.__init__(self)
#         self.q = q
#
#     def run(self):
#         print("Starting ", self.pid)
#         while not self.q.empty():
#             crawler(self.q)
#         print("Exiting ", self.pid)
#
#
# def crawler(q):
#     url = q.get(timeout=2)
#     try:
#         r = requests.get(url, timeout=20)
#         print(q.qsize(), r.status_code, url)
#     except Exception as e:
#         print(q.qsize(), url, 'ERROR：', e)
#
#
# if __name__ == '__main__':
#     ProcessName = ['Process-1', 'Process-2', 'Process-3']
#     workQueue = Queue(100)
#     # 填充队列
#     for url in link_list:
#         workQueue.put(url)
#     for i in range(0, 3):
#         p = MyProcess(workQueue)
#         print(p)
#         # daemon设置为True，当父进程结束后，子进程就会自动被终止
#         p.daemon = True
#         p.start()
#         p.join()
#     end = time.time()
#     print('Process+Queue多进程爬虫的总时间为：', end - start)
#     print('Main process Ended!')

# # 使用Pool+Queue的方法
# from multiprocessing import Pool, Manager
# import time
# import requests
#
# link_list = []
# with open(r'D:\PYproject\pyhton爬虫\alexa - 副本.txt', 'r')as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1].replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
#
#
# def crawler(q, index):
#     Proces_id = 'Process-' + str(index)
#     while not q.empty():
#         url = q.get(timeout=2)
#         try:
#             r = requests.get(url, timeout=20)
#             print(Proces_id, q.qsize(), r.status_code, url)
#         except Exception as e:
#             print(Proces_id, q.qsize(), url, 'ERROR：', e)
#
#
# if __name__ == '__main__':
#     manager = Manager()
#     workQueue = manager.Queue(100)
#
#     # 填充队列
#     for url in link_list:
#         workQueue.put(url)
#
#     # 创建线程池的最大值为3
#     pool = Pool(processes=3)
#     for i in range(4):
#         # 使用非阻塞方法添加进程，不一定非要等到结果出来就可以添加其它进程运行
#         pool.apply_async(crawler, args=(workQueue, i))
#         # # 使用阻塞方法要等到回调结果出来，在有结果之前，当前进程会被挂起
#         # pool.apply(crawler, args=(workQueue, i))
#
#     print('Started processes')
#     pool.close()
#     pool.join()
#
#     end = time.time()
#     print('Pool+Queue多进程爬虫的总时间为：', end - start)
#     print('Main process Ended!')

# 多协程爬虫
import gevent
from gevent.queue import Queue, Empty
import time
import requests
# 把下面有可能有IO操作的单独坐上标记
from gevent import monkey

# 将IO转为异步执行的函数
monkey.patch_all()

link_list = []
with open(r'D:\PYproject\pyhton爬虫\alexa - 副本.txt', 'r')as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1].replace('\n', '')
        link_list.append(link)

start = time.time()


def crawler(index):
    Process_id = 'Process-' + str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout=2)
        try:
            r = requests.get(url, timeout=20)
            print(Process_id, workQueue.qsize(), r.status_code, url)
        except Exception as e:
            print(Process_id, workQueue.qsize(), url, 'ERROR：', e)


def boss():
    for url in link_list:
        workQueue.put_nowait(url)


if __name__ == '__main__':
    workQueue = Queue(100)

    gevent.spawn(boss).join()
    jobs=[]
    for i in range(10):
        jobs.append(gevent.spawn(crawler,i))
    gevent.joinall(jobs)

    end=time.time()
    print('gevent+Queue多协程爬虫的总时间为：',end-start)
    print('Main Ended!')
