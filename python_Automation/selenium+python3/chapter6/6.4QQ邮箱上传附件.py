# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/15}

from selenium import webdriver
from time import sleep

# 创建浏览器驱动
driver = webdriver.Chrome(r"D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 设置元素等待
driver.implicitly_wait(10)
# 访问网址
driver.get("https://mail.qq.com/")
# 设置全屏显示
driver.maximize_window()
sleep(3)

"""
# 找到嵌套元素
iframe = driver.find_element_by_id("login_frame")
# 切入嵌套元素
driver.switch_to.frame(iframe)
"""
# 切入嵌套元素
driver.switch_to.frame("login_frame")
# 输入QQ号
driver.find_element_by_id("u").send_keys("1979345236")
# 输入密码
driver.find_element_by_id("p").send_keys("xcw01250")
# 点击登录
driver.find_element_by_id("login_button").click()
sleep(3)

# 点击写信
driver.find_element_by_id("composebtn").click()
sleep(3)
# 切入嵌套元素
driver.switch_to.frame("mainFrame")
sleep(3)
# 添加收件人
# 此处为坑，因为该框只有最前边的一丁点是input框，可以进行输入操作，随着输入内容增多，input框逐渐变大
# driver.find_element_by_id("toAreaCtrl").send_keys("1979345236@qq.com")  # 此为对div标签进行操作，故出错
driver.find_elements_by_class_name("js_input")[1].send_keys("1979345236@qq.com")
# 写主题
driver.find_element_by_css_selector('#subject').send_keys("附件")
# 上传附件
driver.find_element_by_name("UploadFile").send_keys("F:\Download\jmeter+Jenkins使用总结.docx")
# 发送
driver.find_element_by_name("sendbtn").click()
sleep(3)

driver.quit()



