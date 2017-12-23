from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class NasdaqStringQuoteLoader(ItemLoader):

    default_output_processor = TakeFirst()

    def parse(self, data):
        self.add_value('symbol', data['symbol'])
        self.add_value('price', data['price'])
        self.add_value('change', data['priceChange'])
        self.add_value('symbolName', data['name'])
        self.add_value('eps', data['earningsPerShare'])
        self.add_value('yearHigh', data['yearHigh'])
        self.add_value('yearLow', data['yearLow'])
