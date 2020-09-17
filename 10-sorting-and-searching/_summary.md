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
1. Linear search for smallest element
2. Move it to front (swap)
3. Linear search for second smallest
4. Swap
5. Continue until all elements are in place

## Insertion Sort

## Quicksort
1. Pick random element
2. Partition array such that all numbers on left of partitioned element are smaller, and all numbers to the right are bigger
3. Keep partitioning until sorted

<span style="color:red">O(n^2)</span> Partitioned element is not guaranteed to be the median or anywhere near the median, thus can be slow.
```python
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
```

## Merge Sort
1. Divide and conquer

## Heapsort

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