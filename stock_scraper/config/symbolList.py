import json
import os.path
from symbolConfig import SymbolConfig

class SymbolList():

    def __init__(self, folder):
        self.folder = folder
        path = os.path.join(folder, "symbols.json")
        if os.path.exists(path):
            print "file is there"

        with open(path, 'r') as file:
            self.__items = json.load(file)

    def count(self):
        return len(self.__items['symbols'])

    def __iter__(self):
        self.current = 0
        self.max = self.count()
        return self

    def next(self):
        if self.current < self.max:
            item = self.__items['symbols'][self.current]
            self.current += 1

            return SymbolConfig(item, self.folder)
        else:
            raise StopIteration
