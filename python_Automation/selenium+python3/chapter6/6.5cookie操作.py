# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/15}


"""
# 认识cookie
from selenium import webdriver
from time import sleep
# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 设置隐性等待
driver.implicitly_wait(5)
# 访问网址
driver.get("https://www.icourse163.org/")

# 设置全屏显示
driver.maximize_window()
print("before login")
for cookie in driver.get_cookies():
    print(cookie)
# 等待30秒，方便输入登录信息
sleep(30)
print("after login")
for cookie in driver.get_cookies():
    print(cookie)
sleep(5)

# 释放资源，退出浏览器
driver.quit()
"""


# 通过Urllib3和http.cookiejar结合实现对cookie的操作
from urllib import request
import http.cookiejar
import urllib3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 消除ssl警告的信息
urllib3.disable_warnings()
# 创建cookieJar对象
cookie = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# 在打开URL的过程中，会将cookie的信息存放在cookie对象中
req = opener.open('http://sogou.com')
# 遍历cookie对象
for i in cookie:
    print(i.name+":"+i.value)

