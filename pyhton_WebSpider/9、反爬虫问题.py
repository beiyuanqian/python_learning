# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/17}

# # 修改请求头
# # 默认请求头为python-requests/2.23.0
# import requests
# r = requests.get('http://www.santostang.com/')
# print(r.request.headers)
#
# # 把请求头改为真正浏览器的格式
# link = 'http://www.santostang.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get(link, headers=headers)
# print(r.request.headers)

# # 做一个User-Agent池，随机切换User-Agent
# from fake_useragent import UserAgent
# import requests
#
# link = 'http://www.santostang.com/'
# ua = UserAgent()
# for i in range(0,5):
#     headers = {"User-Agent": ua.random}
#     response = requests.get(url=link, headers=headers)
#     # 响应信息状态
#     print(response.status_code)
#     print(response.request.headers)

# # 修改爬虫的间隔时间
# import time
#
# # 设置固定时间间隔
# t1 = time.time()
# time.sleep(2)
# t2 = time.time()
# total_time = t2 - t1
# print(total_time)
#
# # 使用random库对时间进行随机数设置
# import random
#
# for i in range(0, 5):
#     # 这里random.randint(0, 2)的结果是0，1，2，而random.random()是一个0~1的随机数，最后结果在0~3秒之间
#     sleep_time = random.randint(0, 2) + random.random()
#     print(sleep_time)
#     time.sleep(sleep_time)

# 把爬虫程序与时间间隔结合在一起
import requests
from bs4 import BeautifulSoup
import time
import random

link = 'http://www.santostang.com/'


def scrap(link):
    headers = {}
    r = requests.get(link, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    return soup


# 每次间隔0，3秒进行爬虫
# soup = scrap(link)
# title_list = soup.find_all('h1', class_='post-title')
# for eachone in title_list:
#     url = eachone.a['href']
#     print('开始爬取这篇博客：', url)
#     soup_article = scrap(url)
#     title = soup_article.find('h1', 'view-title').text.strip()
#     print('这篇博客得标题为：', title)
#     sleep_time = random.randint(0, 2) + random.random()
#     print('开始休息：', sleep_time, '秒')
#     time.sleep(sleep_time)

# 每次爬取0，3秒，也不太像真实的访问，可以设置每爬取2次数据休息10秒
scrap_times = 0
soup = scrap(link)
title_list = soup.find_all('h1', class_='post-title')
for eachone in title_list:
    url = eachone.a['href']
    print('开始爬取这篇博客：', url)
    soup_article = scrap(url)
    title = soup_article.find('h1', 'view-title').text.strip()
    print('这篇博客得标题为：', title)

    scrap_times += 1
    if scrap_times % 2 == 0:
        sleep_time = 10 + random.random()
    else:
        sleep_time = random.randint(0, 2) + random.random()
    print('开始休息：', sleep_time, '秒')
    time.sleep(sleep_time)

