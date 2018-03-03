import scrapy
from stock_scraper.config.symbolConfig import SymbolConfig
from stock_scraper.nasdaq.loaders import NasdaqStringQuoteLoader
from stock_scraper.nasdaq.response import Response
from stock_scraper.items import Price
from stock_scraper.utils.files import getStock

class Nasdaq(scrapy.Request):

    def __init__(self, symbolConfig):
        super(Nasdaq, self).__init__(
                    url = 'http://www.nasdaq.com/quotedll/quote.dll?page=InfoQuotes&mode=stock&symbol=' + symbolConfig.symbol().lower(), 
                    callback = self.parse,
                    meta = {'config': symbolConfig},
                    headers = {
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
                    })

    def parse(self, response):
        return self.parse_rows(response)

    def adapt_response(self, response):
        return response

    def parse_rows(self, response):
        for row in Response(response.body):
            yield self.parse_row(response, row)

    def parse_row(self, response, results):
        config = response.meta['config']
        itemData = getStock( config.symbol()
                           , config.initialData()
                           , config.folder
                           )

        loader = NasdaqStringQuoteLoader(
                        item=itemData)
        
        loader.parse(results)

        return loader.load_item()

