import scrapy

class Price(scrapy.Item):
    symbol = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()

