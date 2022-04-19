# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/30}

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 13000))
print("小明上线了")

while True:
    # 向女神发送数据
    data = "小明：" + input(">>>")
    # 退出判断
    if "exit" in data:
        break
    sk.sendall(data.encode("utf8"))

    # 接收数据
    data = sk.recv(1024)
    print(data.decode("utf8"))


