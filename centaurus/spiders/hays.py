# -*- coding: utf-8 -*-
import scrapy


class HaysSpider(scrapy.Spider):
    name = 'hays'
    allowed_domains = ['hays']
    start_urls = ['http://hays/']

    def parse(self, response):
        pass
