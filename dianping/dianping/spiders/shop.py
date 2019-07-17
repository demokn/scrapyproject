# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from dianping.items import ShopItem


class ShopSpider(Spider):
    name = 'shop'
    allowed_domains = ['www.dianping.com']
    start_urls = ['http://www.dianping.com/']

    def start_requests(self):
        yield Request('http://www.dianping.com/shop/6205990', self.parse_shop)

    def parse_shop(self, response):
        # with open('out.html', 'wb') as f:
        #     f.write(response.body)
        item = ShopItem()
        item['name'] = response.css('h1.shop-name::text').extract_first()
        item['branch'] = response.css('a.J-branch::text').extract_first()
        item['stars'] = response.css('span.mid-rank-stars::attr("title")').extract_first()
        yield item
