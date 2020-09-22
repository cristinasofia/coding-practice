# Stack
Linear structure: Last In First Out

```python
class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, x):
        self.s.append(x)
    
    def pop(self):  
        return self.s.pop()
    
    def top(self):
        return self.s[:-1]

```

# Queue
Linear structure: First In First Out

```python
class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self, x):       # adds item from right
        self.q.append(x)        # O(1)

    def dequeue(self, x):       # removes item from left
        return self.q.pop(0)    # O(1)
    
```

## Stack vs. Queue
- Implement stack using two queues:
```python
class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)
    
    def pop(self):
        while len(self.q1) > 1:
            x = self.q1.pop(0)
            self.q2.append(x)
        
        return self.q1.pop(0)
```

- Implement queue using two stacks:
```python
class Queue:
    
```