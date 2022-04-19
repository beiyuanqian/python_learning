# auto:刘小涵 time:2020-03-26
# 访问 https://www.toutiao.com/

from selenium import webdriver
from time import sleep
# 如果需要鼠标操作，必须引入ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# 创建浏览器驱动
driver = webdriver.Chrome("D:\python37\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("https://www.toutiao.com/")
sleep(3)

# 定位到需要悬停的对象
setting_text = driver.find_element_by_link_text("更多")
# 对定位的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(setting_text).perform()
sleep(3)
# 找到黑框所在大标签
listEle = driver.find_element_by_css_selector(
    'body > div > div.bui-box.container > div.bui-left.index-channel > div > div')
sleep(3)
# 在大标签中匹配列表，find_elements返回列表
listEle_1 = listEle.find_elements_by_tag_name("span")
for Ele in listEle_1:
    print(Ele.text)

sleep(5)
driver.quit()
