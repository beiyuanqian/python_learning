# author:刘小涵  time:2020/4/6

"""
打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init
出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’
发车时间 选 06:00--12:00
发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息，结果如下：
G7641
G1505
G7393
G7689
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

# 设置全屏显示
driver.maximize_window()
# 找到出发城市
ele_startCity = driver.find_element_by_css_selector('#fromStationText')
ele_startCity.click()
ele_startCity.send_keys("南京南\n")
sleep(2)
# 找到目的地城市
ele_destination = driver.find_element_by_css_selector('#toStationText')
ele_destination.click()
ele_destination.send_keys("杭州东\n")
sleep(2)
# 找到发车时间
driver.find_element_by_css_selector('#cc_start_time').click()
driver.find_element_by_xpath('//*[@id="cc_start_time"]/option[3]').click()
sleep(2)
# 找到发车日期
