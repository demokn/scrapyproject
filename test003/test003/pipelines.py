# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class Test003Pipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for imgurl in item['imgurls']:
            # meta里面的数据是从spider获取, 然后通过meta传递给下面方法: file_path
            yield Request(imgurl, meta={'name': item['name']})


    # 重命名, 如果不重写该函数, 图片名为哈希
    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图集名称
        name = request.meta['name']
        # 过滤windows字符串, 否则可能导致乱码或无法下载
        name = re.sub(r'[?\\*|"<>:/"]', '', name)
        # 分文件夹存储
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename
