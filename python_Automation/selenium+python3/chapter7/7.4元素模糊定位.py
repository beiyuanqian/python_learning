# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/16}

from selenium import webdriver

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")

"""
# 访问网址
driver.get("D:\PYproject\\test\selenium+python3\chapter7\\beijing.html")
#模糊定位方法一：starts-with
#使用模糊定位方式来定位超链接“东城区”
res = driver.find_element_by_xpath("//*[starts-with(@id,'dongcheng')]")
# 检测代码定位是否成功
if res:
    print("Starts-with定位元素成功")
else:
    print("Starts-with定位元素失败")
#模糊定位方法二：contains
#使用模糊定位方式来定位超链接“西城区”
res = driver.find_element_by_xpath("//*[contains(@id,'dongcheng')]")
# 检测代码定位是否成功
if res:
    print("Contains定位元素成功")
else:
    print("Contains定位元素失败")
"""

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 设置隐性等待
driver.implicitly_wait(20)
# 访问网址
driver.get("https://www.baidu.com")
driver.maximize_window()
sleep(5)

ActionChains(driver).move_to_element(driver.find_element_by_link_text("设置")).perform()
sleep(3)
driver.find_element_by_class_name("setpref").click()
sleep(3)
r = driver.find_elements_by_name("SL")
r.pop(1).click()

# 释放资源，退出浏览器
# driver.quit()
