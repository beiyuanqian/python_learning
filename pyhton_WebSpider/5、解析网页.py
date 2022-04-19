# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/3/31}

# # 使用正则表达式解析网页，主要有re.match()、re.search()、re.findall()方法
# import requests
# import re
#
# link = 'http://www.santostang.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get(link, headers=headers)
# html = r.text
#
# title_list = re.findall('<h1 class="post-title"><a href=.*?>(.*?)</a></h1>', html)
# print(title_list)

# # 使用BeautifulSoup解析网页，可以从HTML或XML文件中提取数据
# import requests
# from bs4 import BeautifulSoup
# import re

# link = 'http://www.santostang.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.text, 'lxml')
# print(soup)

# # 可以对代码进行美化
# print(soup.prettify())

# # 使用BeautifulSoup获取博客标题
# first_title = soup.find("h1", class_="post-title").a.text.strip()
# print("第一篇文章的标题是：", first_title)
# title_list = soup.find_all("h1", class_="post-title")
# for i in range(len(title_list)):
#     title = title_list[i].a.text.strip()
#     print("第 %s 篇文章的标题是：%s" % (i + 1, title))

# # BeautifulSoup的其它功能：遍历文档树
# # 获取<h1>标签
# print(soup.header.h1)
# 获取某个标签的所有子节点，用contents把它的子节点以列表的方式输出
# print(soup.header.div.contents)
# # 使用children方法获得所有子标签，只能获取该节点的下一级节点
# for child in soup.header.div.children:
#     print(child)
# # 如果要获得所有子子孙孙的节点，用.descendants方法
# for child in soup.header.div.descendants:
#     print(child)
# # 用.parent方法获得父节点的内容
# a_tag=soup.header.div.a
# print(a_tag.parent)

# # BeautifulSoup的其它功能：搜索文档树,最常用find()和find_all()
# # find()和find_all()还可以和re正则解和起来使用
# for tag in soup.find_all(re.compile("^h")):
#     print(tag.name)

# # BeautifulSoup的其它功能：CSS选择器，既可以作为遍历文档树的方法提取数据，也可以作为搜索文档树的方法提取数据
# #可以通过tag标签逐层寻找
# print(soup.select("header h1"))
# # 也可以通过某个tag标签下的直接子标签遍历
# print(soup.select("header>h3"))
# print(soup.select("div>a"))
# #也可以实现搜索文档树的功能，如找出所有链接以http://www.santostang.com/开头的<a>标签
# print(soup.select('a[href^="http://www.santostang.com/"]'))

# # 使用lxml(使用Xpath语法)解析网页，使用lxml提取网页源代码有3种方法：Xpath选择器、CSS选择器和BeautifulSoup的find()方法
# import requests
# from lxml import etree
#
# link = 'http://www.santostang.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get(link, headers=headers)
# # 解析为lxml格式
# html=etree.HTML(r.text)
# titl_list=html.xpath('//h1[@class="post-title"]/a/text()')
# print(titl_list)

# BeautifulSoup爬虫实践：房屋价格数据
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

# 爬前5页的内容
for i in range(1, 2):
    link = 'https://www.airbnb.cn/s/%E6%B7%B1%E5%9C%B3/homes?map_toggle=false&items_offset=' + str(i * 20)
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 找到全部房屋信息
    houses = soup.find_all('div', class_='_14csrlku')
    print("第" + str(i) + "页的内容为：")
    for house in houses:
        # print(house)
        name = house.find('div', class_='_qrfr9x5').text
        price = house.find('span', class_='_1d8yint7').text
        room_type = house.find('span', class_='_faldii7').text
        try:
            comment = house.find('span', class_='_69pvqtq').text
        except:
            comment = 0

        print(name, price, room_type, comment)
    sleep(3)
