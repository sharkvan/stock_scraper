from stock_scraper.sources.nasdaq import Nasdaq
from stock_scraper.sources.barchart import Barchart

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

