# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/11/30}

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(r"D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
driver.get("http://venus-manager-test.leayun.cn/")
driver.maximize_window()
sleep(2)

# print("登录前")
# cookies=driver.get_cookies()
# print(cookies)
# sleep(20)
# print("登录后")
# cookies1=driver.get_cookies()
# print(cookies1)
#登录
driver.find_element_by_class_name("tabs")
sleep(2)
driver.find_element_by_tag_name("span").click()
sleep(2)
username=driver.find_element_by_id("username")
username.send_keys("13840492987")
password=driver.find_element_by_id("password")
password.send_keys("a123456")
# 滑块处理
# 获取滑块元素
sour = driver.find_element_by_id("nc_1_n1z")
# sour = driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-drop-btn")
# print(sour.size["width"])
# print(sour.size["height"])
# 获取滑块区域元素
ele = driver.find_element_by_css_selector("#nc_1__scale_text > span")
# print(ele.size["width"])
# print(ele.size["height"])
sleep(3)
# 拖动滑块,两种方法选其一
# ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], 0).perform()
ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()
