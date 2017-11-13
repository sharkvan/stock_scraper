from stock_scraper.requests.nasdaq import Nasdaq
from stock_scraper.requests.barchart import Barchart

def nasdaqSource(symbolConfig):
    return Nasdaq(symbolConfig)

def barchartSource(symbolConfig):
    return Barchart(symbolConfig)

class Factory():

    options = {
            "nasdaq" : nasdaqSource,
            "barchart" : barchartSource
            }

    def buildRequest(self, symbolConfig):

        return self.options[symbolConfig.source()](symbolConfig)

