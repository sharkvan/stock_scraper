# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os.path
from scrapy import signals
from datetime import datetime
from decimal import Decimal
from stock_scraper.items import Stock, Price, Profile, Dividend
from scrapy.exporters import CsvItemExporter

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.strftime("%Y-%m-%d")
        return serial

    return str(obj)

def getStockFilePath(item, spider):
    path = os.path.join(spider.folder, item['symbol'].lower() + ".json")
    spider.log('reading item from ' + path)
    
    if not os.path.exists(os.path.dirname(path)):
        spider.log("Creating folder path " + os.path.dirname(path))
        os.makedirs(os.path.dirname(path))

    return path

def getSecuritiesFile(spider):
    path = os.path.join(spider.folder, "securities.csv")
    spider.log('Opening securities file at' + path)

    return open(path, 'wb')

class LoadStockPipeline(object):

    def process_item(self, item, spider):
        
        try:
            spider.log("Load stock file")
            path = getStockFilePath(item, spider)

            if os.path.exists(path):
                file = open(path, 'r')
                jsonData = json.load(file)
                file.close()
                stock = Stock(jsonData)
            else:
                spider.log("Creating blank stock")
                stock = Stock()
        except:
            stock = Stock()

        stock.setdefault("symbol", None)
        stock.setdefault("symbolName", None)
        stock.setdefault("industry", None)
        stock.setdefault("sector", None)
        stock.setdefault("frequency", None)
        stock.setdefault("payQtrMonth", 0)
        stock.setdefault("change", Decimal(0))
        stock.setdefault("price", Decimal(0))
        stock.setdefault("eps", Decimal(0))
        stock.setdefault("divYield", Decimal(0))
        stock.setdefault("amount", Decimal(0))
        stock.setdefault("annualAmount", Decimal(0))
        stock.setdefault("exDate", None)
        stock.setdefault("payDate", None)
        
        stock.update(item)

        return stock

class PricePipeline(object):
    def process_item(self, item, spider):
        if 'annualAmount' in item :
            if item['annualAmount'] and item['price'] :
                item['divYield'] = Decimal(item['annualAmount']) / Decimal(item['price'])

        return item

class PayQtrPipeline(object):
    def __init__(self):
        self.qtrMth = lambda: None
        setattr(self, 'qtrMth', [1,2,3,1,2,3,1,2,3,1,2,3])

    def process_item(self, item, spider):

        spider.log(type(item['payDate']))
        if item['payDate']:
            if not type(item['payDate']) is datetime :                
                payDate = datetime.strptime(item['payDate'], '%Y-%m-%d')
            else:
                payDate = item['payDate']

            item['payQtrMonth'] = self.qtrMth[payDate.month-1]

        return item

class JsonWriterPipeline(object):

    def process_item(self, item, spider):
        path = getStockFilePath(item, spider)
        spider.log('write item to ' + path)
        line = json.dumps(dict(item), default=json_serial, ensure_ascii=True).encode('utf8') + "\n"
        self.file = open(path, 'w')
        self.file.write(line)
        self.file.close()
        
        return item

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

        for stock in self.items.itervalues() :
            stock['exDate'] = stock['exDate'].date().isoformat()
            stock['payDate'] = stock['payDate'].date().isoformat()
            exporter.export_item(stock)

        exporter.finish_exporting()
        file.close()
