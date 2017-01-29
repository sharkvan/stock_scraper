import scrapy
from datetime import datetime
from stock_scraper.items import Stock, StockLoader

class DividendSpider(scrapy.Spider):
    name = "dividend"
    allowed_domains = ["nasdaq.com"]

    def __init__(self, category=None, *args, **kwargs):
        super(DividendSpider, self).__init__(*args, **kwargs)
        self.qrtMth = lambda: None
        setattr(self, 'qrtMth', [1,2,3,1,2,3,1,2,3,1,2,3])

    def start_requests(self):
        yield scrapy.Request(url='http://www.nasdaq.com/symbol/' + self.symbol + '/dividend-history')
    
    def parse(self, response):
        stockLoader = StockLoader()
        stock = stockLoader.load(self.filePath) 
        
        grid = grid = response.css('#quotes_content_left_dividendhistoryGrid')
        headers = grid.css('th a::text')
        
        for record in grid.css('tr'):
            if record.css('td span::text') :
                stock['symbol'] = self.symbol

                exDate = datetime.strptime(record.css('td span::text')[0].extract(), '%m/%d/%Y')
                payDate = datetime.strptime(record.css('td span::text')[4].extract(), '%m/%d/%Y')

                stock['dividendExDate'] = exDate 
                #Cash Amount
                stock['dividendAmount'] = record.css('td span::text')[1].extract()
                #Payment Date
                stock['dividendPayDate'] = payDate
                stock['dividendPayQtrMonth'] = self.qrtMth[payDate.month-1]
                break

        payDates = []
        
        for record in grid.css('tr'):
            if record.css('td span::text'):
                payDates.append(datetime.strptime(record.css('td span::text')[4].extract(), '%m/%d/%Y'))
                if 4 == len(payDates):
                    break

        delta = (payDates[0] - payDates[1]).days
        if (payDates[0] - datetime.now()).days > 100 :
            stock['dividendFrequency'] = 'STP'
        elif delta < 50 :
            stock['dividendFrequency'] = 'MTH'
        elif delta < 100 :
            stock['dividendFrequency'] = 'QTR'
        elif delta < 215 :
            stock['dividendFrequency'] = 'BIA'
        else:
            stock['dividendFrequency'] = 'IR'
       
        return stock
