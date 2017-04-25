import scrapy
import os.path
import json
from datetime import datetime

def friendly_date(obj):

    if isinstance(obj, datetime):
        serial = obj.date().isoformat()
        return serial

    return str(obj)

class Price(scrapy.Item):
    symbol = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()

class Profile(scrapy.Item):
    symbol = scrapy.Field()
    symbolName = scrapy.Field()
    industry = scrapy.Field()
    sector = scrapy.Field()
    eps = scrapy.Field()

class Dividend(scrapy.Item):
    symbol = scrapy.Field()
    price = scrapy.Field()
    divYield = scrapy.Field()
    frequency = scrapy.Field()
    amount = scrapy.Field()
    annualAmount = scrapy.Field()
    exDate = scrapy.Field()
    payDate = scrapy.Field()
    payQtrMonth = scrapy.Field()
    
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
    exDate = scrapy.Field()
    payDate = scrapy.Field()
    payQtrMonth = scrapy.Field()

class CsvStock(Stock):
    exDate = scrapy.Field(Stock.fields['exDate'], serializer=friendly_date)
    payDate = scrapy.Field(Stock.fields['payDate'], serializer=friendly_date)
