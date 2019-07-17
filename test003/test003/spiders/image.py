# -*- coding: utf-8 -*-
import scrapy
from test003.items import Test003Item


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html',
        'http://lab.scrapyd.cn/archives/57.html',
    ]

    def parse(self, response):
        # 实例化item
        item = Test003Item()
        # 注意imgurls是一个集合, 也就是多张图片
        item['imgurls'] = response.css(".post img::attr(src)").extract()
        # 抓取文章标题作为图集名称
        item['name'] = response.css(".post-title a::text").extract_first()
        yield item
