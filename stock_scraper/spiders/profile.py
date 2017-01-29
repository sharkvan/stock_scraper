import scrapy
import json
from stock_scraper.items import Stock, StockLoader

class ProfileSpider(scrapy.Spider):
    name = 'profile'

    DEFAULT_REQUEST_HEADERS = {
            'Accept': 'application/json',
            'Origin': 'https://www.barchart.com',
            'Referer': 'https://www.barchart.com/stocks/sectors/rankings',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        }

    def start_requests(self):
        yield scrapy.Request(url='https://core-api.barchart.com/v1/quotes/get?fields=symbol%2CsymbolName%2Csectors%2CmarketCap%2CpeRatioTrailing%2CearningsPerShare%2CannualNetIncome%2Cbeta%2CdividendRate%2CdividendYield&method=%2Fquotes%2Fget&raw=1&symbols=' + self.symbol,
                                     headers=self.DEFAULT_REQUEST_HEADERS )

    def parse(self, response):
        jsonResponse = json.loads(response.body_as_unicode())
    
        symbolData = jsonResponse['data'][0] 

        stockLoader = StockLoader()
        stock = stockLoader.load(self.filePath) 

        stock['symbol'] = self.symbol
        stock['symbolName'] = symbolData['symbolName']
        stock['eps'] = symbolData['earningsPerShare']
        stock['dividendYield'] = symbolData['dividendYield']

        return stock
