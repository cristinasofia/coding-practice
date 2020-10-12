## Hash Functions
1. Should efficiently compute.
2. Should uniformly distribute the keys.
   
### Hashing Methods 
1. Mod hashing
```
hash_value = key % table_size
```
```python
# string hash function example
def hash_func(key):
    for k in key:
        hash_val = 37 * hash_val + k
    
    return hash_val % table_size
```
2. Multiplicative hashing
```python
# hash_func(key) = floor((a * key * mod 2^w)/(2^(w-m))) = ((k * a) & (1<<m) - 1) >> w
# where a is a random odd number
# m is the length of bits of output/table size 
# w is the size of the machine word (32 bits)
def hash_func(key):    
    return ((key*1031237) & (1<<20) - 1)>>5
```

## Hash Set Implementation
```python
class Bucket:
    def __init__(self):
        self.bucket = []
    
    def add(self, key):
        if key not in self.bucket:
            self.bucket.append(key)
    
    def remove(self, key):
        if key in self.bucket:
            self.bucket.remove(key)
    
    def contains(self, key):
        return key in self.bucket
    
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
        
```