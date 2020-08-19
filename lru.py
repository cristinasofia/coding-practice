class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # initialize
        self.capacity = capacity
        # dictionary of key = node.key and values = nodes
        self.cache = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add(self, node):
        # add node at end of dll
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove(self, node):
        # delete node from anywhere in dll
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # move key to end (most recently used)
        if key in self.cache:
            self._remove(self.cache[key])
        n = Node(key, value)
        self._add(n)
        self.cache[key] = n
        # check if cache has exceeded capacity
        # then pop least recently used
        if len(self.cache) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.cache[n.key]

    def get(self, key):
        # O(1) time
        # retutn -1 if key isn't found 
        if key not in self.cache:
            return -1
        # if found, then move key to end (most recently used)
        n = self.cache[key]
        self._remove(n)
        self._add(n)
        # return value of key
        return n.value

        
def main():
    capacity = 4
    obj = LRUCache(capacity)
    obj.put(45,1)
    print(obj.cache.keys())
    obj.put(32,2)
    print(obj.cache.keys())
    obj.put(28,3)
    print(obj.cache.keys())
    obj.put(34,4)
    print(obj.cache.keys())
    obj.put(17,5)
    print(obj.cache.keys())

if __name__ == "__main__":
    main()