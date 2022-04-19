# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/22}

"""
版本：1.0
需求：实现一个接口测试工具，带GUI页面样式
功能描述：实现接口测试，方便测试人员测试
"""
# 1、导入应用对象
from PySide2.QtWidgets import QApplication
# 2、界面ui文件需要导入到代码里去
from PySide2.QtUiTools import QUiLoader
# 3、导入读取ui文件的库
from PySide2.QtCore import QFile
import json
import requests
import threading

"""
后端处理流程：
1、发送请求
    1、使用对应的requests库操作：
        请求方法（4种方法）；
            1、if条件判断决定使用哪个requests.get/post
            2、request.Request(url,method)
        请求url、
        请求头：最好输入字典格式
        请求body：最好输入字典格式
    2、点击发送按钮
2、显示响应
3、清空数据
"""


class HttpClient:
    def __init__(self, uiName='接口工具.ui'):  # 初始化方法，只要创建实例，就会自动调用
        # 5、获取ui文件
        self.qFile = QFile(uiName)
        # 6、打开这个ui文件
        self.qFile.open(QFile.ReadOnly)
        # 7、加载ui对象
        self.ui = QUiLoader().load(self.qFile)
        # 8、关闭qfile文件
        self.qFile.close()
        # 关联按钮
        self.ui.pushButton.clicked.connect(self.request_send)

    # 封装发送方法
    def request_send(self):
        # 获取请求方法
        method = self.ui.comboBox.currentText()  # 当前的值
        # 请求的url
        url = self.ui.lineEdit.text()
        # 请求头，从控件获取的数据时str,转化成dict
        header = self.ui.plainTextEdit.toPlainText()
        if header.strip() != "":
            header = json.loads(header)
        # 请求体
        payload = self.ui.plainTextEdit_2.toPlainText()
        if payload.strip() != "":
            payload = json.loads(payload)
        # 打印信息，调试
        print(method, url, header, payload, sep="\n")
        # 发送请求
        req = requests.Request(method, url, headers=header, data=payload)
        prepare = req.prepare()  # 获取请求数据
        s = requests.Session()  # 创建会话
        # 直接发送
        # resp = s.send(prepare)
        t1 = threading.Thread(target=self.thread_send, args=(s, prepare))
        t1.start()
        # t1.join()# 如果加了join，一旦url接口不通，这个GUI页面不能继续操作，会等待这个接口出结果才可以操作

    # # 有一个想法，一个线程，如果url不存在，GUI会卡住
    def thread_send(self, s, prepare):
        resp = s.send(prepare)
        self.show_response(resp)

    def show_response(self, resp):
        # 响应头
        resp.encoding = "UTF-8"
        self.ui.textBrowser.append(
            "HTTP/1.1 {} \n{} \n\n{}".format(
                resp.status_code,  # 状态码
                '\n'.join('{}:{}'.format(k, v) for k, v in resp.headers.items()),  # 响应头
                resp.text  # 响应体
            )
        )


# 4、需要一个应用程序对象
app = QApplication([])  # sys.argv
httpClient = HttpClient()
# 9、显示这个ui
httpClient.ui.show()
# 10、运行应用对象
app.exec_()
