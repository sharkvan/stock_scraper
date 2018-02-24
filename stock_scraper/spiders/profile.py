import scrapy
import json
import time
from stock_scraper.items import Profile
from decimal import Decimal
from stock_scraper.config.symbolList import SymbolList
from stock_scraper.utils.files import getStock

class ProfileSpider(scrapy.Spider):
    name = 'profile'

    DEFAULT_REQUEST_HEADERS = {
            'Accept': 'application/json',
            'Origin': 'https://www.barchart.com',
            'Referer': 'https://www.barchart.com/stocks/sectors/rankings',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        }

    def start_requests(self):
        symbolList = SymbolList(self.symbol)

        for symbolConfig in symbolList:
            time.sleep(0.500)
            yield scrapy.Request(
                    url = 'https://core-api.barchart.com/v1/quotes/get?fields=symbol%2CsymbolName%2Csectors%2Ceps&symbols=' + symbolConfig.symbol(),
                    meta = {'symbol': symbolConfig},
                    headers = self.DEFAULT_REQUEST_HEADERS 
                    )

    def parse(self, response):
        jsonResponse = json.loads(response.body_as_unicode())
    
        symbolData = jsonResponse['data'][0] 

        config = response.meta['symbol']
        stock = getStock( config.symbol()
                           , config.initialData()
                           , config.folder
                           )

        profile = Profile()

        profile['symbol'] = config.symbol()
        
        try:
            profile['eps'] = Decimal(stock['eps'])
            profile['eps'] = Decimal(symbolData['eps'])
        except:
            profile['eps'] = Decimal(0)

        if len(symbolData['sectors']) > 0:
            if 'industry' in stock:
                profile['industry'] = stock['industry']
            
            profile['industry'] = symbolData['sectors'][1]['description']
            
            if 'sector' in stock:
                profile['sector'] = stock['sector']
            
            profile['sector'] = symbolData['sectors'][0]['description']

        return profile
