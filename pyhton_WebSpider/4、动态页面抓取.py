# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/3/26}
import csv
# 爬取到的文章第一页的评论
import requests
import json

link = """https://api-zero.livere.com/v1/comments/list?callback=jQuery1124010509076029820341_1616745380517&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1616745380519"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
r = requests.get(link, headers=headers)
# 爬取出来的动态网页的信息
print(r.text)
json_string = r.text
# 从第一个‘}’开始提取，最后的两个字符‘}’和‘，’不取
json_string = json_string[json_string.find('{'):-2]
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']
for eachone in comment_list:
    message = eachone['content']
    print(message)

# # 爬取到的文章多页的评论
# import requests
# import json
#
#
# def single_page_comment(link):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
#     r = requests.get(link, headers=headers)
#     # 获取json的string
#     json_string = r.text
#     # 从第一个‘}’开始提取，最后的两个字符‘}’和‘，’不取
#     json_string = json_string[json_string.find('{'):-2]
#     json_data = json.loads(json_string)
#     comment_list = json_data['results']['parents']
#     for eachone in comment_list:
#         message = eachone['content']
#         print(message)
#
#
# for page in range(1, 4):
#     link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery1124010509076029820341_1616745380517&limit=10&offset="
#     link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1616745380523"
#     page_str = str(page)
#     link = link1 + page_str + link2
#     print(link)
#     single_page_comment(link)

# # 通过selenium模拟浏览器抓取
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome("D:\Program Files\Python38\Lib\site-packages\selenium\chromedriver.exe")
# driver.get('http://www.santostang.com/2018/07/04/hello-world/')
# sleep(5)
# # # 查找页面第一条评论
# # iframe = driver.find_element_by_css_selector("iframe[title='livere-comment']")
# # driver.switch_to.frame(iframe)
# # comment = driver.find_elements_by_css_selector('#list > div:nth-child(1) > div.reply-bottom > div.reply-content-wrapper > div.reply-content')
# # content = driver.find_element_by_tag_name('p')
# # print(content.text)
#
# # 查找页面全部评论
# iframe = driver.find_element_by_css_selector("iframe[title='livere-comment']")
# driver.switch_to.frame(iframe)
# sleep(2)
# comments=driver.find_elements_by_id('list')
# for comment in comments:
#     comment = comment.find_element_by_class_name('reply-wrapper')
#     content = driver.find_element_by_tag_name('p')
#     print(content.text)

# for i in range(1,3):
#     #下滑到页面底部
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(2)
#     # 转换iframe，再找到查看更多，点击
#     iframe = driver.find_element_by_css_selector("iframe[title='livere-comment']")
#     driver.switch_to.frame(iframe)
#     load_more=driver.find_element_by_css_selector('#list > div.more-wrapper > button:nth-child('+str(i)+')')
#     load_more.click()
#     sleep(3)
#     comments = driver.find_elements_by_css_selector(
#         '#list > div:nth-child(1) > div.reply-bottom > div.reply-content-wrapper > div.reply-content')
#     for eachcomment in comments:
#         content = driver.find_element_by_tag_name('p')
#         print(content.text)

# # 把iframe又转回去
# driver.switch_to.default_content()
# sleep(2)
#
# iframe = driver.find_element_by_css_selector("iframe[title='livere-comment']")
# driver.switch_to.frame(iframe)
# comments = driver.find_elements_by_css_selector(
#     '#list > div:nth-child(1) > div.reply-bottom > div.reply-content-wrapper > div.reply-content')
# for eachcomment in comments:
#     content = driver.find_element_by_tag_name('p')
#     print(content.text)
# sleep(5)
# driver.close()

# # selenium的高级操作（一）：控制CSS
# from selenium import webdriver
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("permissions.default.stylesheet", 2)
# driver = webdriver.Firefox(firefox_profile=fp,
#                            executable_path='D:\Program Files\Python38\Lib\site-packages\selenium\geckodriver.exe')
#
# driver.get('http://www.santostang.com/2018/07/04/hello-world/')

# # selenium的高级操作（一）：限制图片的加载
# from selenium import webdriver
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("permissions.default.image", 2)
# driver = webdriver.Firefox(firefox_profile=fp,
#                            executable_path='D:\Program Files\Python38\Lib\site-packages\selenium\geckodriver.exe')
#
# driver.get('http://www.santostang.com/2018/07/04/hello-world/')

# # selenium的高级操作（一）：控制JavaScript的运行
# from selenium import webdriver
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("javascript.enabled", False)
# driver = webdriver.Firefox(firefox_profile=fp,
#                            executable_path='D:\Program Files\Python38\Lib\site-packages\selenium\geckodriver.exe')
#
# driver.get('http://www.santostang.com/2018/07/04/hello-world/')

# # selenium爬虫实战：深圳短租数据
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# # 查找1到5页的数据
# for i in range(0, 5):
#     driver.get(
#         'https://www.airbnb.cn/s/Shenzhen--%E5%B9%BF%E4%B8%9C%E7%9C%81%E4%B8%AD%E5%9B%BD/homes?items_offset=' + str(
#             i * 20))
#     sleep(3)
#     # 关闭地图按钮
#     driver.find_element_by_id('MapToggleBar').click()
#     sleep(2)
#     # 找到页面中所有的出租房
#     # rent_list = driver.find_elements_by_css_selector('div._gig1e7')
#     rent_list = driver.find_elements_by_class_name('_gig1e7')
#     sleep(3)
#     for house in rent_list:
#         # 找到价格
#         # price = house.find_element_by_css_selector('div._1yarz4r')
#         price = house.find_element_by_class_name('_1d8yint7')
#         price = price.text.replace('每晚', "").replace("价格", "")
#         # 找到名称
#         name = house.find_element_by_class_name('_qrfr9x5').text
#         # 找到评论数量
#         try:
#             comment = house.find_element_by_class_name('_69pvqtq').text
#         except:
#             comment = 0
#         # 找到房屋类型大小
#         details = house.find_element_by_class_name('_faldii7').text
#         print(price, name, comment, details)
#
# sleep(5)
# driver.quit()
