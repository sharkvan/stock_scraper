import scrapy
from stock_scraper.utils.dateutils import friendly_date

class Payment(scrapy.Item):
    amount = scrapy.Field()
    exDate = scrapy.Field(serializer=friendly_date)
    payDate = scrapy.Field(serializer=friendly_date)
    recDate = scrapy.Field(serializer=friendly_date)
    decDate = scrapy.Field(serializer=friendly_date)
