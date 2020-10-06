# 705 https://leetcode.com/problems/design-hashset/
class Bucket:
    def __init__(self):
        self.bucket = []
    
    def add(self, key):
        found = False
        for i, k in enumerate(self.bucket):
            if key == k:
                self.bucket[i] = key
                found = True
                break
        
        if not found:
            self.bucket.append(key)
    
    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if key == k:
                del self.bucket[i]
    
    def contains(self, key):
        for k in self.bucket:
            if key == k:
                return True
        return False
    
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 2096
        self.table = [Bucket() for _ in range(self.capacity)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash = key % self.capacity
        self.table[hash].add(key)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash = key % self.capacity
        self.table[hash].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash = key % self.capacity
        return self.table[hash].contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)