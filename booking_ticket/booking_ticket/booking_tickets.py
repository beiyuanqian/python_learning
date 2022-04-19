# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/18}

from 携程定火车票.booking_ticket import class_name, xpath, return_driver, read_excel, log
from time import sleep
from 携程定火车票.booking_ticket import search_tickets

# 搜索火车票列表
# search_tickets("上海", "杭州", 1)
log("Read Excel Files to get test data.")
dic1 = read_excel("testdata.xlsx", 0)
log("Begin to search tickets")
search_tickets(dic1[0][0], dic1[0][1], 1)
log("End to search tickets")
log("Begin to get driver object.")
driver = return_driver()
sleep(3)

# 点击预定
log("Click book button:")
xpath("//div[starts-with(@id,\"trainListVue\")]/div[3]/div[1]/div[4]/div[4]/div[2]/div[1]/div[6]/div[1]/a").click()
sleep(3)
# 输入乘客姓名
log("input order information")
class_name("input-name").clear()
class_name("input-name").send_keys("小明")

sleep(5)
driver.quit()

