import json
import os.path
from stock_scraper.items import Stock

def getStockFilePath(symbol, folder):
    path = os.path.join(folder, "results", symbol.lower() + ".json")
    
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    return path

def getStock(symbol, initialData, folder):
        initialData.update({'symbol':symbol})
        try:
            path = getStockFilePath(symbol, folder)

            if os.path.exists(path):
                with open(path, 'r') as file:
                    jsonData = json.load(file)

                initialData.update(jsonData)
            else:
                print "Path not there " + path
        except:
            pass

        return Stock(initialData)
