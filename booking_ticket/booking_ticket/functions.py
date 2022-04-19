# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/5/18}

from selenium import webdriver
from datetime import date, timedelta
import xlrd
import logging

# 以下为driver设置和打开携程火车票网站
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")

# 返回driver对象
def return_driver():
    return driver

# 打开携程网火车票首页
def open_base_site(url):
    driver.get(url)

# 返回今天后的第n天日期
def date_n(n):
    return str((date.today() + timedelta(days=+ int(n))).strftime("%Y-%m-%d"))

# 函数id将返回按照id属性来定位元素的语句
def id(element):
    return driver.find_element_by_id(element)

# 函数class_name将返回按照class属性来定位元素的语句
def class_name(element):
    return driver.find_element_by_class_name(element)

# 函数css将返回按照css selector方式来定位元素的语句
def css(element):
    return driver.find_element_by_css_selector(element)

# 函数xpath将返回按照xpath方式来定位元素的语句
def xpath(element):
    return driver.find_element_by_xpath(element)

# 函数js通过Selenium来执行JavaScript语句
def js(element):
    driver.execute_script("document.getElementById("+"'"+element+"'"+").removeAttribute('readonly')")

# 用于处理和获取Excel文件中的测试数据
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data
    return dic

# 定义一个log函数
def log(str):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                        datefmt='%a,%d %b %Y %H:%M:%S',
                        filename='log-selenium.log',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)





