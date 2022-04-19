# author:刘小涵  time:2020/3/25

from selenium import webdriver
import time

'''
访问：https://m.weibo.cn
点击：大家都在搜
点击：微博热搜榜
找到：实时热点，每分钟更新一次
将其中带有热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种
'''

# 创建浏览器驱动
driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# 访问网址
driver.get("https://m.weibo.cn")

# 找到大家都在搜 m-search
driver.find_element_by_class_name("m-search").click()
time.sleep(3)
# 找到热搜榜所在大标签 card m-panel card16 m-col-2，class如果有空格，就用.替代card，m-panel，card16，m-col-2，或者取开头、结尾的单词
hotSearchEle = driver.find_element_by_class_name("m-col-2")
# 在大标签中匹配热搜列表 m-item-box
hotSearchSli = hotSearchEle.find_elements_by_class_name("m-item-box")
# 取列表的最后一个元素,即微博热搜榜,并点击
hotSearchSli[-1].click()
time.sleep(3)
# 找到 实时热点，每分钟更新一次
hotSli = driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div")
# 从 hotSli 中找到 card m-panel card4 标签列表, 即每一行热搜标签
hotDivSli = hotSli.find_elements_by_class_name("card4")
# 迭代 hotSli 中的每一个 div 标签  # 注: 第一个置顶的热搜不是每分钟更新一次, 每次刷新都可能不一样
for hotDiv in hotDivSli:
    # 判断这一行热搜有没有图片标签
    iconSli = hotDiv.find_elements_by_class_name("m-link-icon")
    if iconSli:  # 如果有图片标签
        # 获取 img 标签
        img = iconSli[0].find_element_by_tag_name("img")
        # 获取 src 属性
        srcLink = img.get_attribute("src")
        # 判断类型是 hot 还是 new 还是 fei
        if "hot" in srcLink:
            hotType = "热"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_class_name("m-text-cut").text
            print("{}: {}".format(hotType, hotText))
        elif "new" in srcLink:
            hotType = "新"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_class_name("m-text-cut").text
            print("{}: {}".format(hotType, hotText))
        elif "fei" in srcLink:
            hotType = "沸"
            # 获取热搜文本
            hotText = hotDiv.find_element_by_class_name("m-text-cut").text
            print("{}: {}".format(hotType, hotText))

time.sleep(5)
# 释放资源
driver.quit()
