from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.values = {}
        self.freq = {}
        self.groups = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        if key not in self.values:
            return -1

        self.update_freq(key)
        return self.values[key]

    def update_freq(self, key):
        f = self.freq[key]

        del self.groups[f][key]

        if not self.groups[f]:
            del self.groups[f]
            if self.min_freq == f:
                self.min_freq += 1

        self.freq[key] += 1
        self.groups[f + 1][key] = None

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.values:
            self.values[key] = value
            self.update_freq(key)
            return

        if len(self.values) == self.capacity:
            key_to_remove, _ = self.groups[self.min_freq].popitem(last=False)

            del self.values[key_to_remove]
            del self.freq[key_to_remove]

        self.values[key] = value
        self.freq[key] = 1
        self.groups[1][key] = None
        self.min_freq = 1