# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class Test002Pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载, 或传过来的不是集合则无需循环直接yield
        for imgurl in item["imgurls"]:
            yield Request(imgurl)

    # def file_path(self, request, response=None, info=None):
    #     # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    #     image_guid = request.url.split('/')[-1]  # 提取url前面名称作为图片名。
    #     return image_guid
