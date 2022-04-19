# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/28}

import os
import socket

def post_file(sk_obj, file_path):
    """
    发送文件
    :param sk_obj:socket对象
    :param file_path:文件路径
    ：return:None
    """
    # 发送文件大小
    file_size = os.stat(file_path).st_size  # 获取文件大小
    file_size = str(file_size)  # 将int转为str
    file_size = file_size.encode("utf8")  # 将str转为bytes
    sk_obj.sendall(file_size)
    sk_obj.recv(1024)
    # 发送文件名称
    sk_obj.sendall(os.path.split(file_path)[1].encode("utf8"))
    sk_obj.recv(1024)
    # 发送文件内容
    with open(file_path, "rb") as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size = file_size - 1024


def get_file(sk_obj):
    """
    接收文件
    :param sk_obj:socket对象
    :return:None
    """
    # 接收文件大小
    file_size = int(sk_obj.recv(1024).decode("utf8"))
    sk_obj.sendall(b"ok")
    # 接收文件名称
    file_name = sk_obj.recv(1024).decode("utf8")
    sk_obj.sendall(b"ok")
    # 接收文件内容
    with open("1.png", "wb") as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size = file_size - 1024

# 创建socket对象
sk = socket.socket()
# 绑定ip地址和端口号
sk.bind(("127.0.0.1", 13000))
# 监听
sk.listen()
# 等待传入连接
conn, addr = sk.accept()

get_file(conn)
# 释放
conn.close()
sk.close()


