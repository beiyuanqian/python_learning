# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/1}

# # 存储至TXT或csv
# # 存储至txt
# title1 = "This is a test sentence.\n"
# title2 = "This is a test sentence.\nThis is a test sentence."
# with open(r'C:\Users\gree\Desktop\test.txt', 'a+') as f:
#     f.write(title1)
#     f.write(title2)
#     f.close()

# # 多个变量写入txt文件时，可使用分隔符Tab,用'\t'.join将变量连接成一个字符串
# output = '\t'.join(['name', 'title', 'age', 'gender'])
# with open(r'C:\Users\gree\Desktop\test1.txt', 'a+') as f:
#     f.write(output)
#     f.close()

# # 读取txt文件用f.read()，逐行读取用.splitlines()
# with open(r'C:\Users\gree\Desktop\test.txt', 'r') as f:
#     result = f.read().splitlines()
#     print(result)

# # 把数存储至csv
# import csv
#
# with open(r'C:\Users\gree\Desktop\test.csv', 'r', encoding='UTF-8') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     for row in csv_reader:
#         print(row)
#         print(row[0])

# # 把数据写入csv，可以将变量加入到一个列表中，再用writerow()方法把一个列表直接写入一列中
# import csv
#
# output_list = ['A1', 'B1', 'C1']
# with open(r'C:\Users\gree\Desktop\test1.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
#     w = csv.writer(csvfile)
#     w.writerow(output_list)

# # python操作mysql数据库
# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "33060", "scraping")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # sql插入语句
# sql = """INSERT INTO urls (url,content) VALUES ('www.baidu.com','This is content.')"""
# # try:
# # 执行sql语句
# cursor.execute(sql)
# # 提交到数据库执行
# db.commit()
# # except:
# #     # 如果发生错误则回滚
# #     db.rollback()
# # 关闭数据库连接
# db.close()

# # 把博客爬取的标题和url地址使用python存储到mysql数据库中
# import requests
# from bs4 import BeautifulSoup
# import pymysql
#
# db = pymysql.connect('localhost', 'root', '33060', 'scraping')
# cursor = db.cursor()
# link = 'http://www.santostang.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get(link, headers=headers)
#
# soup = BeautifulSoup(r.text, 'lxml')
# title_list = soup.find_all('h1', class_='post-title')
# for eachone in title_list:
#     url = eachone.a['href']
#     title = eachone.a.text.strip()
#     cursor.execute("insert into urls (url,content) values (%s,%s)", (url, title))
# db.commit()
# db.close()

# # 连接MongoDB
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client.blog_database
# collection = db.blog

# # 把博客爬取的标题存储到MongoDB数据库中
# import requests
# import datetime
# from bs4 import BeautifulSoup
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client.blog_database
# collection = db.blog
#
# link = 'http://www.santostang.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get(link, headers=headers)
# soup = BeautifulSoup(r.text, "lxml")
# title_list = soup.find_all('h1', class_='post-title')
# print(title_list)
# for eachone in title_list:
#     url = eachone.a['href']
#     title = eachone.a.text.strip()
#     # 将爬虫获取的数据存入post字典中
#     post = {"url": url, "title": title, "date": datetime.datetime.utcnow()}
#     # 使用insert_one加入集合collection中
#     collection.insert_one(post)
#     #最后在bin目录里用mongo打开，再使用use blog_database和db.blog.find().pretty()查询数据

# MongoDB爬虫实践：虎扑论坛
import requests
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient
from time import sleep


# 获取页面
def get_page(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    r = requests.get(link, headers=headers)
    # 此网站使用gzip封装，需要使用r.content解封装
    html = r.content
    # 由UTF-8解码为unicode
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    print(soup)
    return soup


# # 解析网页
# def get_data(post_list):
#     data_list = []
#     for post in post_list:
#         title = post.find('div', class_='post-title').a.text.strip()
#         post_link = post.find('div', class_='post-title').a['href']
#         post_link = 'https://bbs.hupu.com/bxj' + post_link
#         author = post.find('div', class_='post-auth').a.text.strip()
#         author_link = post.find('div', class_='post-auth').a['href']
#         start_time = post.find('div', class_='post-time').text.strip()
#         # if start_time.find('-') == 4:
#         #     date_time = datetime.datetime.strptime(start_time, '%Y-%m-%d').date()
#         # elif start_time.find('-') == 2:
#         #     date_time=str('2021-' + start_time)
#         #     # date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M').date()
#         reply_view = post.find('div', class_='post-datum').text.strip()
#         reply = reply_view.split('/')[0].strip()
#         view = reply_view.split('/')[1].strip()
#         data_list.append([title, post_link, author, author_link, reply, view, start_time])
#     return data_list
#
#
# def get_data1(post_list):
#     data_list = []
#     for post in post_list:
#         title = post.find('div', class_='titlelink box').text.strip()
#         post_link = post.find('div', class_='titlelink box').a['href']
#         post_link = 'https://bbs.hupu.com/bxj' + post_link
#         author = post.find('div', class_='author box').a.text.strip()
#         author_link = post.find('div', class_='author box').a['href']
#         start_time = post.find('div', class_='author box').contents[5].text.strip()
#         reply_view = post.find('span', class_='ansour box').text.strip()
#         reply = reply_view.split('/')[0].strip()
#         view = reply_view.split('/')[1].strip()
#         reply_time = post.find('div', class_='endreply box').a.text.strip()
#         if ':' in reply_time:
#             date_time = str(datetime.date.today()) + " " + reply_time
#             date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
#         elif reply_time.find('-') == 4:
#             date_time = datetime.datetime.strptime(reply_time, '%Y-%m-%d').date()
#         else:
#             date_time = datetime.datetime.strptime('2021' + reply_time, '%Y-%m-%d').date()
#         last_reply = post.find('div', class_='endreply box').span.text.strip()
#         data_list.append([title, post_link, author, author_link, start_time, reply, view, date_time, last_reply])
#     return data_list
#
#
# class MongoAPI(object):
#     def __init__(self, db_ip, db_port, db_name, table_name):
#         self.db_ip = db_ip
#         self.db_port = db_port
#         self.db_name = db_name
#         self.table_name = table_name
#         self.conn = MongoClient(host=self.db_ip, port=self.db_port)
#         self.db = self.conn[self.db_name]
#         self.table = self.db[self.table_name]
#
#     def get_one(self, query):
#         return self.table.find_one(query, projection={'_id': False})
#
#     def get_all(self, query):
#         return self.table.find(query)
#
#     def add(self, kv_dict):
#         return self.table.insert(kv_dict)
#
#     def delete(self, query):
#         return self.table.delete_many(query)
#
#     def check_exist(self, query):
#         ret = self.table.find_one(query)
#         return ret != None
#
#     # 如果没有会新建
#     def update(self, query, kv_dict):
#         self.table.update_one(query, {'$set': kv_dict}, upsert=True)
# link = 'https://bbs.hupu.com/bxj-1'
# soup = get_page(link)
# print('1:')
link = 'https://bbs.hupu.com/bxj'
soup = get_page(link)
print('2:')
# for i in range(1,3):
#     link = 'https://bbs.hupu.com/bxj-'+str(i)
#     soup = get_page(link)
#     hupu_host = MongoAPI('localhost', 27017, 'hupu', 'post')
#     if link == 'https://bbs.hupu.com/bxj-1':
#         post_all = soup.find_all('li', class_='bbs-sl-web-post-layout bbs-sl-web-post-body')
#         data_list = get_data(post_all)
#         for each in data_list:
#             # print(each)
#             hupu_host.update({'title': each[0],
#                            'post_link': each[1],
#                            'autor': each[2],
#                            'autor_link': each[3],
#                            'reply': each[4],
#                            'view': each[5],
#                            'start_time': each[6],
#                            })
#     else:
#         post_all = soup.find('ul', class_="for-list")
#         post_list = post_all.find_all('li')
#         data_list = get_data1(post_list)
#         for each in data_list:
#             hupu_host.update({'title': each[0],
#                            'post_link': each[1],
#                            'autor': each[2],
#                            'autor_link': each[3],
#                            'start_time': each[4],
#                            'reply': each[5],
#                            'view': each[6],
#                            'date_time': each[7],
#                            'last_reply': each[8],
#                            })
#     sleep(3)


