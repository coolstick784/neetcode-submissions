from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.ct = {}
        self.min_freq = 1
        self.keys = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            ct = self.keys[key][1]
            del self.ct[ct][key]

            if self.min_freq == ct and not self.ct[ct]:
                del self.ct[ct]
                self.min_freq += 1

            self.ct.setdefault(ct + 1, OrderedDict())[key] = True
            self.keys[key][1] += 1
            return self.keys[key][0]

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.keys:
            ct = self.keys[key][1]
            del self.ct[ct][key]

            if self.min_freq == ct and not self.ct[ct]:
                del self.ct[ct]
                self.min_freq += 1

            self.ct.setdefault(ct + 1, OrderedDict())[key] = True
            self.keys[key][1] += 1
            self.keys[key][0] = value

        else:
            if len(self.keys) == self.capacity:
                key_to_remove, _ = self.ct[self.min_freq].popitem(last=False)
                del self.keys[key_to_remove]

                if not self.ct[self.min_freq]:
                    del self.ct[self.min_freq]

            self.keys[key] = [value, 1]
            self.min_freq = 1
            self.ct.setdefault(1, OrderedDict())[key] = True