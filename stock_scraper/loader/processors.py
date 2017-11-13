from decimal import Decimal

class ToDecimal(object):
    def __call__(self, values):
        results = []

        for value in values:
            try:
                results.append(Decimal(value))
            except:
                results.append(Decimal(0))
