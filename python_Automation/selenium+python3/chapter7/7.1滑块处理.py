# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/15}

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 设置隐性等待
driver.implicitly_wait(5)
# 访问网址
driver.get("https://passport.ctrip.com/user/reg/home")

# 设置全屏显示
driver.maximize_window()
sleep(5)
# 点击同意并继续
driver.find_element_by_link_text("同意并继续").click()

"""
# 通过距离滑动
# 获取滑块元素
sour = driver.find_element_by_class_name("cpt-drop-btn")
# sour = driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-drop-btn")
# print(sour.size["width"])
# print(sour.size["height"])
# 获取滑块区域元素
ele = driver.find_element_by_class_name("cpt-bg-bar")
# print(ele.size["width"])
# print(ele.size["height"])
sleep(3)
# 拖动滑块,两种方法选其一
# ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], 0).perform()
ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()
"""
# 通过位置滑动
startPst = driver.find_element_by_class_name("cpt-img-double-right-outer")
endPst = driver.find_element_by_class_name("cpt-img-check-right")
sleep(2)
ActionChains(driver).drag_and_drop(startPst, endPst).perform()

# 释放资源，退出浏览器
# driver.quit()
