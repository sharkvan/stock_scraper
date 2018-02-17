import scrapy
from stock_scraper.utils.dateutils import friendly_date

class Stock(scrapy.Item):
    symbol = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    symbolName = scrapy.Field()
    industry = scrapy.Field()
    sector = scrapy.Field()
    eps = scrapy.Field()
    divYield = scrapy.Field()
    frequency = scrapy.Field()
    amount = scrapy.Field()
    annualAmount = scrapy.Field()
    exDate = scrapy.Field(serializer=friendly_date)
    payDate = scrapy.Field(serializer=friendly_date)
    payQtrMonth = scrapy.Field()
    yearHigh = scrapy.Field()
    yearLow = scrapy.Field()
