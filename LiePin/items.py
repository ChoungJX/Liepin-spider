# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Position = scrapy.Field()
    Company = scrapy.Field()
    All = scrapy.Field()
    Work_location = scrapy.Field()
    Annual_salary = scrapy.Field()
    Hands_on_background = scrapy.Field()
    Education = scrapy.Field()
    
