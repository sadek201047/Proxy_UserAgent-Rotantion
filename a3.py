import scrapy
class firstSpider(scrapy.Spider):
    name = "ipatranscription"
    start_urls = ['https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    ]
    def parse(self, response):
        ip = response.css('.ip-address::text').extract()
        link = 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
        yield scrapy.Request(url=link, callback=self.parse_contents, meta={"ip_address": ip}, dont_filter=True)

    def parse_contents(self, response):
        uagent = response.css('#id_user_agent::text').extract()
        ip = response.meta['ip_address']
        yield {"user_agent": uagent,"ip_address": ip}