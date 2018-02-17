import json
import os.path
import requests
import inspect
from scrapy import signals
from datetime import datetime
from decimal import Decimal
from stock_scraper.items import Stock, Price, Profile, Dividend
from scrapy.exporters import CsvItemExporter

class PayQtrPipeline(object):
    def __init__(self):
        self.qtrMth = lambda: None
        setattr(self, 'qtrMth', [1,2,3,1,2,3,1,2,3,1,2,3])

    def process_item(self, item, spider):

        if 'payDate' in item and item['payDate']:
            spider.log(type(item['payDate']))
            
            if not type(item['payDate']) is datetime :                
                payDate = datetime.strptime(item['payDate'], '%Y-%m-%d')
            else:
                payDate = item['payDate']

            item['payQtrMonth'] = self.qtrMth[payDate.month-1]

        return item

