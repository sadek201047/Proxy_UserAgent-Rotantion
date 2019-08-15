# -*- coding: utf-8 -*-
import scrapy


class A2Spider(scrapy.Spider):
    name = 'a2'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes',
    ]

    def parse(self, response):
        ag = response.css('#id_user_agent::text').extract()
        yield {'ag': ag}
