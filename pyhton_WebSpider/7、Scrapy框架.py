# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/4/13}

# 通过Scrapy抓取博客
# 1、创建Scrapy项目
# 在cmd中进入自定义目录，例如桌面，运行下面命令：cd C:\Users\santostang\desktop
# 然后运行命令scrapy startproject blogSpider，其中blogSpider就是项目名称，
# 在开始爬虫之前，定义爬虫的目标字段，那么打开items.py，在BlogspiderItem类输入以下需要的字段
# import scrapy
# class BlogspiderItem(scrapy.Item):
#     title = scrapy.Field()
#     link = scrapy.Field()
#     content = scrapy.Field()
# 2、获取博客网页并保存
# 在cmd的当前目录输入以下命令scrapy genspider santostang www.santostang.com,
# scrapy crawl santostang
# scrapy crawl santostang -o article.json
# scrapy crawl santostang -o article.json
