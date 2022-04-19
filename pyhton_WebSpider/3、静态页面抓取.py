# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/3/26}


# #获取响应内容
# import requests
# r=requests.get('http://www.santostang.com/')
# print("文本编码：",r.encoding)
# print("响应状态码：",r.status_code)
# print("字符串方式的响应体：",r.text)

# # 传递url参数
# import requests
#
# key_dict = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=key_dict)
# print("URL已经正确编码：", r.url)
# print("字符串方式的响应体：\n", r.text)

# # 定制请求头
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
#     'Host': 'www.santostang.com'
# }
# r = requests.get('http://www.santostang.com/', headers=headers)
# print("响应状态码：", r.status_code)

# # 发送post请求
# import requests
#
# key_dict = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', data=key_dict)
# print("字符串方式的响应体：\n", r.text)

# # 超时
# import requests
#
# link = "http://www.santostang.com/"
# r = requests.get(link, timeout=2)

# # 爬虫实践，TOP250电影数据
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_movies():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
#         'Host': 'movie.douban.com'
#     }
#     movie_list = []
#     for i in range(0, 10):
#         link = 'https://movie.douban.com/top250?start=' + str(i * 25)
#         r = requests.get(link, headers=headers, timeout=10)
#         print(str(i + 1), "页响应状态码：", r.status_code)
#         # print(r.text)
#
#         soup = BeautifulSoup(r.text, "lxml")
#         # div_list = soup.find_all('div',class='hd')
#         # for each in div_list:
#         #     movie=each.a.span.text.strip()
#         #     movie_list.append(movie)
#         return movie_list
#
#
# get_movies()
