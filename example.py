# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['nearby.com']
    start_urls = ['https://www.nearbuy.com/offers/new-delhi']

    def parse(self, response):
        res=Selector(response=response).xpath('//p/text()').extract()
        print(res)
        f=open('dump.txt','rw+')
        f.write(json.dumps(res))
