# Arrays

## Libraries
### Python
- Instantiating an array methods
  - ``` arr = [0] * 11```
  - ``` arr = [0 for _ in range(11)]```
  - ``` arr = list(range(11)) ```
- Basic operations: ```len(arr), arr.append(x), arr.remove(x), a.insert(i, x)```
- Copy
  - ```arr2 = arr1 ``` vs. ```arr2 = list(arr1) ```
  - ```copy.copy(arr)``` vs. ```copy.deepcopy(arr) ```
- Methods
  - min(A), max(A), 
  - binary search for sorted lists: bisect.bisect(arr,6), bisect.bisect-left(arr,6), bisect.bisect_right(arr,6)
  - A.reverse() (in-place), reversed(A) (returns an iterator)
  - A.sor() (in-place), sorted(A) (returns a copy)
  - del A[i] (deletes the i-th element), del A[i:j] (removes the slice)
- Slicing: 
  - Let A = [1, 6, 3, 4, 5, 2, 7].
    - A[2:4] is [3, 4]
    - A[2:] is [3, 4, 5, 2, 7]
    - A[:4] is [1, 6, 3, 4)
    - A[:-1] is [1, 6, 3, 4, 5, 2]
    - A[-3:] is [5, 2, 7]
    - A[-3:-1] is [5, 2]
    - A[1:5:2] is [6, 4]
    - A[5:1:-2] is [2, 4]
    - A[::-1] is [7, 2, 5, 4, 3, 6, 1] (reverses list)
  - Rotate a list: A[k:] + A[:k] rotates A by k to the left.
  - Create a copy: B = A[:] (shallow copy of A into B)
- Loops
  - [x**2 for x in range(6)] is [0, 1, 4, 9, 16, 25]
  - [x**2 for x in range(6) if x%2 == 0] is [0, 4, 16]
  - If A = [1, 3, 5] and B = ['d', 'b'], then [(x, y) for x in A for y in B] is [(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]
  - 2D to 1D list: if M = [['a', 'b', 'c'], ['d', 'e','f']], x for row in M for x in row is ['a', 'b', 'c', 'd', 'e', 'f ']
  - If A = [[1, 2, 3], [4, 5, 6]] then [[x**2 for x in row] for row in M] is [[1, 4, 9], [16, 25, 36]]


### Complexity
- Accessing an element is **O(1)** constant because of indexing.
- Searching, insertion, and deletion is **O(n)** because it involves going through all elements of the array.
   
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
      <td>Array</td>
      <td align="center" style="color:green">O(1)</td>
      <td align="center" colspan = "3" style="color:#CCCC00">O(n)</td>
      <td align="center" style="color:green">O(1)</td>
      <td align="center" colspan = "3" style="color:#CCCC00">O(n)</td>
      <td align="center" style="color:#CCCC00">O(n)</td>
    </tr>
</tbody></table>

## Techniques
### Sliding Window
1. Start grows in inner loop and end grows in outer loop.
2. Counter used for problem specification.

```python
start, end = 0, 0
d = {}
count = 0

while end < len(arr):

    d[end] += 1
    if d[end] :
        count += 1

    end += 1

    while count :
        # update result if finding min
        min_len = min(min_len, end – start + 1)
        
        d[start] -= 1
        if d[start] :
            count -= 1

        start += 1

# update result if finding maximum
max_len = max(max_len, end – start)
```

### Old and New State Pointers
1.	Calculate current result based on old state value (compare).
2.	Before assigning current result, store old state value into new state.
3.	Now current state proceed as new state.

```python
last, now = 0, 0

for i in arr:
    last, now = now, max(last + i, now)

return now
```

### Left and Right Pointers
1.	One pointer on beginning (left), one pointer on end (right)
2.	Move toward each other until meet in middle
```python
    l, r = 0, len(arr) – 1

    while l < r:
    if left condition:
        l += 1
    if right condtion:
        r -= 1
```

### Two Pointers
Each pointer moves independently.
```python
    p1, p2 = 0, 0

    while p1 < len(arr1) and p2 < len(arr2):
    if arr1 condition:
        p1 += 1
    if arr2 condition:
        p2 += 1
```

### K-th Problems
1. By sorting
```python
nums.sort(key = lambda x: x)
return nums[:K]
```    

1. By minheap
```python
import heapq
# returns K smallest elements
return heapq.nsmallest(K, nums, key=lambda x: x)
# return K largest elements 
return heapq.nlargest(K, nums, key=lambda x: x) 
```

3. By quickselect
```python  
def by_quickselect(self, points, K):
  
    def partition(l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        
        nums[r], nums[low] = nums[low], nums[r]
        return low
        
    def select(l, r):
        
        pos = partition(l, r)
        if K > pos:
            # go right
            return select(pos+1,r)
        elif K < pos:
            # go left
            return select(l, pos-1)
        else:
            return nums[pos]
        
        
    return select(0, len(points)-1)
```
