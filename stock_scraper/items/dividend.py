import scrapy

class Dividend(scrapy.Item):
    symbol = scrapy.Field()
    dividends = scrapy.Field()
