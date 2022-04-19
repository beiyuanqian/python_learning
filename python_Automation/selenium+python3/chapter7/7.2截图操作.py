# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/15}

from selenium import webdriver
from time import sleep
# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 设置隐性等待
driver.implicitly_wait(10)
"""
# 页面截图
# 访问网址
driver.get("https://www.baidu.com")
# 设置全屏显示
driver.maximize_window()
driver.save_screenshot("1.png")
"""
# 元素截图
from PIL import Image

# 访问网址
driver.get("https://user.qunar.com/passport/login.jsp?")
# 设置全屏显示
driver.maximize_window()
# 选择密码登录
driver.find_element_by_class_name("pwd-login").click()
driver.save_screenshot("2.png")
imgcode = driver.find_element_by_id("vcodeImg")
left = imgcode.location["x"]
top = imgcode.location["y"]
right = left + imgcode.size["width"]
bottom = top + imgcode.size["height"]
im = Image.open("2.png")
im = im.crop((left, top, right, bottom))
im.save("2.1.png")


# 释放资源，退出浏览器
driver.quit()
