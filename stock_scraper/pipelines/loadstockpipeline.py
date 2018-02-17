import json
import os.path
from decimal import Decimal
from stock_scraper.items import Stock
from stock_scraper.utils.files import getStockFilePath

class LoadStockPipeline(object):

    def process_item(self, item, spider):
        
        try:
            spider.log("Load stock file")
            path = getStockFilePath(item['symbol'], spider.folder)

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

