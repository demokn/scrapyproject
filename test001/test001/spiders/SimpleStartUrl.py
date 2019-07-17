# -*- coding: utf-8 -*-
import scrapy


class SimpleStartUrlSpider(scrapy.Spider):
    name = 'SimpleStartUrl'
    start_urls = [  # 另一种写法, 无需定义`start_requests`方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'SimpleStartUrl-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)
