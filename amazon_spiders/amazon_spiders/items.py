# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_number = scrapy.Field()
    book_name = scrapy.Field()
    # 获取节点中的属性值
    link_addr = scrapy.Field()
    author = scrapy.Field()
    star_number = scrapy.Field()
    comment_number = scrapy.Field()
    book_type = scrapy.Field()
    price = scrapy.Field()
