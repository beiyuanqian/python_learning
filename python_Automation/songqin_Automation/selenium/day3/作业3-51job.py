# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/12}

"""
登录 51job ，http://www.51job.com
输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉），
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
"""

from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("https://www.51job.com")

# 设置全屏显示
driver.maximize_window()
# 输入搜索关键字python
driver.find_element_by_id("kwdselectid").send_keys("python")
# 点击地区按钮
driver.find_element_by_id("work_position_input").click()
# 地区选杭州，将其他城市取消选择
# 找到已选择地区的展示控件
addEle = driver.find_element_by_id("work_position_click_multiple_selected")
# 在addEle匹配列表span，挨个点掉,只有一个，直接点掉第一个
addEle.find_elements_by_tag_name("span")[0].click()
time.sleep(3)
# 找到杭州并点击
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
# 点击确定按钮
driver.find_element_by_id("work_position_click_bottom_save").click()
time.sleep(3)
# 点击搜索按钮
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()
time.sleep(3)


for i in range(1,10):
    print("=" * 10, "这是第{}页".format(i), "=" * 10)
    # 获取职位列表
    jobSli = driver.find_element_by_id("resultList")
    jobEleSli = jobSli.find_elements_by_class_name("el")
    time.sleep(3)
    for job in jobEleSli:
        # 去掉第一行——标题行
        if "title" in job.get_attribute("class"):
            continue
        # 在一行去寻找需要的文本——寻找span标签
        infoSli = job.find_elements_by_tag_name("span")
        for i in infoSli:
            print(i.text, end=" | ")
        print()
driver.quit()
