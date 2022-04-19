# author:刘小涵  time:2020/3/24

from selenium import webdriver
import time

# 创建浏览器驱动
driver = webdriver.Chrome('驱动路径')
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get('网址')
driver.get("http://www.baidu.com")
# 找到搜索框
inputElement = driver.find_element_by_id("id值")
inputElement = driver.find_element_by_id("kw")
# 对文本框输入搜索内容
inputElement.send_keys("需要输入的文本内容")
inputElement.send_keys("松勤")
# 元素定位，找到搜索按钮
searchElement = driver.find_element_by_id("su")
# 点击搜索按钮
searchElement.click()

time.sleep(5)
# 释放资源，退出浏览器
driver.quit()
