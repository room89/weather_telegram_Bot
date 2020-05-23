class SecDist:
    def __init__(self):
        self._items = dict()
        self._items['bot'] = {}
        self._items['bot']['token'] = ''

    def __getitem__(self, item):
        return self._items[item]


secdist = SecDist()
