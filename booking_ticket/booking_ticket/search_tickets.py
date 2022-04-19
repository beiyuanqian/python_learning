# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/18}

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from 携程定火车票.booking_ticket import date_n, id, class_name, js, return_driver,open_base_site

def search_tickets(departure_city, arrival_city, n):
    driver = return_driver()

    open_base_site("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
    driver.maximize_window()

    # departure_city = departure_city
    # arrival_city = arrival_city
    # departure_time = date_n(n)

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
    id("departDate").send_keys(date_n(n))
    sleep(3)
    # 单击页面空白处，以免挡住搜索框
    ActionChains(driver).move_by_offset(0, 0).click().perform()
    sleep(3)
    # 点击搜索
    class_name('searchbtn').click()



