# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/20}

"""
版本：1.0
需求：实现一个接口测试工具，带GUI页面格式
功能描述：1、实现接口测试，2、方便测试人员操作
实现方案：1、GUI编程，2、接口requeste库
"""
# 1、导入应用对象
from PySide2.QtWidgets import QApplication
# 2、界面ui文件需要导入到代码里去
from PySide2.QtUiTools import QUiLoader
# 3、导入读取ui文件的库
from PySide2.QtCore import QFile

# 4、需要一个应用程序对象
app = QApplication([])  # sys.argv
# 5、获取ui文件
qFile = QFile(r'D:\PYproject\测试开发\模块一：python基础\day4-\登录.ui')
# 6、打开这个ui文件
qFile.open(QFile.ReadOnly)
# 7、加载ui对象
ui = QUiLoader().load(qFile)
# 8、关闭qfile文件
qFile.close()


# ---------登录操作---------
def login():
    # 账号获取
    username = ui.lineEdit.text()
    # 密码获取
    password = ui.lineEdit_2.text()
    # 显示登录结果
    # print(username,password)
    ui.textBrowser.append(f"用户{username}，登录成功")



def exit():
    ui.textBrowser.clear()
    # 清除


# 动作关联
ui.pushButton.clicked.connect(login)
ui.pushButton_2.clicked.connect(exit)

#下拉菜单设置
# ui.comboBox.addItems(["1","2","3"])

#获取当前下拉菜单栏的选项
print(ui.comboBox.currentText())
ui.radioButton.setChecked(True)

# 9、显示这个ui
ui.show()
# 10、运行应用对象
app.exec_()
