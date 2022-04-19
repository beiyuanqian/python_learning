# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/19}

# # 获取网站的中文显示乱码
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.w3school.com.cn/'
# r = requests.get(url)
# # 转换编码格式，不然中文显示为乱码
# r.encoding = 'gbk'
# soup = BeautifulSoup(r.text, 'lxml')
# xx = soup.find('div', id='d1').h2.text
# print(xx)

# 网页使用gzip压缩
import requests
import chardet

url = 'http://www.sina.com.cn/'
r = requests.get(url)

# 直接输出显示乱码
# print(r.text)
# 显示中文
after_gzip = r.content
print('解码后字符串的编码为', chardet.detect(after_gzip))
print(after_gzip.decode('UTF-8'))
