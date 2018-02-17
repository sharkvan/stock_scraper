import scrapy
import os.path
import json
from datetime import datetime
from stock_scraper.utils.dateutils import friendly_date

class Dividend(scrapy.Item):
    symbol = scrapy.Field()
    price = scrapy.Field()
    divYield = scrapy.Field()
    frequency = scrapy.Field()
    amount = scrapy.Field()
    annualAmount = scrapy.Field()
    exDate = scrapy.Field(serializer=friendly_date)
    payDate = scrapy.Field(serializer=friendly_date)
    payQtrMonth = scrapy.Field()
