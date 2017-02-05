import scrapy
from stock_scraper.items import StockLoader, Stock

class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['nasdaq.com']
    start_urls = ['http://www.nasdaq.com/symbol/']

    def start_requests(self):
        yield scrapy.Request(url='http://www.nasdaq.com/symbol/' + self.symbol)

    def parse(self, response):
        stockLoader = StockLoader()
        stock = stockLoader.load(self.filePath) 
        stock['symbol'] = self.symbol
        stock['price'] = response.css('#qwidget_lastsale::text').extract_first().strip('$')

        return stock
