# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/5/7}

# # 输出9x9乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(str(i) + "x" + str(j) + "=" + str(i * j), end=" ")
#     print("")

# # 计算奖金
# I = int(input("请输入月利润："))
# I = I / 10000
# if I <= 10:
#     bonus = I * 0.1
# elif I > 10 and I <= 20:
#     bonus = 10 * 0.1 + (I - 10) * 0.075
# elif I > 20 and I <= 40:
#     bonus = 10 * (0.1 + 0.075) + (I - 20) * 0.05
# elif I > 40 and I <= 60:
#     bonus = 10 * (0.1 + 0.075) + 20 * 0.05 + (I - 40) * 0.03
# elif I > 60 and I <= 100:
#     bonus = 10 * (0.1 + 0.075) + 20 * (0.05 + 0.03) + (I - 60) * 0.015
# elif I > 100:
#     bonus = 10 * (0.1 + 0.075) + 20 * (0.05 + 0.03) + 40 * 0.015 + (I - 100) * 0.01
# print(bonus)

# # 用字典的值对字典排序
# import operator
#
# a = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(a.items())
# print(sorted(a.items()))
# print(sorted(a.items(), key=operator.itemgetter(1)))

# # 获取页面
# import requests
#
# # 定义link为目标网页地址
# link = "http://www.santostang.com"
# # 定义请求头的浏览器代理，伪装成浏览器
# headers = {'User-Agent': 'Mozilla/5.0(Windows; U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# # 请求网页
# r = requests.get(link, headers=headers)
# # r.text是获取网页内容代码
# print(r.text)

# # 获取第一篇文章标题
# import requests
# from bs4 import BeautifulSoup
#
# link = "http://www.santostang.com"
# headers = {'User-Agent': 'Mozilla/5.0(Windows; U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# r = requests.get(link, headers=headers)
#
# soup = BeautifulSoup(r.text, "html.parser")
# title = soup.find("h1", class_="post-title").a.text.strip()
# print(title)
#
# with open('title_test.txt', "a+")as f:
#     f.write(title)
