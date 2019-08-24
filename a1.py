# First change
#second change
import scrapy


class A1Spider(scrapy.Spider):
    name = '1'
    allowed_domains = ['google.com']
    start_urls = ['https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    'https://www.expressvpn.com/what-is-my-ip',
    ]
    #
    #ss
    """6666"""

    def parse(self, response):
        #user_agent = response.css('#id_user_agent::text').extract()
        #for ips in range(0,10):
        	#yield response.follow('https://www.expressvpn.com/what-is-my-ip', callback=self.parse_ips)

    #def parse_ips(self, response)
        ip = response.css('.ip-address::text').extract()
        #yield {'IP':ip}
        #print(ip)
        yield scrapy.Request('https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes', callback=self.parse2, meta={"ip": ip})
        

    def parse2(self, response):
        ag = response.css('#id_user_agent::text').extract()
        ip = response.meta['ip']
        yield {'ag': ag,
        'ip':ip}
    
        
