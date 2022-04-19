# 导包
from appium import webdriver
import time

# 准备自动化配置信息
desired_caps = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号
    'plathformVersion': '6',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息
    'appPackage': 'com.alpha.lagouapk',
    'appActivity': '.HelloActivity',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒
    'newCommandTimeout': 6000,
    # 更换底层驱动
    'automationName': 'UiAutomator2',
    # 修改手机的输入法,如果指定UI2作为驱动，则不需要配置
    # 'unicodeKeyboard': True,
    # 自动化结束之后输入法欢迎
    # 'resetKeyboard': True
}

# 初始化driver对象-用于控制手机
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 稳定元素
time.sleep(15)

# 根据屏幕尺寸计算相对坐标
win_size = driver.get_window_size()
print(win_size)
width = win_size['width']
height = win_size['height']
x = width / 2
y = height / 16
print(x, y)
driver.tap([(x, y)])
# # 点击弹出搜索框，跟据坐标点击元素
# driver.tap([(997, 148)])
time.sleep(15)

driver.quit()
