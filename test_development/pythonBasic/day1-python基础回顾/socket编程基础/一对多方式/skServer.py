#-*- coding: utf-8 -*-
#@File    : skServer.py
#@Time    : 2021/4/13 21:55
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/4/13 
import socketserver
class sqServer(socketserver.BaseRequestHandler):
    def handle(self):
        #1- 描述下服务已经启动
        print('---松勤聊天系统已经上线---')
        #处理逻辑
        while True:
            # 接收数据
            clientData = self.request.recv(1024).decode('utf-8')  # 解码
            print('接收到的服务器端的数据>>> ', clientData)
            #发送数据
            sendData = input("请输入发送数据:")
            self.request.sendall(sendData.encode('utf-8'))  # 编号
        self.request.close()

#2- 创建服务端
server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),sqServer)
#3- 一直运行
server.serve_forever()