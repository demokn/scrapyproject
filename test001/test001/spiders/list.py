# -*- coding: utf-8 -*-
import scrapy


class ListSpider(scrapy.Spider):
    name = 'list'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        quotes = response.css('div.quote')  # 提取首页所有名言，保存至变量

        for v in quotes:  # 循环获取每一条名言里面的：名言内容、作者、标签

            text = v.css('.text::text').extract_first()  # 提取名言
            autor = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

            # 接下来进行写文件操作，每个名人的名言储存在一个txt文档里面
            fileName = '%s-语录.txt' % autor  # 定义文件名,如：木心-语录.txt

            with open(fileName, "a+") as f:  # 不同人的名言保存在不同的txt文档，“a+”以追加的形式
                f.write(text)
                f.write('\n')  # ‘\n’ 表示换行
                f.write('标签：' + tags)
                f.write('\n-------\n')
