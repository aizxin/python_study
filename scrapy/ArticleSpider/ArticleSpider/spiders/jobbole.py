# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['www.jobbole.com']
    start_urls = ['http://www.jobbole.com/']

    def parse(self, response):
        //*[@id="widgets-homepage-fullwidth"]/div[1]/div[2]/div[2]/p/a[1]
        //*[@id="post-113119"]/div[1]/h1
        pass
