# -*- coding: utf-8 -*-
import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        pass
