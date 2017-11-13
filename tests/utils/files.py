import unittest
import os
import os.path
from stock_scraper.utils.files import getStock

class TestUtilsFiles(unittest.TestCase):

    def test_loading_new_stock(self):
        stock = getStock("ABC", {}, os.path.join(os.getcwd(), "results"))
        self.assertIsNotNone(stock)
        self.assertEqual(stock['symbol'], "ABC")

    def test_loading_existing_stock(self):
        initialData = {'frequency':'mth'}
        stock = getStock("IID", initialData, os.path.join(os.getcwd(), "results"))

        self.assertIsNotNone(stock)
        self.assertEqual(stock['symbol'], "IID")
        self.assertEqual(stock['frequency'], "mth")
        self.assertEqual(stock['price'], "7.56")
    
