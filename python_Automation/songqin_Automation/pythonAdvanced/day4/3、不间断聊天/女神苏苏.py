# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/29}

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("有人和女神聊天了")

        while True:
            # 接收数据
            client_data = self.request.recv(1024)  # 相当于之前的conn.recv()
            print(client_data.decode("utf8"))
            # 发送数据
            self.request.sendall(input(">>>").encode("utf8"))

server = socketserver.ThreadingTCPServer(("127.0.0.1", 13000), MyServer)
print("女神上线了，并且发了照片，说自己很无聊")
server.serve_forever()




