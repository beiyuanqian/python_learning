import scrapy
from bs4 import BeautifulSoup
# from blogSpider.items import BlogspiderItem
from blogSpider.items import BlogspiderItem


class SantostangSpider(scrapy.Spider):
    name = 'santostang'
    allowed_domains = ['www.santostang.com']
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        # # 获取博客网页并保存在本地
        # print(response.text)
        # filename = r'D:\PYproject\pyhton爬虫\blogSpider\blogSpider\index.html'
        # with open(filename, 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # # 提取标题
        # soup = BeautifulSoup(response.text, 'lxml')
        # first_title = soup.find('h1', class_='post-title')
        # print('第一篇的文章标题为：', first_title)
        # title_list = soup.find_all('h1', class_='post-title')
        # for i in range(len(title_list)):
        #     title = title_list[i].a.text.strip()
        #     print("第 %s 篇文章的标题为：%s" % (i + 1, title))
        # # 将提取到的数据封装到BlogspiderItem对象中
        # # 存放文章信息的列表
        # items = []
        # soup = BeautifulSoup(response.text, 'lxml')
        # title_list = soup.find_all('h1', class_='post-title')
        # for i in range(len(title_list)):
        #     # 将数据封装到BlogspiderItem对象，字典类型数据
        #     item = BlogspiderItem()
        #     title = title_list[i].a.text.strip()
        #     link = title_list[i].a['href']
        #     # 变成字典
        #     item['title'] = title
        #     item['link'] = link
        #     items.append(item)
        # return items
        soup = BeautifulSoup(response.text, 'lxml')
        title_list = soup.find_all('h1', class_='post-title')
        for i in range(len(title_list)):
            # 将数据封装到BlogspiderItem对象，字典类型数据
            item = BlogspiderItem()
            title = title_list[i].a.text.strip()
            link = title_list[i].a['href']
            # 变成字典
            item['title'] = title
            item['link'] = link
            # 根据文章链接，发送request请求，并传递item参数
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find('div', class_='view-content').text.strip()
        content = content.replace('\n', ' ')
        item['content'] = content
        yield item
