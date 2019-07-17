# -*- coding: utf-8 -*-
import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['lab.scrapyd.cn/archives/55.html']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html/']

    def parse(self, response):
        pass
