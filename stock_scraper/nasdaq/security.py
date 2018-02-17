from decimal import Decimal

# Sample security string
#    WHLR|
#    Wheeler Real Estate Investment Trust, Inc.|
#    NASDAQ-CM|
#    |
#    http://www.whlr.us|
#    $&nbsp;10.27|
#    32,531|
#    $&nbsp;10.28|
#    $&nbsp;9.99|
#    N/A|
#    N/A|
#    $&nbsp;15.28|
#    $&nbsp;7.95|
#    NE|
#    8,673|
#    $&nbsp;-1.83|
#    $&nbsp;10.17|
#    $&nbsp;10.29|
#    Aug. 30, 2017|
#    Aug. 30, 2017|
#    $&nbsp;89,071.71|
#    $&nbsp;10.15|
#    0.12|
#    1.18%|
#    up|
#    Common Stock Real Estate Investment Trust|
#    Aug. 30, 2017&nbsp;Market Closed|
#    N|
#    |
#    |
#    N|
#    WHLR|
#    Dec. 31, 1969|
#    |
#    |
#    |
#    |
#    |
#    |
#    Y|
#    17|
#    N|
#    |
#    |
#    |
#    C|
#    10.27|
#    0.12|
#    1.18%|
#    32,531|
#    up|
#    N|
#    $&nbsp;10.28|
#    $&nbsp;9.99|
#    N/A|
#    N/A|
#    N|
#    N|
#    -0.44|
#    13.4 %|
#    0.000000|
#    0.000000|
#    Dec. 31, 1969|
#
#0 - Symbol
#1 - Security Name
#2 - Exchange
#3 - 
#4 - Security Url
#5 - Price
#6 - Volume
#7 - Day High
#8 - Day Low
#9 - 
#10 - 
#11 - 52 wk High
#12 - 52 wk Low
#13 - P/E Ratio
#14 - 
#15 - Earnings Per Share
#16 - Open Price
#17 - Close Price
#18 - Open Price Date
#19 - Close Price Date
#20 - Market Cap
#21 - Previous Close Price
#22 - Price Change
#23 - Percent Price Change
#24 - Price Direction
#25 - Share Type
#26 - 
#27 - 
#28 - 
#29 -
#30 -
#31 - Symbol
#
#46 - Net Change

class Security():
    
    def __init__(self, securityData):
        self.data = securityData.split(self.__delimiter())

    def __delimiter(self):
        return "|"

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
    
    def symbol(self):
        return self.data[0] #0 - Symbol

    def name(self):
        return self.data[1] #1 - Security Name

    def exchange(self):
        return self.data[2] #2 - Exchange

#3 - 

    def url(self):
        return self.data[4] #4 - Security Url

    def price(self): 
        return self.__formatDecimal(self.data[5]) #5 - Price

    def volume(self):
        return self.__formatDecimal(self.data[6]) #6 - Volume

    def dayHigh(self):
        return self.__formatDecimal(self.data[7]) #7 - Day High

    def dayLow(self):
        return self.__formatDecimal(self.data[8]) #8 - Day Low

#9 - 
#10 - 

    def yearHigh(self):
        return self.__formatDecimal(self.data[11]) #11 - 52 wk High

    def yearLow(self):
        return self.__formatDecimal(self.data[12]) #12 - 52 wk Low

    def peRatio(self):
        return self.__formatDecimal(self.data[13]) #13 - P/E Ratio

#14 - 

    def earningsPerShare(self):
        return self.__formatDecimal(self.data[15]) #15 - Earnings Per Share

    def openPrice(self):
        return self.__formatDecimal(self.data[16]) #16 - Open Price

    def closePrice(self):
        return self.__formatDecimal(self.data[17]) #17 - Close Price
    
    def openPriceDate(self):
        return self.data[18] #18 - Open Price Date

    def closePriceDate(self):
        return self.data[19] #19 - Close Price Date

    def marketCap(self):
        return self.__formatDecimal(self.data[20]) #20 - Market Cap

    def previousClosePrice(self):
        return self.__formatDecimal(self.data[21]) #21 - Previous Close Price

    def priceChange(self):
        return self.__priceChange( self.__formatDecimal(self.data[22]), self.priceDirection()) #22 - Price Change

    def percentPriceChange(self):
        return self.__formatDecimal(self.data[23]) #23 - Percent Price Change

    def priceDirection(self):
        return self.data[24] #24 - Price Direction

    def shareType(self):
        return self.data[25] #25 - Share Type
#26 - 
#27 - 
#28 - 
#29 -
#30 -
#31 - Symbol
#
    def netChange(self):
        return self.__formatDecimal(self.data[46]) #46 - Net Change

