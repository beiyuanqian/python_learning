# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/6/3}

import socket

name = "Nathandle1"


def handleData(data):
    """
    将消息处理为特定格式woi
    :param data: 消息原文
    :return: 处理后的消息
    """
    #  先处理消息的第二部分
    if data == "Nathanle1":
        dataType = "1"
    else:
        dataType = "2"
    #  处理消息的第一部分
    strLen = len(data)
    if len(str(strLen)) < 4:
        dataLen = "0" * (4 - len(str(strLen))) + str(strLen)
    else:
        dataLen = str(strLen)
    return "|".join([dataLen, dataType, data])


sk = socket.socket()
sk.connect(("127.0.0.1", 13000))

# 自报家门
sk.sendall(handleData(name).encode("utf8"))
sk.recv(1024)
while True:
    # 发送消息
    inp = input(">>>")
    sk.sendall(handleData(inp).encode("utf8"))
    if inp == "exit":
        break
    # 收消息
    serverData = sk.recv(1024).decode("utf8")
    print(serverData)
