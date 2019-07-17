# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from dianping.items import ShopItem


class ShopSpider(Spider):
    name = 'shop'
    allowed_domains = ['www.dianping.com']
    start_urls = [
        'http://www.dianping.com/nanjing/ch30/g141',
    ]

    # def start_requests(self):
    #     yield Request('http://www.dianping.com/shop/6205990', self.parse_shop)

    def parse(self, response):
        regions = response.css("#region-nav>a::attr(href)").extract()
        for region in regions:
            yield Request(region, self.parse_region)

    def parse_shop(self, response):
        # with open('out.html', 'wb') as f:
        #     f.write(response.body)
        item = ShopItem()
        item['name'] = response.css('h1.shop-name::text').extract_first()
        item['branch'] = response.css('a.J-branch::text').extract_first()
        item['stars'] = response.css('span.mid-rank-stars::attr("title")').extract_first()
        yield item

    def parse_region(self, response):
        shops = response.css(".shop-all-list .tit>a:first_of_type::attr(href)").extract()
        for shop in shops:
            yield Request(shop, self.parse_shop)

        next_page = response.css("a.next::attr(href)").extract_first()
        if next_page is not None:
            yield Request(next_page, self.parse_region)
