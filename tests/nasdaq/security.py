import unittest
from stock_scraper.nasdaq.security import Security
from decimal import Decimal

class TestSecurity(unittest.TestCase):

    def mock_data(self):
        return "IID|Voya International High Dividend Equity Income Fund|NYSE||www.ingfunds.com|$&nbsp;7.46|41,297|$&nbsp;7.46|$&nbsp;7.335|N/A|N/A|$&nbsp;7.94|$&nbsp;6.26|N/A|8,407|N/A|$&nbsp;7.39|N/A|Sep. 15, 2017|Sep. 15, 2017|$&nbsp;62,716.22|$&nbsp;7.37|0.09|1.22%|up|Common Shares of Beneficial Interest|Sep. 15, 2017&nbsp;Market Closed|N|||Y|IID|Dec. 31, 1969||||||||14|N||||C|7.46|0.09|1.22%|41,297|up|Y|$&nbsp;7.46|$&nbsp;7.335|N/A|N/A|N|N|0|8.47 %|0.000000|0.000000|Dec. 31, 1969|"

    def test_security(self):
        target = Security(self.mock_data())

        self.assertEquals("IID", target.symbol())
        self.assertEquals("NYSE", target.exchange())
        self.assertEqual(Decimal(".09"), target.priceChange())
