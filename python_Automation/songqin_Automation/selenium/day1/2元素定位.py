# author:刘小涵  time:2020/3/24
from selenium import webdriver
import time

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get(r"D:\PYproject\python自动化\test\selenium\day1\test1.html")
'''
# 元素定位的第一种方式：根据id属性,有id且id不是随机字符串，首选id
uName=driver.find_element_by_id("username")
uName.send_keys("张三")
pwd=driver.find_element_by_id("password")
pwd.send_keys("123")
'''
'''
# 元素定位的第二种方式：根据class属性
inpElement = driver.find_element_by_class_name("username")
inpElement.send_keys("李四")
butElement = driver.find_element_by_class_name("login")
butElement.click()
'''
'''
# 元素定位的第三种方式：根据name属性定位
driver.find_element_by_name("pwd").send_keys("123")
'''
'''
# 元素定位的第四种方式：根据标签定位,如果有多个P标签，会找到第一个，如果这个标签里有很多元素和值，就全部取出来
tagElement = driver.find_element_by_tag_name("p")
# 获取元素的文本值,标签中间的值
print(tagElement.text)
'''
'''
# 元素定位的第五种方式：链接文本
driver.find_element_by_link_text("抗击肺炎").click()
'''
"""
# 元素定位的第六种方式：链接文本--支持模糊搜索
driver.find_element_by_partial_link_text("击肺").click()
"""
"""
# 元素定位的第七种方式：根据xpath，万能
# liElement=driver.find_element_by_xpath("/html/body/div/ul[2]/li[3]")
print(liElement.text)
"""
"""
# 元素定位的第八种方式，根据 css 选择器定位，万能
liEle = driver.find_element_by_css_selector("body > div > ul:nth-child(1) > li:nth-child(1)")
print(liEle.text)
"""

time.sleep(5)
# 释放资源
driver.quit()
