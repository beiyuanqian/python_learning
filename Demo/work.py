# coding=utf-8

# author:刘小涵  time:2020/3/26

from selenium import webdriver
from time import sleep

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
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
# 点击权限管理
driver.find_element_by_link_text("权限管理").click()
sleep(3)
# 点击组织与人员
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li[2]').click()
sleep(3)
# 点击家用空调技术-科室
driver.find_element_by_xpath('//div[text()="家用空调技术 - 科室"]').click()
sleep(3)

# 设置循环
userEmail = ['260349', '260375']
for i in range(len(userEmail)):
    # 点击新增人员
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/button').click()
    sleep(3)
    # 找到输入人员名称框
    inpName = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/input')
    # 输入人员名称
    inpName.send_keys(userEmail[i])
    sleep(3)
    # 选择物料权限
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/div/input').click()
    # 选择全部物料权限
    driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper")
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[2]").click()
    sleep(3)
    # 选择角色
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/div[2]/form/div[9]/div/div/div[2]/input').click()
    sleep(3)
    # 选择主任
    driver.find_element_by_xpath('/html/body/div[5]/div[1]')
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[3]').click()
    sleep(3)
    # 点击空白
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/div[2]/form').click()
    sleep(3)
    # 点击确定
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/div[3]/div/button[2]').click()
    sleep(3)

# 释放资源，退出浏览器
driver.quit()
