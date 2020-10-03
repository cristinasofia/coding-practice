## Complexity

<table>
    <tbody><tr>
      <th>Data Structure</th>
      <th colspan="8">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="4">Average</th>
      <th colspan="4">Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <th></th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th></th>
    </tr>
    <tr>
      <td>Stack</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td>Queue</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</table>

## Stack
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

## Queue
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

### Stack vs. Queue
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