import json
import os.path
import requests
import inspect
from scrapy import signals
from datetime import datetime
from decimal import Decimal
from stock_scraper.items import Stock, Price, Profile, Dividend
from scrapy.exporters import CsvItemExporter

def getSecuritiesFile(spider):
    path = os.path.join(spider.folder, "securities.csv")
    spider.log('Opening securities file at' + path)

    return open(path, 'wb')

class SecuritiesPipeline(object):
    def __init__(self):
        self.items = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def process_item(self, item, spider):
        if item['symbol'] in self.items:
            self.items[item['symbol']].update(item)
        else:
            self.items[item['symbol']] = Stock(item)

        return item

    def spider_closed(self, spider):
        file = getSecuritiesFile(spider)
        exporter = CsvItemExporter(file, encoding='utf8', fields_to_export=('symbol', 'symbolName', 'industry', 'sector', 'frequency', 'eps', 'price', 'divYield', 'exDate', 'amount', 'payDate', 'payQtrMonth', 'change'))
        exporter.start_exporting()

        for symbol in sorted(self.items) :
            stock = self.items[symbol] 

            if 'exDate' in stock and isinstance(stock['exDate'], datetime):
                stock['exDate'] = stock['exDate'].date().isoformat()
            
            if 'payDate' in stock and isinstance(stock['payDate'], datetime):
                stock['payDate'] = stock['payDate'].date().isoformat()
            
            exporter.export_item(stock)

        exporter.finish_exporting()
        file.close()
