# author:刘小涵  time:2020/3/28

"""
在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，具体做法是使用 switch_to.alert 方法定位
到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作
text：返回 alert/confirm/prompt 中的文字信息
accept()：接受现有警告框
dismiss()：取消现有警告框
send_keys(“haha”)：发送文本至警告框
"""

from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("D:\PYproject\python自动化\\test\selenium\day4\警告框.html")
driver.implicitly_wait(5)

# # 触发对话框
# driver.find_element_by_id("bu1").click()
# 找到对话框对象
# al = driver.switch_to.alert
# time.sleep(3)
# 确认对话框
# al.accept()


# # 触发确认框
# driver.find_element_by_id("bu2").click()
# 获取确认框对象
# al = driver.switch_to.alert
# 确认对话框
# al.accept()
# 触发确认框
# driver.find_element_by_id("bu2").click()
# 取消对话框
# al.dismiss()


# 触发提示框
driver.find_element_by_id("bu3").click()
# 获取提示框对象
al = driver.switch_to.alert
# 将文本发送到提示框里
al.send_keys("口罩太贵了")
# 确认对话框
al.accept()

time.sleep(3)
driver.quit()
