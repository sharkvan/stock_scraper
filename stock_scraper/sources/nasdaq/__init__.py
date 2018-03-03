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
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
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
        config = response.meta['config']
        itemData = getStock( config.symbol()
                           , config.initialData()
                           , config.folder
                           )

        loader = NasdaqStringQuoteLoader(
                        item=itemData)
        
        loader.parse(results)

        return loader.load_item()

