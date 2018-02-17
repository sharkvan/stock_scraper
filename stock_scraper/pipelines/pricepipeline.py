import json
import os.path
import requests
import inspect
from scrapy import signals
from datetime import datetime
from decimal import Decimal
from stock_scraper.items import Stock, Price, Profile, Dividend
from scrapy.exporters import CsvItemExporter

class PricePipeline(object):
    def process_item(self, item, spider):
        if 'annualAmount' in item and 'price' in item :
            if item['annualAmount'] and item['price'] :
                item['divYield'] = Decimal(item['annualAmount']) / Decimal(item['price'])

        return item

