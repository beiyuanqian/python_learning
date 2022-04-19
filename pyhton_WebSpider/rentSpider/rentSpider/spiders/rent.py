import scrapy


class RentSpider(scrapy.Spider):
    name = 'rent'
    allowed_domains = ['www.airbnb.cn/s/%E6%B7%B1%E5%9C%B3/homes?map_toggle=false']
    start_urls = ['http://www.airbnb.cn/s/%E6%B7%B1%E5%9C%B3/homes?map_toggle=false/']

    def parse(self, response):
        pass
