import json
from stock_scraper.utils.serializers import json_serial
from stock_scraper.utils.files import getStockFilePath

class JsonWriterPipeline(object):

    def process_item(self, item, spider):
        path = getStockFilePath(item['symbol'], spider.folder)
        spider.log('write item to ' + path)
        line = json.dumps(dict(item), default=json_serial, ensure_ascii=True).encode('utf8') + "\n"
        self.file = open(path, 'w')
        self.file.write(line)
        self.file.close()
        
        return item
