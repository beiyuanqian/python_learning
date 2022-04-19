# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/12/30}

from selenium import webdriver
from time import sleep

# 创建浏览器驱动
driver = webdriver.Chrome(r"D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("https://gtsc.gree.com/#/index")
# 设置全屏显示
driver.maximize_window()
sleep(2)
# 找到用户名输入框
name = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div/input")
# 输入用户名
name.send_keys("1001")
# 找到密码输入框
password = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[4]/div/div/input")
# 输入密码
password.send_keys("123456")
# 找到登录按钮
login = driver.find_element_by_css_selector(
    "body > div > div.view-middle > form > div.el-form-item.enterprise-footer-btn > div > button")
# 点击登录
login.click()
sleep(2)

# # 输出首页消息内容
# for i in range(1, 6):
#     # 输出消息类型
#     info_type = driver.find_element_by_css_selector("#tab-" + str(i))
#     print(info_type.text)
#     info_type.click()
#     sleep(2)
#     # 输出消息标题
#     tagsElement = driver.find_elements_by_tag_name("tr")
#     for tagElement in tagsElement:
#         # print(tagElement.text)
#         info_title = tagElement.find_element_by_tag_name("td")
#         print(info_title.text)

# # 点击菜单项目管理
# for memu_1 in driver.find_elements_by_tag_name("li"):
#     if memu_1.text=="项目管理":
#         memu_1.click()

# 找到项目管理
for i in range(1, 7):
    try:
        menus = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/ul/li[' + str(i) + "]")
        # print(menus.text)
        if menus.text == "项目管理":
            menus.click()
            # 找到我的申请
            for j in range(1, 8):
                try:
                    sleep(1)
                    menu = menus.find_element_by_xpath(
                        '//*[@id="app"]/div[2]/div[2]/ul/li[' + str(i) + ']/ul/li[' + str(j) + "]")
                    # print(menu.text)
                    if menu.text == "我的申请":
                        menu.click()
                        # 切换到我的申请页面
                        windows = driver.window_handles
                        # 此处一定留时间以便driver切换成功
                        sleep(1)
                        driver.switch_to.window(windows[-1])
                        # # 输出表格标题
                        # print(driver.find_element_by_tag_name("tr").text)
                        sleep(3)
                        print(len(driver.find_elements_by_xpath(
                            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li')))
                        # 依次输出每页内容
                        for l in range(1, len(driver.find_elements_by_xpath(
                                '//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li')) + 1):
                            print("第" + str(l) + "页")
                            driver.find_element_by_xpath(
                                '//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li[' + str(
                                    l) + ']').click()
                            # 输出申请标题
                            for k in range(1, 11):
                                try:
                                    sleep(3)
                                    tiltle = '//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[' + str(
                                        k) + ']/td[1]'
                                    print(driver.find_element_by_xpath(tiltle).text)
                                except:
                                    pass
                except:
                    pass
    except:
        pass

sleep(5)
# 释放资源，退出浏览器
driver.quit()
