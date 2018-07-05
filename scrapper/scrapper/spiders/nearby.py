# -*- coding: utf-8 -*-
import scrapy
from scrapper.items import NearbyItem

class NearbySpider(scrapy.Spider):
    name = 'nearby'
    allowed_domains = ['nearby.com']
    start_urls = ['https://www.nearbuy.com/travel']

    def parse(self, response):
        item = NearbyItem()
        item['name'] = response.xpath('//h3[contains(@class, "card__title")]/text()').extract()
        item['value'] = response.xpath('//p[contains(@class, "actual-price")]/text()').extract()
        item['location'] = response.xpath('//h3[contains(@class, "card__location")]/text()').extract()
        print(item)
        
