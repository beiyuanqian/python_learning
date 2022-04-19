# author:刘小涵  time:2020/3/27

"""
在页面操作过程中有时候点击某个链接会弹出新的窗口，这时就需要切换到新打开的窗口上进行操作。WebDriver提供了以下方法
current_window_handle：获得当前标签页句柄
window_handles：返回所有便签页的句柄
switch_to.window(标签页句柄)：切换到对应的标签页
关闭标签页使用 close 方法
"""
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("http://www.baidu.com")

"""
# 直接用该方法会出错
# 点击抗击肺炎
driver.find_element_by_link_text("抗击肺炎").click()
print(driver.title)
# 点击国外疫情
driver.find_element_by_css_selector("#tab > div > a:nth-child(2)").click()
"""

# 点击抗击肺炎
driver.find_element_by_link_text("抗击肺炎").click()
# 获得当前标签页的句柄，即操作系统当中的一个唯一资源标识符
print("百度页面的句柄", driver.current_window_handle)
# 返回所有标签页的句柄
handles = driver.window_handles
print(handles)
print("一共有多少句柄", len(handles))

# # 确定对应的下标时，直接切换到对应标签页
# driver.switch_to.window(handles[1])
# 使用for循环切换到对应标签页
for i in handles:
    # 切换到对应的标签页
    driver.switch_to.window(i)

    if "实时更新" in driver.title:
        break

print(driver.title)
# 点击国外疫情
driver.find_element_by_css_selector("#tab > div > a:nth-child(2)").click()

# # 找到搜索按钮
# input_element = driver.find_element_by_id("kw")
# # 输入搜索内容
# input_element.send_keys("松勤\n")
#
# # 点击松勤教育官网
# driver.find_element_by_css_selector("#\34  > h3 > a > em").click()
#
# # 获得当前所有打开的窗口的句柄
# all_handles = driver.window_handles
#
# for handle in all_handles:
#     driver.switch_to.window(handle)
#     print(driver.title)

# 退出浏览器
# driver.quit()
