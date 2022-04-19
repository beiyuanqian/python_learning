# author:刘小涵  time:2020/3/27

"""
大多数Web应用程序都是使用Ajax和Javascript开发的。当浏览器加载页面时，我们想要与之交互的元素可能尚未被加载出来。
此刻不仅难以识别元素，而且很容易定位不到元素，抛出异常。使用Waits，我们可以解决此问题
WebDriver提供了两种类型的等待：显式等待和隐式等待
显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
WebDriver提供了driver.implicitly_wait(10)
方法来实现隐式等待，默认参数的单位为秒，本例中设置等待时长为10秒。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到.
假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常
"""

from selenium import webdriver
# from time import sleep

# 显式等待时引入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
driver.get("https://m.weibo.cn/")

"""
# 设置隐式等待
# 一次设置，全局生效
# 在元素定位的时候，如果找不到元素，就去轮询检查（每0.5秒检查一次），知道元素出现
# 元素出现以后，就不再等，如果元素超时未出现，就报错
driver.implicitly_wait(10)

# 点击大家都在搜
driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div").click()
# 点击微博热搜榜
driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4").click()
"""

# 显式等待
# 使webdriver等待元素出现，如果元素出现，就不再等了，继续执行后边的代码，达到超时时间就会报错，只在引用的地方生效
# 点击大家都在搜
driver.find_element_by_css_selector(
    "#app > div.main-wrap > div.lite-topbar.main-top > div.nav-top > a > aside > label > div").click()
# 显式等待微博热搜榜
# 设置元素等待的配置最多等5秒，轮询时间为0.5秒
element = WebDriverWait(driver, 5, 0.5).until(
    # 条件：直到元素加载完成
    EC.presence_of_element_located(
        # 设定元素寻找方案，并传入表达式，写定位元素的方法
        (By.CSS_SELECTOR,
         "#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div > div > h4")
    )
)
element.click()


# # 显示等待封装为函数
# def foo(driver, outTime, lTime, byEle, eleName):
#     """
#     封装了一个线性等待的函数
#     :param driver: 浏览器对象
#     :param outTime: 超时时间
#     :param lTime: 轮询时间
#     :param byEle: 元素定位方案
#     :param eleName: 元素定位表达式
#     :return: 元素对象
#     """
#     element = WebDriverWait(driver, outTime, lTime, ).until(
#         EC.presence_of_element_located(
#             (byEle, eleName)
#         )
#     )
#     return element

#
# foo(driver="xxx", outTime=10, lTime=1, byEle=By.ID, eleName="kw")

# 每隔 0.5s 检查一次(默认就是 0.5s), 最多等待 5 秒
# element = WebDriverWait(driver, 5, 0.5).until(
#     EC.presence_of_element_located(
#         (By.ID, "kw")
#     )
# )
# element.send_keys('selenium')

driver.quit()
