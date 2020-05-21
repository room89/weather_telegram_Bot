class SecDist:
    def __init__(self):
        self._items = dict()
        self._items['bot'] = {}
        self._items['bot']['token'] = '1173660514:AAErTBQxrs-A2OEvmAPcI7UkI8fr_v0rpf4'

    def __getitem__(self, item):
        return self._items[item]


secdist = SecDist()
