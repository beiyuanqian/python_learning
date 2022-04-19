# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/11}

from selenium import webdriver
from time import sleep
# 如果需要鼠标操作，必须引入ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# 创建浏览器驱动
driver = webdriver.Chrome(r"D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("http://120.198.219.9:8082")
# 设置全屏显示
driver.maximize_window()
sleep(3)
# 找到用户名输入框
inputElement = driver.find_element_by_name("userEmailNum")
# 对用户名输入框输入用户名
inputElement.send_keys("admin")
sleep(3)
# 找到密码输入框
inputElement = driver.find_element_by_name("password")
# 对密码输入框输入密码
inputElement.send_keys("gree2602369")
sleep(3)
# 元素定位，找到登录按钮
searchElement = driver.find_element_by_css_selector("#app > div > form > button")
# 点击登录按钮
searchElement.click()
sleep(3)
# 刷新页面，提示框消失
# 刷新操作
driver.refresh()
sleep(3)
# 点击数据查询
driver.find_element_by_link_text("数据查询").click()
sleep(3)
# 找到物料编码
number = driver.find_element_by_css_selector(
    '#app > div > div.main-container.hasTagsView > div.app-main > div.data-query.app-container > div.el-card.is-always-shadow > div > span > form > div > div:nth-child(2) > span > div > div.el-form-item__content > div > div.el-input.el-input--mini.el-input--suffix > input')
# 输入物料编码
number.send_keys('number001')
# 找到批次编号
batch = driver.find_element_by_css_selector(
    '#app > div > div.main-container.hasTagsView > div.app-main > div.data-query.app-container > div.el-card.is-always-shadow > div > span > form > div > div:nth-child(6) > span > div > div.el-form-item__content > div > input')
# 输入批次编号
batch.send_keys('2')
# 找到日期
date = driver.find_element_by_css_selector(
    '#app > div > div.main-container.hasTagsView > div.app-main > div.data-query.app-container > div.el-card.is-always-shadow > div > span > form > div > div.el-col.el-col-24.el-col-sm-12.el-col-md-16.el-col-lg-6 > span > div > div.el-form-item__content > div')
date.click()
# 定位到需要悬停的对象(此处需注意)
setting_text = driver.find_element_by_css_selector(
    '#app > div > div.main-container.hasTagsView > div.app-main > div.data-query.app-container > div.el-card.is-always-shadow > div > span > form > div > div.el-col.el-col-24.el-col-sm-12.el-col-md-16.el-col-lg-6 > span > div > div.el-form-item__content > div')
# 对定位的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(setting_text).perform()
# 找到日期输入框
driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time')
# 输入开始日期
startdate = driver.find_element_by_css_selector(
    'body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(1) > div > input')
startdate.clear()
startdate.send_keys('2020-04-15')
sleep(3)
# 输入开始时间
starttime = driver.find_element_by_css_selector(
    'body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-date-range-picker__editor.el-input.el-input--small > input')
starttime.clear()
starttime.click()
starttime.send_keys('00:00:00')
sleep(3)
# # 定位到需要悬停的对象(此处需注意)
# setting_text = driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-date-range-picker__editor.el-input.el-input--small > input')
# # 对定位的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(setting_text).perform()
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content.has-seconds > div > div:nth-child(1) > div.el-scrollbar__wrap > ul > li:nth-child(1)').click()
# sleep(2)
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content.has-seconds > div > div:nth-child(2) > div.el-scrollbar__wrap > ul > li:nth-child(1)').click()
# sleep(2)
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content.has-seconds > div > div:nth-child(3) > div.el-scrollbar__wrap > ul > li:nth-child(1)').click()
# sleep(2)
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm').click()
# sleep(3)
# 输入结束日期
overdate = driver.find_element_by_css_selector(
    'body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span.el-date-range-picker__editors-wrap.is-right > span:nth-child(1) > div > input')
overdate.clear()
overdate.send_keys('2020-04-15')
sleep(3)
# 输入结束时间
overtime = driver.find_element_by_css_selector(
    'body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span.el-date-range-picker__editors-wrap.is-right > span:nth-child(2) > div.el-date-range-picker__editor.el-input.el-input--small > input')
overtime.clear()
overtime.click()
overtime.send_keys("23:59:59")
sleep(3)
# # 定位到需要悬停的对象(此处需注意)
# setting_text = driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span.el-date-range-picker__editors-wrap.is-right > span:nth-child(2) > div.el-date-range-picker__editor.el-input.el-input--small > input')
# # 对定位的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(setting_text).perform()
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span.el-date-range-picker__editors-wrap.is-right > span:nth-child(1) > div > input').click()
# sleep(2)
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content.has-seconds > div > div:nth-child(2) > div.el-scrollbar__wrap > ul > li:nth-child(1)').click()
# sleep(2)
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__content.has-seconds > div > div:nth-child(3) > div.el-scrollbar__wrap > ul > li:nth-child(1)').click()
# sleep(2)
# driver.find_element_by_css_selector('body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__body-wrapper > div > div.el-date-range-picker__time-header > span:nth-child(1) > span:nth-child(2) > div.el-time-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm').click()
# sleep(3)
driver.find_element_by_css_selector(
    'body > div.el-picker-panel.el-date-range-picker.el-popper.has-time > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain').click()
sleep(5)

# 释放资源，退出浏览器
driver.quit()
