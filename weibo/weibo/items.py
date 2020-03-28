# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
    url：链接
    title：标题
    leadNews：导语
    '''
    url = scrapy.Field()
    title = scrapy.Field()
    leadNews = scrapy.Field()
