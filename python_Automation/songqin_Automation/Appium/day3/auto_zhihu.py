# 导包
from appium import webdriver

# 准备自动化配置信息
desired_caps = {
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号,写整数位即可
    'plathformVersion': '9',
    # 设备的名称--值可以随便写
    'deviceName': 'test0106',
    # 提供被测app的信息-包名，入口信息
    'appPackage': 'com.hpbr.zhihu',
    'appActivity': '知乎',
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

# 通过id选择元素，uiautomatorapi方式
code = "new UiSelector().resourceId('com.zhihu.android:id/text')"
ele = driver.find_element_by_android_uiautomator(code)
print(ele.text)
ele.click()

driver.quit()
