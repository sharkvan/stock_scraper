import json
import requests
from scrapy import signals
from stock_scraper.utils.serializers import json_serial

class PostToStorage(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                storage_service = crawler.settings.get('STORAGE_SERVICE_URI')
        )

    def __init__(self, storage_service):
        self.storage_service = storage_service

    #def open_spider(self, spider):
        

    #def close_spider(self, spider):
        

    def process_item(self, item, spider):
        symbol = item['symbol']
        response = requests.get(self.storage_service + "/" + symbol)
        if response.status_code == 404:
            data = json.dumps(dict(item), default=json_serial, ensure_ascii=True).encode('utf8')
            response = requests.post(self.storage_service, {'stock': data})
        else:
            del item['symbol']
            data = json.dumps(dict(item), default=json_serial, ensure_ascii=True).encode('utf8')
            response = requests.post(self.storage_service + "/" + symbol, {'facet': data})

        response.raise_for_status()

        return item
