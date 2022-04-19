# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/18}

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from datetime import date, timedelta
# 定义函数，返回今天后的第n天日期
def date_n(n):
    return str((date.today() + timedelta(days=+ int(n))).strftime("%Y-%m-%d"))

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
driver.maximize_window()
sleep(3)

departure_city = "上海"  # 出发城市
arrival_city = "杭州"  # 到达城市
departure_time = date_n(1)  # 出发时间

# 输入出发城市
Departure_city = driver.find_element_by_id("departCityName")
Departure_city.clear()
Departure_city.send_keys(departure_city)
sleep(3)
# 输入到达城市
Arrival_city = driver.find_element_by_id("arriveCityName")
Arrival_city.clear()
Arrival_city.send_keys(arrival_city)
sleep(3)
# 出发时间的选择有两种：
"""
# 1、直接输入日期
# 移除出发时间的readonly属性
driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
# 选择出发时间
Departure_time = driver.find_element_by_id("departDate")
Departure_time.clear()
Departure_time.send_keys("2020-05-20")
sleep(3)
"""
# 2、时间选择为今天后的第几天
# 移除出发时间的readonly属性
driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
# 选择出发时间
Departure_time = driver.find_element_by_id("departDate")
Departure_time.clear()
Departure_time.send_keys(departure_time)
sleep(3)
# 单击页面空白处，以免挡住搜索框
ActionChains(driver).move_by_offset(0, 0).click().perform()
sleep(3)
# 点击搜索
driver.find_element_by_class_name('searchbtn').click()
sleep(3)
# 点击预定
driver.find_element_by_css_selector("#trainListVue > div:nth-child(3) > div > div.lisBox > div.List-Box > div.List-Wrap > div:nth-child(1) > div.w6 > div:nth-child(1) > a").click()
sleep(3)
# 输入乘客姓名
Name = driver.find_element_by_class_name("input-name")
Name.clear()
Name.send_keys("小明")






