# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ShopItem(scrapy.Item):
    name = scrapy.Field()  # 店铺名
    branch = scrapy.Field()  # 分店数量
    stars = scrapy.Field()  # 店铺星级
    reviewCount = scrapy.Field()  # 评论条数
    avgPrice = scrapy.Field()  # 人均价格
    commentScore = scrapy.Field()  # 评分
    address = scrapy.Field()  # 地址
    tel = scrapy.Field()  # 电话
    commentPic = scrapy.Field()  # 带图评论数
    commentGood = scrapy.Field()  # 好评数
    commentCommon = scrapy.Field()  # 中评数
    commentBad = scrapy.Field()  # 差评数
