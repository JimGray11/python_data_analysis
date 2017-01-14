# -*- coding: utf-8 -*-
import scrapy
from  amazon_spiders.items import AmazonSpidersItem


# 主要是为爬取亚马逊最畅销的图书
class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.cn"]
    start_urls = (
        'https://www.amazon.cn/gp/bestsellers/books/ref=zg_bs_books_pg_1?ie=UTF8&pg=1',
    )

    def parse(self, response):
        # 使用xpath来解析网页------主要获取书名，作者，评论数，包装，价格，对应的链接
        nodes = response.xpath('//div[@class="zg_itemRow"]')
        for node in nodes:
            # 创建Item对象
            item = AmazonSpidersItem()
            item['rank_number'] = node.xpath('.//span[@class="zg_rankNumber"]/text()').extract_first()
            item['book_name'] = node.xpath('.//a[@class="a-link-normal"]/text()')[2].extract()
            # 获取节点中的属性值
            item['link_addr'] = node.xpath('.//div[@class="a-fixed-left-grid-col a-col-right"]/a/@href').extract_first()
            item['author'] = node.xpath('.//span[@class="a-size-small a-color-base"]/text()').extract_first()
            item['star_number'] = node.xpath('.//a[@class="a-link-normal"]/@title').extract()
            item['comment_number'] = node.xpath('.//a[@class="a-size-small a-link-normal"]/text()').extract()
            item['book_type'] = node.xpath('.//span[@class="a-size-small a-color-secondary"]/text()').extract()
            item['price'] = node.xpath('.//span[@class="a-size-base a-color-price"]/text()').extract()
            yield item
        # 上述解析完成一个页面, class=zg_page  zg_selected 表示选中的页面
        xpath_next_page = './/li[@class="zg_page zg_selected"]/following-sibling::li/a/@href'
        if response.xpath(xpath_next_page):
            next_page = response.xpath(xpath_next_page).extract_first()
            request = scrapy.Request(next_page, callback=self.parse)
            yield request
