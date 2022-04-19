# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/18}

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from booking_ticket.functions import date_n, id, class_name, xpath, js, return_driver, open_base_site

# 创建浏览器驱动
driver = return_driver()
# 访问网址
open_base_site("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
driver.maximize_window()
sleep(3)

departure_city = "上海"  # 出发城市
arrival_city = "杭州"  # 到达城市
departure_time = date_n(1)  # 出发时间

# 输入出发城市
id("departCityName").clear()
id("departCityName").send_keys(departure_city)
sleep(3)
# 输入到达城市
id("arriveCityName").clear()
id("arriveCityName").send_keys(arrival_city)
sleep(3)
# 移除出发时间的readonly属性
js('departDate')
# 选择出发时间
id("departDate").clear()
id("departDate").send_keys(departure_time)
sleep(3)
# 单击页面空白处，以免挡住搜索框
ActionChains(driver).move_by_offset(0, 0).click().perform()
sleep(3)
# 点击搜索
class_name('searchbtn').click()
sleep(3)
# 点击预定
xpath("//div[starts-with(@id,\"trainListVue\")]/div[3]/div[1]/div[4]/div[4]/div[2]/div[1]/div[6]/div[1]/a").click()
sleep(3)
# 输入乘客姓名
class_name("input-name").clear()
class_name("input-name").send_keys("小明")
