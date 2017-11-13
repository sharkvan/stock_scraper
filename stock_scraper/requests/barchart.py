import scrapy
from stock_scraper.config.symbolConfig import SymbolConfig
from stock_scraper.sources.barchart.loader import BarchartJsonLoader
from stock_scraper.nasdaq.response import Response
from stock_scraper.utils.files import getStock

class Barchart(scrapy.Request):
    def __init__(self, symbolConfig):
        super(Barchart, self).__init__(
            url = 'https://core-api.barchart.com/v1/quotes/get?fields=symbol%2Cprice%2CsymbolName%2Csectors%2Ceps&symbols=' + symbolConfig.symbol().lower(),
            callback = self.parse,
            meta = {'config': symbolConfig},
            headers = {
                'Referer': 'https://www.barchart.com/stocks/sectors/rankings',
                'Origin': 'https://www.barchart.com',
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
                })

    def parse(self, response):
        config = response.meta['config']
        itemData = getStock( config.symbol()
                           , config.initialData()
                           , config.folder
                           )

        loader = BarchartJsonLoader(
                    item=itemData)

        loader.parse(response)
        return loader.load_item()
