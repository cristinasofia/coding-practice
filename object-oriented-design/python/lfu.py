from collections import OrderedDict
from collections import Counter

class LRUCache(object):
    
    def __init__(self, capacity):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.d:
            return -1
        
        v = self.d.pop(key)
        self.d[key] = v
        return v

    def put(self, key, value):
        if key in self.d:
            self.d.pop(key)
        self.d[key] = value
        
    def find_and_remove(self, keys):
        for k in self.d.keys():
            if k in keys:
                self.d.pop(k)
                return k
            
class LFUCache(LRUCache):

    def __init__(self, capacity):
        super(LFUCache, self).__init__(capacity)
        self.c = Counter()

    def get(self, key):
        found_key = super(LFUCache, self).get(key)
        if found_key != -1:
            self.c[key] += 1
            
        return found_key

    def put(self, key, value):
        
        if self.capacity == 0:
            return
        
        # if key in self.c, then key is being updated and not adding to capacity
        # and if the length of LRY will exceed capacity
        
        if key not in self.c and len(self.d) + 1 > self.capacity: # reaches capacity
            LFU = self.getLFU()

            if len(LFU) > 1: # tie, or more than one LFU
                # evict LRU
                k = super(LFUCache, self).find_and_remove(LFU)
                self.c.pop(k) # remove from LFUCache
            else:
                # invalidate LFU
                k = LFU[0]
                self.d.pop(k) # remove from LRUCache
                self.c.pop(k) # remove from LFUCache
        
        if key not in self.c:
            self.c[key] = 0
        else:
            self.c[key] += 1
            
        super(LFUCache, self).put(key,value)
    
    def getLFU(self):
        min_value = min(self.c.itervalues()) # find minimum frequency
        min_keys = [k for k in self.c if self.c[k] == min_value] # find all keys with minimum frequency
        return min_keys


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)