# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/6/3}

import socket


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
sk.bind(("127.0.0.1", 13000))
sk.listen()

while True:
    conn, addr = sk.accept()
    # 接受客户端的表明身份
    clientName = conn.recv(1024).decode("utf8")
    print("客户端身份：", clientName)
    conn.sendall(b"ok")

    while True:
        # 收消息
        clientData = conn.recv(1024).decode("utf8")
        print(clientData)
        if clientData == "exit":
            break
        # 发消息
        conn.sendall(handleData(input(">>>")).encode("utf8"))
    conn.close()

if __name__ == "__main__":
    ret = handleData("哈哈")
    print(ret)
