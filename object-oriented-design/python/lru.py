# LRU Cache using Ordered Dict
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:             # if isn't found, ret -1
            return -1
        
        v = self.d.pop(key)               # move to end as LRU
        self.d[key] = v
        return v                          # then ret value
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:                 # if key is found
            self.d.pop(key)               # move to end as LRU
        self.d[key] = value               # update value
        
        if len(self.d) > self.capacity:   # if capacity exceeded
            self.d.popitem(last = False)  # pop item
            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)
