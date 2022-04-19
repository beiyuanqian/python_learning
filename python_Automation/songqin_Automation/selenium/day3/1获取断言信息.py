# author:刘小涵  time:2020/3/27

"""
不管是在做功能测试还是自动化测试，最后一步需要拿实际结果与预期进行比较。这个比较称之为断言。
我们通常可以通过获取title 、URL和text等信息进行断言
title：用于获得当前页面的标题
current_url：用户获得当前页面的URL
text：获取标签对之间的文本信息
"""

from selenium import webdriver

driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
driver.get("http://www.baidu.com")
"""
# 获取当前页面的标题
print(driver.title)
driver.get("https://www.toutiao.com/")
print(driver.title)
"""
"""
#获取当前页面的url
print(driver.current_url)
driver.get("https://www.toutiao.com/")
print(driver.current_url)
"""
"""
#获取标签对之间的文本信息
link = driver.find_element_by_link_text("抗击肺炎")
print(link.text)
if "抗击肺炎"==link.text:
    print("断言通过")
"""

driver.quit()
