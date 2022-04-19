# author:刘小涵  time:2020/3/28
# WebDriver提供了Select类来处理下拉框

from selenium import webdriver
# webdriver提供了Select类处理下拉框
from selenium.webdriver.support.select import Select
from time import sleep

# 实例化一个浏览器对象
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get(r"D:\PYproject\python自动化\test\selenium\day4\下拉框.html")

# 不用下拉框
# 点击select标签
driver.find_element_by_id("abc").click()
sleep(3)
# 根据xpath选择元素
driver.find_element_by_xpath('//*[@id=\"abc\"]/option[3]').click()

# 定位到下拉框元素
ele = driver.find_element_by_id("abc")
sleep(3)

# 根据下标选择，下标从0开始
# Select(ele).select_by_index(1)
# 根据 value 属性选择
# Select(ele).select_by_value("3")
# 根据下拉框可视文本选择，即标签中间的值
Select(ele).select_by_visible_text("333")

# 取消选中，方法同上
# Select(ele).deselect_by_index()

# time.sleep(3)
# driver.quit()
