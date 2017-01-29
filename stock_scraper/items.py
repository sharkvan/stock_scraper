import scrapy
import os.path
import json

class StockLoader():
    def load(self, filePath):
        if os.path.isfile(filePath):
            file = open(filePath, 'r')
            jsonData = json.load(file)
            file.close()
            stock = Stock(jsonData[0])
                
            return stock
        else:
            return Stock()

class Stock(scrapy.Item):
    symbol = scrapy.Field()
    symbolName = scrapy.Field()
    eps = scrapy.Field()
    dividendYield = scrapy.Field()
    dividendFrequency = scrapy.Field()
    dividendAmount = scrapy.Field()
    dividendExDate = scrapy.Field()
    dividendPayDate = scrapy.Field()
    dividendPayQtrMonth = scrapy.Field()
    price = scrapy.Field()
    industry = scrapy.Field()
    sector = scrapy.Field()
    
