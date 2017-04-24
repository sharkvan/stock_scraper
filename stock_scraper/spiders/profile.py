import scrapy
import json
from stock_scraper.items import Profile
from decimal import Decimal

class ProfileSpider(scrapy.Spider):
    name = 'profile'

    DEFAULT_REQUEST_HEADERS = {
            'Accept': 'application/json',
            'Origin': 'https://www.barchart.com',
            'Referer': 'https://www.barchart.com/stocks/sectors/rankings',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        }

    def start_requests(self):
        with open(self.symbol, 'r') as symbols:
            for symbol in symbols:
                symbol = symbol.strip()
                if not symbol: continue
                yield scrapy.Request(url = 'https://core-api.barchart.com/v1/quotes/get?fields=symbol%2CsymbolName%2Csectors%2Ceps&symbols=' + symbol,
                                         meta = {'symbol': symbol},
                                         headers = self.DEFAULT_REQUEST_HEADERS )

    def parse(self, response):
        jsonResponse = json.loads(response.body_as_unicode())
    
        symbolData = jsonResponse['data'][0] 

        stock = Profile() 

        stock['symbol'] = response.meta['symbol']
        stock['symbolName'] = symbolData['symbolName']
        try:
            stock['eps'] = Decimal(symbolData['eps'])
        except:
            stock['eps'] = Decimal(0)

        if len(symbolData['sectors']) > 0:
            stock['industry'] = symbolData['sectors'][1]['description']
            stock['sector'] = symbolData['sectors'][0]['description']

        return stock
