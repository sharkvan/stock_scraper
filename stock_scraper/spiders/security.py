import scrapy
from stock_scraper.config.symbolList import SymbolList
import json
from stock_scraper.sources.factory import Factory

class SecuritySpider(scrapy.Spider):
    name = 'security'

    def start_requests(self):
        symbolList = SymbolList(self.folder)
        factory = Factory()

        for symbolConfig in symbolList:
            yield factory.buildRequest(symbolConfig)
