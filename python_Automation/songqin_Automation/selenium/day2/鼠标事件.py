from selenium import webdriver
from time import sleep
# 如果需要鼠标操作，必须引入ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
driver.get("http://www.baidu.com")
sleep(5)
# 设置全屏显示
driver.maximize_window()
sleep(5)
# 定位到需要悬停的对象
setting_text = driver.find_element_by_link_text("设置")
sleep(5)
# 对定位的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(setting_text).perform()
sleep(3)
# 点击搜索设置
driver.find_element_by_class_name("setpref").click()

"""
ActionChains 类提供了鼠标操作的常用方法：
perform()： 执行操作
context_click()： 右击；
double_click()： 双击；
drag_and_drop()： 拖动；
move_to_element()： 鼠标悬停。

# 将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
# 将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
# 将页面滚动条移动到页面任意位置，改变等于号后的数值即可
js="var q=document.documentElement.scrollTop=50"
driver.execute_script(js)
"""

sleep(5)
# 释放资源，退出浏览器
driver.quit()
