import unittest
import os
import os.path
from stock_scraper.config.symbolList import SymbolList 

class TestSymbolList(unittest.TestCase):

    def test_loading_file(self):
        testFolder = os.path.join(os.getcwd())

        symbolList = SymbolList(testFolder)

        self.assertEquals(2, symbolList.count())
