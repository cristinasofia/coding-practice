## Complexity
- Accessing an element is **O(1)** constant because of indexing.
- Searching, insertion, and deletion is **O(n)** because it involves going through all elements of the array.

- Python
  - **O(1)**: Get/set an element, and append
  - **O(n)**: Copy, insert, delete, x in s
   
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
      <td style="color:green">Θ(1)</td>
      <td colspan = "3" style="color:#CCCC00">Θ(n)</td>
      <td style="color:green">O(1)</td>
      <td colspan = "3" style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</tbody></table>

## Sliding Window
Start grows in inner loop and end grows in outer loop. <br>
Counter used for problem specification. <br>
```python
    start, end = 0, 0
    dict = {}
    count = 0

    while end < len(arr):
    
    dict[end] += 1
    if dict[end] :
        count += 1

    end += 1
    
    while count :
        # update result if finding min
        min_len = min(min_len, end – start + 1)
        
        dict[start] -= 1
        if dict[start] :
        count -= 1

        start += 1

    # update result if finding maximum
    max_len = max(max_len, end – start)
```
[1](/01-arrays-and-strings/sliding-window/fruit-into-baskets.py)
[2](/01-arrays-and-strings/sliding-window/longest-repeating-character-replacement.py)
[3](/01-arrays-and-strings/sliding-window/longest-substring-with-at-most-two-distinct-characters.py)

## Fast and Slow
Fast pointer moves through same array at greater pace than slow.
```python
    slow = arr[0]

    for fast in range(arr):
    if slow condition:
        slow = slow.next # slow += 1
```

[Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)<br>
[Remove N-th Node](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)<br>

## Old and New State Pointers
1.	Calculate current result based on old state value (compare).
2.	Before assigning current result, store old state value into new state.
3.	Now current state proceed as new state.
```python
    last, now = 0, 0

    for i in arr:
    last, now = now, max(last + i, now)

    return now
```

[Fib](https://leetcode.com/problems/fibonacci-number/)<br>
[House Robber](https://leetcode.com/problems/house-robber/)<br>
[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)<br>
[Decode Ways](https://leetcode.com/problems/decode-ways/ )<br>

## Left and Right Pointers
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

[Two Sum](https://leetcode.com/problems/two-sum/)<br>
[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)

## Two Pointers
Each pointer moves independently.
```python
    p1, p2 = 0, 0

    while p1 < len(arr1) and p2 < len(arr2):
    if arr1 condition:
        p1 += 1
    if arr2 condition:
        p2 += 1
```

[Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

## K-th Problems
1. By sorting
```python
nums.sort(key = lambda x: x)
return nums[:K]
```    
2. By minheap
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