from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from stock_scraper.loader.processors import ToDecimal
import json

class BarchartJsonLoader(ItemLoader):

    default_output_processor = TakeFirst()

    eps_in = ToDecimal()

    def parse(self, response):
        print response.body_as_unicode()
        jsonResponse = json.loads(response.body_as_unicode())
    
        data = jsonResponse['data'][0] 

        self.add_value('symbol', data['symbol'])
        self.add_value('symbolName', data['symbolName'])
        self.add_value('eps', data['eps'])

        if len(data['sectors']) > 0:
            self.add_value('industry', data['sectors'][1]['description'])
            self.add_value('sector', data['sectors'][0]['description'])

