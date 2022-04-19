from selenium import webdriver
from time import sleep
# 想要操作键盘，需要引入Keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
driver.get("http://www.baidu.com")
sleep(3)
inpEle = driver.find_element_by_id("kw")
# 先在文本框输入一个内容
inpEle.send_keys("selenium")
sleep(3)
# 全选输入框内容
inpEle.send_keys(Keys.CONTROL, "a")
sleep(3)
# 剪切文本
inpEle.send_keys(Keys.CONTROL, "x")
sleep(3)
# 粘贴文本
inpEle.send_keys(Keys.CONTROL, "v")
sleep(3)

"""
以下为常用的键盘操作：
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
send_keys(Keys.F1) 键盘 F1
send_keys(Keys.F12) 键盘 F12
"""

# 释放资源，退出浏览器
driver.quit()
