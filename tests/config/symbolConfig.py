import unittest
import json
import os.path
from stock_scraper.config.symbolConfig import SymbolConfig

class TestSymbolConfig(unittest.TestCase):

    def test_loading_config(self):
        testFolder = os.path.join(os.getcwd())

        file = open(os.path.join(testFolder, "symbols.json"))
        items = json.load(file)
        item = items['symbols'][0]
        target = SymbolConfig(item)

        self.assertEquals('ABDC', target.symbol())
        self.assertEquals('nasdaq', target.source())

        item = items['symbols'][1]
        target = SymbolConfig(item)

        self.assertEquals('IID', target.symbol())
        self.assertEquals('barchart', target.source())
