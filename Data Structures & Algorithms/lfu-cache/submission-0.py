class LFUCache:

    def __init__(self, capacity: int):
        self.ct = {} # each has a ordered dict
        self.min = 1
        self.keys = {}# key : [value, ct]
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            ct = self.keys[key][1]
            del self.ct[ct][key]
        
            if self.min == ct and not self.ct[ct]:
                del self.ct[ct]
                self.min += 1
            
            self.ct.setdefault(ct+1, OrderedDict())[key] = True
            self.keys[key][1] += 1
            return self.keys[key][0]
        return -1 
        

    def put(self, key: int, value: int) -> None:

        if key in self.keys:
            ct = self.keys[key][1]
            del self.ct[ct][key]
        
            if self.min == ct and not self.ct[ct]:
                self.min += 1
            
            self.ct.setdefault(ct+1, OrderedDict())[key] = True
            self.keys[key][1] += 1
            self.keys[key][0] = value
        else:
            if len(self.keys) == self.capacity:
                
                key_to_remove, _ = self.ct[self.min].popitem(last=False)
                del self.keys[key_to_remove]
                if not self.ct[self.min]:
                    self.min += 1
        
            self.keys[key] = [value, 1]
            self.min = min(self.min, 1)
            self.ct.setdefault(1, OrderedDict())[key] = True

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)