import scrapy
from scrapy.utils.spider import iterate_spider_output
from stock_scraper.items import Price, Stock
from decimal import Decimal
from stock_scraper.nasdaq.security import Security
from stock_scraper.nasdaq.loaders import NasdaqStringQuoteLoader
from stock_scraper.nasdaq.response import Response

class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['nasdaq.com']

    def start_requests(self):
        with open(self.symbol, 'r') as symbols:
            for symbol in symbols:
                symbol = symbol.strip()
                if not symbol: continue
                yield scrapy.Request( url = 'http://www.nasdaq.com/quotedll/quote.dll?page=InfoQuotes&mode=stock&symbol=' + symbol.lower(), 
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
        return self.parse_rows(response)

    def adapt_response(self, response):
        return response

    def parse_rows(self, response):
        for row in Response(response.body):
            yield self.parse_row(response, row)

    def parse_row(self, response, results):
        loader = NasdaqStringQuoteLoader(
                        item=Price())
        
        loader.parse(results)

        return loader.load_item()
