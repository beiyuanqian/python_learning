# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/19}

import socket
# 创建socket对象
sk = socket.socket()
# 客户端不需要设置ip地址和端口号，ip地址是设备的ip地址，端口号为系统分配的一个空闲的端口号
# 发起连接
sk.connect(('127.0.0.1', 13000))
# 发送数据到服务端
sk.sendall(input(">>>").encode("utf8"))
# 接收数据，接受服务器发来的消息
sever_data = sk.recv(1024)
print(sever_data.decode("utf8"))
