from selenium import webdriver
from time import sleep

# 创建浏览器对象
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("https://www.baidu.com")
"""
# 1、控制浏览器大小
# 设置全屏显示
driver.maximize_window()
# 设置最小化浏览器
driver.minimize_window()
# 2、自定义窗口大小
print("设置浏览器宽900，高900显示，参数为像素点")
driver.set_window_size(900, 900)
sleep(5)
"""
"""
# 2、控制浏览器前进、后退、刷新
driver.get("https://news.baidu.com")
# 后退操作
driver.back()
sleep(5)
# 前进操作
driver.forward()
sleep(5)
# 刷新操作
driver.refresh()
sleep(5)
"""
"""
# 获得元素的尺寸
size = driver.find_element_by_id("kw").size
print("元素尺寸:", size)
# 获取元素文本值,此时浏览器换为http://m.weibo.cn
text = driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-main > div > div.m-box-col.inner-box > div > div > ul > li:nth-child(2) > span").text
print(text)
"""
"""
# submit()方法用于提交表单。 例如， 在搜索框输入关键字之后的“回车” 操作， 就可以通过该方法模拟
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
"""
"""
# 获取元素属性
print(driver.find_element_by_id("kw").get_attribute("name"))
# 获取元素的结果是否可见，返回结果为True或False
print(driver.find_element_by_id("kw").is_displayed())
"""

"""
# 如果遇到iframe之类，先切到相应区域再滚动，内嵌网页也没认为是整个浏览器
# 页面向下滚动100个像素点
driver.execute_script("window.scrollBy(0,100)")
# 页面向上滚动100个像素点
driver.execute_script("window.scrollBy(0,-100)")
# 页面向右滚动100个像素点
driver.execute_script("window.scrollBy(100,0)")
# 页面向左滚动100个像素点
driver.execute_script("window.scrollBy(-100,0)")

# 对于内嵌元素的滚动条
driver.execute_script("document.getElementsByClassName(\"scoll\")[0].scrollLeft=-100")
"""
# 释放资源，退出浏览器
driver.quit()
