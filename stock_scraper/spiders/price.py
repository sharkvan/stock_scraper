import scrapy
from stock_scraper.items import Price
from decimal import Decimal

class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['nasdaq.com']

    def start_requests(self):
        with open(self.symbol, 'r') as symbols:
            for symbol in symbols:
                symbol = symbol.strip()
                if not symbol: continue
                yield scrapy.Request( url = 'http://www.nasdaq.com/symbol/' + symbol.lower(), 
                                      callback = self.parse,
                                      meta = {'symbol': symbol},
                                      headers = {
                                        'Accept-Encoding': 'gzip, deflate, sdch',
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                        'Host': 'www.nasdaq.com',
                                        'Referer': 'https://www.nasdaq.com/',
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
                                    })
                
    def parse(self, response):
        stock = Price() 
        stock['symbol'] = response.meta['symbol']
        try:
            stock['price'] = Decimal(response.css('#qwidget_lastsale::text').extract_first().strip('$'))
        except:
            stock['price'] = Decimal(0)

        try:
            stock['change'] = Decimal(response.css('#qwidget_netchange::text').extract_first())
        except:
            stock['change'] = Decimal(0)

        return stock
