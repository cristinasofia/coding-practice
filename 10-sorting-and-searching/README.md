# Sorting

<table class="table table-bordered table-striped">
    <tbody><tr>
      <th>Algorithm</th>
      <th colspan="2">Time</th>
      <th>Space</th>
      <th colspan ="2">Comparison</th>
    </tr>
    <tr>
      <th></th>
      <th>Average</th>
      <th>Worst</th>
      <th>Worst</th>
      <th>Pros</th>
      <th>Cons</th>
    </tr>
    <tr>
      <td>Bubble Sort</td>
      <td align="center" colspan="2" style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
      <td> </td>
      <td></td>
    </tr>
    <tr>
      <td>Selection Sort</td>
      <td align="center" colspan="2" style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
    <td>Insertion Sort</td>
    <td align="center" colspan="2" style="color:red">O(n^2)</td>
    <td style="color:green">O(1)</td>
    <td>Fastest for small inputs; Works in-place</td>
    <td></td>
    </tr>
    <tr>
    <td>Quicksort</td>
    <td style="color:orange">O(n log(n))</td>
    <td style="color:red">O(n^2)</td>
    <td style="color:#9acd32">O(log(n))</td>
    <td>Fast for most inputs; cache-friendly; Works best for elements that are close together</td>
    <td>Worst case O(n^2)</td>
    </tr>
    <tr>
    <td>Mergesort</td>
    <td align="center" colspan="2" style="color:orange">O(n log(n))</td>
    <td style="color:#CCCC00">O(n)</td>
    <td>Works best in huge datasets</td>
    <td>Takes up a lot of space</td>
    </tr>
    <tr>
    <td>Heapsort</td>
    <td align="center" colspan="2" style="color:orange">O(n log(n))</td>
    <td style="color:green">O(1)</td>
    <td>Guaranteed speed optimal O(nlogn); Needs less memory/works in-place O(1)</td>
    <td>Even if sorted still O(nlogn); Worse than Quicksort</td>
    </tr>
    <tr>
    <td>Radix Sort</td>
    <td align="center" colspan="2" style="color:green">O(nk)</td>
    <td style="color:#CCCC00">O(n+k)</td>
    <td></td>
    <td></td>
    </tr>

</tbody></table>

## Bubble Sort
1. Start at beginning of array
2. If first is greater than second: swap
3. Go on to next pair
4. Continue to sweep array until end

## Selection Sort
1. Linear search for smallest element. Swap with first element.
2. Linear search for second smallest. Swap with second element.
3. Repeat finding the next-smallest element, and swapping until the array is sorted.

```python
# adds sorted numbers to the right end of the array
def selectionsort(arr):
    n = len(arr)
    for i in reversed(range(n)):
        max_index = 0
        for j in range(1,i+1):
            if arr[j] > arr[max_index]:
                max_index = j

        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
```

## Insertion Sort
1. Picks one element of array
2. Finds location it belongs
3. Inserts in the array

```python
def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        moved = False
        placed = False
       
        for j in reversed(range(i)):

            if arr[j] > temp:
                # shift numbers until you find it's location
                arr[j+1] = arr[j]
                moved = True
            else:
                arr[j+1] = temp
                placed = True
                break
    
        # edge case
        if moved and not placed:
            arr[0] = temp
```
## Best: O(n)
If we're inserting 13 into the subarray [2, 3, 5, 7, 11], no element has to slide to the right. The element is less than every element to its left.
## Average/Worse: O(n^2)
If we're inserting 0 into the subarray [2, 3, 5, 7, 11], then every element in the subarray has to slide over one position to the right.

## Quicksort
1. Pick random element
2. Partition array such that all numbers on left of partitioned element are smaller, and all numbers to the right are bigger
3. Keep partitioning until sorted

```python
# method 1
def partition(l, r):
    low = l
    while l < r:
        if A[l] < A[r]:
            A[l], A[low] = A[low], A[l]
            low += 1
        l += 1
    A[r], A[low] = A[low], A[r]
    return low

def quickSort(l, r):
    pos = partition(l, r)
    if r > pos:                     
        quickSort(pos + 1, r)       # go right
    if l < pos:             
        quickSort(l, pos - 1)       # go left

# method 2

def quickSort(arr, l, r):
    if r-l <= 0:
        return
    
    m = (l+r) //2
    i, j = l, r
    
    while i <= j:
        while arr[i] < arr[m]:
            i += 1
        while arr[m] < arr[j]:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    quicksort(arr, l, i-1)
    quicksort(arr, i, r)

# quickSort(arr, 0, len(arr) - 1)
```
### Best/Average: O(nlogn)
Balanced partitions.
### Worst: O(n^2)
Partitioned element is not guaranteed to be the median or anywhere near the median, thus can be slow.

## Merge Sort
1. Divide and conquer

```python

def mergesort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        
        merge(arr, l, m, r)
        
def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    
    i, j, k = 0, 0, l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

       
#mergesort(arr, 0, len(arr) - 1)
```

## Heapsort

```python
def heapsort():
    for i in reversed(range(n/2 - 1)):
        heapify(n, i)
    
    for i in reversed(range(n - 1)):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

def heapify(n, i):
    largest = i
    l = (2*i) + 1
    r = (2*i) + 2
    
    # if left child is larger than root
    if l < n and arr[largest] < arr[l]:
        largest = l
    # if right child is larger than largest found
    if r < n and arr[largest] < arr[r]:
        largest = r
    # if largest element is not root
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(n, largest)


#heapsort()
```

## Radix Sort
1. Iterate through each digit of each number
2. Group numbers by digit

<span style="color:green">O(nk)</span> where n is the number of elements and k is the number of passes.

# Searching

## Binary Search

### Iterative
```python
# x is the target
l = 0
r = len(A) - 1

def binarySearch(l, r):
    while l <= r:
        m = (l + r)//2
        if A[m] == x:
            return m
        elif A[m] < x:
            l = m + 1
        else:
            r = m - 1

    return -1
```

### Recursive
```python
# x is the target
l = 0
r = len(A) - 1

def binarySearchRecursive(l, r):
    if l > r:
        return -1

    m = (l + r)//2
    if A[m] == x:
        return m
    elif A[m] < x:
        return binarySearchRecursive(m + 1, r)
    else:
        return binarySearchRecursive(l, m - 1)
```