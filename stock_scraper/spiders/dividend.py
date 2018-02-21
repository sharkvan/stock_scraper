import scrapy
from decimal import Decimal
from datetime import datetime
from scrapy.exceptions import DropItem
from stock_scraper.items import Dividend, Dividends, Payment
from stock_scraper.config.symbolList import SymbolList
from stock_scraper.utils.files import getStock

class DividendSpider(scrapy.Spider):
    name = "dividend"
    allowed_domains = ["nasdaq.com"]
    
    DEFAULT_REQUEST_HEADERS = {
             'Accept-Encoding': 'gzip, deflate, sdch',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
             'Host': 'www.nasdaq.com',
             'Referer': 'https://www.nasdaq.com/',
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
             }

    def start_requests(self):
        symbolList = SymbolList(self.symbol)

        for symbolConfig in symbolList:
            yield scrapy.Request(
                    url = 'http://www.nasdaq.com/symbol/' + symbolConfig.symbol() + '/dividend-history', 
                    callback = self.parse,
                    meta = {'symbol': symbolConfig},
                    headers = self.DEFAULT_REQUEST_HEADERS)
   
    def getCalendarQuarter(self, datetime) :
        return (datetime.date().month // 3) + 1

    def parse(self, response):
        
        #price = Decimal(response.css('#qwidget_lastsale::text').extract_first().strip('$'))
        grid = grid = response.css('#quotes_content_left_dividendhistoryGrid')
        
        #payDates = []
        #today = datetime.now()

       # {symbol:"ticc",
       #  dividends: {
       #      "12/29/2017": {
       #             payDate:
       #             exDate:
       #             recDate:
       #             decDate:
       #             amount:
       #         }
       #      }
       #  }

        config = response.meta['symbol']
        for record in grid.css('tr'):
            if record.css('td span::text') :
                #try:
                    dividend = Dividend() 
                    dividend['symbol'] = config.symbol()
                    
                    payment = Payment()
                    payment['exDate'] = datetime.strptime(record.css('td span::text')[0].extract(), '%m/%d/%Y')
                    payment['payDate'] = datetime.strptime(record.css('td span::text')[4].extract(), '%m/%d/%Y')
                    payment['amount'] = Decimal(record.css('td span::text')[1].extract())

                    dividends = {}
                    dividends[payment['payDate'].strftime("%Y-%m-%d")] = payment

                    dividend['dividends'] = dividends

                    yield dividend

                #    payDates.append(dividend)
                #    if (dividend['payDate'] - today).days >= 365:
                #        break
                #except:
                #    print "Oh! error"
                #    continue

#        if payDates.count == 0:
#            return None 

        # Update this so that we collect the last years worth of dividends, first date - last date >= 365
        # We would want no more than 12 but as few as 1. Also make sure the last payment is within the
        # last 12 months. Now we can generate a trailing yield and a forward looking yield. The forward
        # looking yield should be 1 quarterly payment or the sum of 3 monthly payments, then multiplied by
        # 4. This should help to lower larger jumps in yields dues to abnormal monthly payments.
#        nextDivIndex = 0
#        for dividend in payDates:
#            exDate = dividend['exDate']
#            if exDate <= today :
#                break

#            if self.getCalendarQuarter(exDate) == self.getCalendarQuarter(today) :
#                break

#            nextDivIndex += 1

#        try:
#            item = payDates[nextDivIndex]

#            item['symbol'] = response.meta['symbol']
#            item['price'] = price
        
#            if (today - item['payDate']).days > 100 :
#                item['frequency'] = 'STP'
#                item['divYield'] = Decimal(0)
#                item['annualAmount'] = Decimal(0)
#            else:
#                delta = (item['payDate'] - payDates[nextDivIndex + 1]['payDate']).days
#                if delta < 50 :
#                    item['frequency'] = 'MTH'
#                    item['annualAmount'] = ((item['amount'] +
#                                      payDates[nextDivIndex+1]['amount'] +
#                                      payDates[nextDivIndex+2]['amount']) * 4 ) 
#                elif delta < 100 :
#                    item['frequency'] = 'QTR'
#                    item['annualAmount'] = (item['amount'] * 4)
#                elif delta < 215 :
#                    item['frequency'] = 'BIA'
#                    item['annualAmount'] = (item['amount'] * 2)
#                else:
#                    item['frequency'] = 'IR'
#                    item['annualAmount'] = 0

            #item['payDate'] = str(item['payDate'])
            #item['exDate'] = str(item['exDate'])
#            return item
#        except:
#            return None 
