# 导包
from appium import webdriver
import time

# 准备自动化配置信息
desired_caps = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号,写整数位即可
    'plathformVersion': '9',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息
    'appPackage': 'com.hpbr.bosszhipin',
    'appActivity': '.module.launcher.WelcomeActivity',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒
    'newCommandTimeout': 6000,
    # 设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    # 'automationName': 'UiAutomator2'  # 或者UiAutomator1
    # 跳过UiAutomator2的安装，如果是第一次安装，不要添加该配置项
    'skipServerInstallation': True
}

# 初始化driver对象-用于控制手机-启动被测应用
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 稳定元素

time.sleep(10)
# # 滑动swipe方法
# driver.swipe(500, 1700, 500, 700)
# 取屏幕中心
w_size = driver.get_window_size()
w_width = w_size['width']
w_height = w_size['height']
start_x = w_width / 2
start_y = w_height / 2

# 滑动距离-一个格子的距离
box = driver.find_element_by_id("com.hpbr.bosszhipin:id/boss_job_card_view")
distance = box.size["height"]

# 防止滑动的间隔时间过长
driver.implicitly_wait(1)
# 滑动到指定的页面-自动化测试
while 1:
    driver.swipe(start_x, start_y, start_x, start_y - distance)
    # 找到元素就停止滑动
    eles = driver.find_elements_by_android_uiautomator('new UiSelector().text("功能测试")')
    if eles:
        print("找到目标元素")
        break
driver.implicitly_wait(10)

time.sleep(10)
driver.quit()
