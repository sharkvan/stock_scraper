import unittest
from stock_scraper.nasdaq.response import Response

class TestNasdaqResponseParse(unittest.TestCase):

    def mock_response(self):
        return "<*>IID|Voya International High Dividend Equity Income Fund|NYSE||www.ingfunds.com|$&nbsp;7.46|41,297|$&nbsp;7.46|$&nbsp;7.335|N/A|N/A|$&nbsp;7.94|$&nbsp;6.26|N/A|8,407|N/A|$&nbsp;7.39|N/A|Sep. 15, 2017|Sep. 15, 2017|$&nbsp;62,716.22|$&nbsp;7.37|0.09|1.22%|up|Common Shares of Beneficial Interest|Sep. 15, 2017&nbsp;Market Closed|N|||Y|IID|Dec. 31, 1969||||||||14|N||||C|7.46|0.09|1.22%|41,297|up|Y|$&nbsp;7.46|$&nbsp;7.335|N/A|N/A|N|N|0|8.47 %|0.000000|0.000000|Dec. 31, 1969|<*>WHLR|Wheeler Real Estate Investment Trust, Inc.|NASDAQ-CM||http://www.whlr.us|$&nbsp;11.36|15,319|$&nbsp;11.64|$&nbsp;11.30|N/A|N/A|$&nbsp;14.76|$&nbsp;7.95|NE|8,673|$&nbsp;-1.83|$&nbsp;11.30|$&nbsp;11.22|Sep. 15, 2017|Sep. 15, 2017|$&nbsp;98,525.28|$&nbsp;11.22|0.14|1.25%|up|Common Stock Real Estate Investment Trust|Sep. 15, 2017&nbsp;Market Closed|N|||N|WHLR|Dec. 31, 1969||||||||17|N||||C|11.36|0.14|1.25%|15,319|up|N|$&nbsp;11.64|$&nbsp;11.30|N/A|N/A|N|N|-0.17|12.12 %|0.000000|0.000000|Dec. 31, 1969|"

    def test_response_with_two_items(self):
        target = Response(self.mock_response())

        self.assertTrue(target.count() == 2, 'The response has %s items' % (target.count()))

