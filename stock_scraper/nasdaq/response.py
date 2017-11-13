from security import Security
from decimal import Decimal

class Response():

    item_delimiter = "<*>"
    field_delimiter = "|"

    def __init__(self, response):
        symbols = response.split(self.item_delimiter)
        self.__items = list(filter(lambda x : x, symbols))

    def count(self):
        return len(self.__items)

    def __iter__(self):
        self.current = 0
        self.max = self.count()
        return self
    
    def next(self):
        if self.current < self.max:
            item = self.__items[self.current]

            self.current += 1
            return self.__getItemDict(item)
        else:
            raise StopIteration

    def __formatDecimal(self, value):
        number = value.strip('$').replace('&nbsp;','').strip('unch').strip('N/A').replace(',','').strip('NE').strip('%')

        if number:
            return Decimal(number)
        else:
            return Decimal(0)
    
    def __priceChange(self, change, direction):
        
        if direction == "down":
            change = change * -1

        return change
    
    def __getItemDict(self, item):
        fields = item.split(self.field_delimiter)

        return { 'symbol': fields[0]
               , 'name': fields[1]
               , 'exchange': fields[2]
               , 'url': fields[4]
               , 'price': self.__formatDecimal(fields[5])
               , 'volume': self.__formatDecimal(fields[6])
               , 'dayHigh': self.__formatDecimal(fields[7])
               , 'dayLow': self.__formatDecimal(fields[8])
               , 'yearHigh': self.__formatDecimal(fields[11])
               , 'yearLow': self.__formatDecimal(fields[12])
               , 'peRatio': self.__formatDecimal(fields[13])
               , 'earningsPerShare': self.__formatDecimal(fields[15])
               , 'openPrice': self.__formatDecimal(fields[16])
               , 'closePrice': self.__formatDecimal(fields[17])
               , 'openPriceDate': fields[18]
               , 'closePriceDate': fields[19]
               , 'marketCap': self.__formatDecimal(fields[20])
               , 'previousClosePrice': self.__formatDecimal(fields[21])
               , 'priceChange': self.__priceChange( self.__formatDecimal(fields[22]),
                                                    fields[24])
               , 'percentPriceChange': self.__formatDecimal(fields[23])
               , 'priceDirection': fields[24]
               , 'shareType': fields[25]
               , 'netChange': self.__formatDecimal(fields[46])
               }
