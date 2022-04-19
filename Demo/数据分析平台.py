# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/16}

from selenium import webdriver

# 创建浏览器对象
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get('https://172.28.31.196/databoard/starter.html')
# 设置全屏显示
driver.maximize_window()

# 截屏，截取整个页面，./是当前路径,建议使用png格式
driver.get_screenshot_as_file("./all.png")

# 截屏，截取单个元素.form是表单的意思
ele = driver.find_element_by_id('form')
ele.screenshot("./ele.png")

driver.quit()
