
class SymbolConfig():

    def __init__(self, data, folder):
        self.data = data.copy()
        self.folder = folder

        if 'symbol' not in data:
            raise Exception("No symbol was passed")

    def symbol(self):
        return self.data['symbol']

    def initialData(self):
        if 'initial-data' in self.data:
            return self.data['initial-data']
        else:
            return {}

    def source(self):
        if 'source' in self.data:
            return self.data['source']
        else:
            return "nasdaq"

    def folder(self):
        return self.folder

