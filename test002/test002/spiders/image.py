# -*- coding: utf-8 -*-
import scrapy
from test002.items import Test002Item


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = Test002Item()  # 实例化item
        imgurls = response.css(".post img::attr(src)").extract()
        item["imgurls"] = imgurls
        yield item
