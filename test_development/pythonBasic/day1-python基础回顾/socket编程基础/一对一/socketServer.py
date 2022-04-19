# -*- coding: utf-8 -*-
# @File    : socketServer.py
# @Time    : 2021/4/13 21:29
# @Author  : xintian
# @Email   : 1730588479@qq.com
# @Software: PyCharm
# Date:2021/4/13
import socket

ip_port = ('127.0.0.1', 9999)
# 1- 创建socket对象---socket也叫套接字
sk = socket.socket()
# 2- 绑定ip 端口
sk.bind(ip_port)
# 3- 开启监听
sk.listen()
print('---socket服务器已经启动完成---')
# 4- 阻塞 等待客户端来链接  可以返回 连接对象,客户端的ip
conn, addr = sk.accept()
# 5- 接收数据
clientData = conn.recv(1024).decode('utf-8')  # 解码
print('接收到的客户端数据>>> ', clientData)
# 6- 发送数据
sendData = input("请输入发送数据:")
conn.sendall(sendData.encode('utf-8'))  # 编号
# 7- 关闭socket
sk.close()
