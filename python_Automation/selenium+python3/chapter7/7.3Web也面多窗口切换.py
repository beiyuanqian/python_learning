# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/15}

from selenium import webdriver

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 设置隐性等待
driver.implicitly_wait(300)
# 访问网址
driver.get("https://www.hao123.com/")

# 设置全屏显示
driver.maximize_window()
# 获得当前窗口句柄
current_handle = driver.current_window_handle
# 单击超链接
driver.find_element_by_link_text("hao123新闻").click()
# 所有窗口句柄，即列表类型
handles = driver.window_handles
# 切换到新窗口
driver.switch_to.window(handles[1])
driver.find_element_by_link_text("娱乐").click()


# 释放资源，退出浏览器
# driver.quit()






