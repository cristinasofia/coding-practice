# LRU Cache using Ordered Dict
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:             # if isn't found, ret -1
            return -1
        
        self.move_to_end(key)           # move to end as LRU
        return self[key]                # then ret value
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:                 # if key is found
            self.move_to_end(key)       # move to end as LRU
        self[key] = value               # update value
        
        if len(self) > self.capacity:   # if capacity exceeded
            self.popitem(last = False)  # pop item
            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)