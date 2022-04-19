# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/6/2}
# 先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。
# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
# 然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容
#
# http://mirrors.163.com/centos/6/isos/x86_64/README.txt
# http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt
# 主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中

import requests
import threading

url1 = "http://mirrors.163.com/centos/6/isos/x86_64/README.txt"
url2 = "http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt"

newStr = ""  # 初始化字符串
r = threading.Lock()
def foo(url):
    r.acquire()  # 上锁
    global newStr
    newStr += requests.get(url).text
    r.release()  # 释放

t1 = threading.Thread(target=foo, args=(url1,))
t2 = threading.Thread(target=foo, args=(url2,))
t1.start()
t2.start()
t1.join()
t2.join()

with open("python进阶测试-作业3-task12/readme89.txt", "w", encoding="utf8") as f:
    f.write(newStr)

