# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from dianping.items import ShopItem
from fontTools.ttLib import TTFont
import re
from urllib.request import urlopen, urlretrieve


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
        shop_config = response.css(".footer-container+script::text").extract_first()
        item['address'] = re.search('address:\s*"(\S*?)"', shop_config).group(1)
        item['tel'] = self.decode(''.join(response.css('.expand-info.tel *::text').extract()), response)
        yield item

    def parse_region(self, response):
        shops = response.css(".shop-all-list .tit>a:first_of_type::attr(href)").extract()
        for shop in shops:
            yield Request(shop, self.parse_shop)

        next_page = response.css("a.next::attr(href)").extract_first()
        if next_page is not None:
            yield Request(next_page, self.parse_region)

    def decode(self, s, response):
        links = response.css('link::attr(href)').extract()
        css_url = None
        for link in links:
            if 'svgtextcss' in link:
                css_url = 'http://' + link.lstrip().lstrip('http:').lstrip('https:').lstrip('//')
                break
        if css_url is None:
            raise RuntimeError('svgtextcss not found')
        css_body = urlopen(css_url).read().decode()
        font_url = 'http://' +  re.search(r'url\("(\S*?.woff)"', css_body).group(1).lstrip().lstrip('http:').lstrip('https:').lstrip('//')
        urlretrieve(font_url, 'tmp_font.woff')
        replace_map = self.parse_ttf('tmp_font.woff')
        for uni_char, actual_char in replace_map.items():
            s = s.replace(uni_char, actual_char)
        return s


    def parse_ttf(self, parse_font_name):
        base_font_map = {
            'e0fb': '8',
            'e318': '9',
            'e684': '7',
            'e702': '2',
            'eae2': '5',
            'ec24': '6',
            'ed97': '3',
            'f138': '1',
            'f3f1': '0',
            'f589': '4',
        }

        base_font = TTFont('base_font.woff')
        base_font_orders = base_font.getGlyphOrder()[2:]

        parse_font = TTFont(parse_font_name)
        parse_font_orders = parse_font.getGlyphOrder()[2:]

        base_font_flags = [list(base_font['glyf'][i].flags) for i in base_font_orders]
        parse_font_flags = [list(parse_font['glyf'][i].flags) for i in parse_font_orders]

        parse_font_map = {}
        for base_index, base_flag in enumerate(base_font_flags):
            for parse_index, parse_flag in enumerate(parse_font_flags):
                if self.compare_flag(base_flag, parse_flag):
                    base_key = base_font_orders[base_index].replace('uni', '').lower()
                    if base_key in base_font_map:
                        parse_key = parse_font_orders[parse_index].replace('uni', '').lower()
                        parse_key = eval(r'u"\u' + str(parse_key) + '"')
                        parse_font_map[parse_key] = base_font_map[base_key]
        return parse_font_map

    def compare_flag(self, l1, l2):
        if len(l1) != len(l2):
            return 0
        for i in range(len(l2)):
            if l1[i] != l2[i]:
                return 0
        return 1
