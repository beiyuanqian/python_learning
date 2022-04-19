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
    'appPackage': 'app包名',
    'appActivity': 'app入口信息',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒
    'newCommandTimeout': 6000,
    # 设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName': 'UiAutomator2'  # 或者UiAutomator1
    # 跳过UiAutomator2的安装，如果是第一次安装，不要添加该配置项
    # 'skipServerInstallation': True
}

# 初始化driver对象-用于控制手机-启动被测应用
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 稳定元素

# 点击放大镜
# eles = driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')  # 先取所有符合条件的元素
# # 找到第二个元素--放大镜
# btn = eles[1]
# btn.click()
driver.find_element_by_xpath(
    "//*[@resource-id='com.hpbr.bosszhipin:id/ly_menu']/android.widget.RelativeLayout[2]/*").click()

# 搜索框输入职位信息
search_input = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')  # 输入参数

# 选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()

# 获取当前页面第一个职位信息
driver.find_element_by_id('com.hpbr.bosszhipin:id/boss_job_card_view').click()

# 获取地区、工作年限、学历
location = driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_required_location").text
work_exp = driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_required_work_exp").text
degree = driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_required_degree").text
print(f'地区:{location}|工作年限：{work_exp}|学历：{degree}')

# 演示xpath语法
# 根据id选择
job_name = driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/tv_job_name']").text
print(job_name)
driver.quit()
