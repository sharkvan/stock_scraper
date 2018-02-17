import scrapy

class Profile(scrapy.Item):
    symbol = scrapy.Field()
    symbolName = scrapy.Field()
    industry = scrapy.Field()
    sector = scrapy.Field()
    eps = scrapy.Field()
