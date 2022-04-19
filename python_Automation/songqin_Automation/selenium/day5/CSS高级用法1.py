# author:刘小涵  time:2020/4/1

"""
css主要是对象匹配，优先选择
xpath主要是遍历
"""

"""
# 打印基于随机数
import uuid
print(uuid.uuid4())
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
driver.get('D:\PYproject\python自动化\\test\selenium\day5\cssStu.html')

print(driver.find_element_by_css_selector("#abc").text)

driver.quit()
