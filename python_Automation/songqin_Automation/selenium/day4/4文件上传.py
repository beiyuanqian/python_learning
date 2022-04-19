# author:刘小涵  time:2020/3/28

"""
对于通过input标签实现的上传功能，可以将其看作是一个输入框，即通过send_keys()指定本地文件路径的方式实现文件上传
对于非 input 标签实现的上传功能，我们可以通过模拟键盘敲击的方式实现，代码如下
"""

from selenium import webdriver
import win32com.client
import time

driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://tinypng.com/")

# 触发上传文件的操作

driver.find_element_by_xpath("//*[@id=\"top\"]/section/div[1]/section").click()
# 创建脚本对象,即敲击键盘所需要用到的对象
time.sleep(5)
sh = win32com.client.Dispatch("WScript.shell")
# 操作键盘，无目标的，单纯的敲击键盘
sh.Sendkeys("D:\PYproject\ell.png\r\n" )

"""
如果支持多文件上传，则使用sh.Sendkeys(""""D:\PYproject\ell.png" "D:\PYproject\ell.png\r\n"""")
使用shell对象的Sendkeys方法给应用程序发送字符串
输入要上传的文件或者图片路径
有的系统要加 ‘\r’
有的系统要加 ‘\r\n’
"""
# driver.quit()
