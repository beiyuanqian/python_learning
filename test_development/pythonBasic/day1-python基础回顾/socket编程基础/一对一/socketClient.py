# -*- coding: utf-8 -*-
# @File    : socketClient.py
# @Time    : 2021/4/13 21:29
# @Author  : xintian
# @Email   : 1730588479@qq.com
# @Software: PyCharm
# Date:2021/4/13
import socket

ip_port = ('127.0.0.1', 9999)
# 1- 创建socket对象---socket也叫套接字
sk = socket.socket()
# 2- 连接服务器
sk.connect(('127.0.0.1', 9999))

# 3- 发送数据
sendData = input("请输入发送数据:")
sk.sendall(sendData.encode('utf-8'))  # 编号

# 5- 接收数据
clientData = sk.recv(1024).decode('utf-8')  # 解码
print('接收到的服务器端的数据>>> ', clientData)

# 7- 关闭socket
sk.close()
