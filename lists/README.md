## Complexity

<table>
  <tbody>
    <tr>
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
      <td><a href="02-linked-lists">Linked List</a></td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
  </tbody>
</table>

## Fast and Slow
Fast pointer moves through same array at greater pace than slow.

```python
slow = arr[0]

for fast in range(arr):
    if slow condition:
        slow = slow.next # slow += 1
```

## Arrays vs. Linked Lists
- Array have a fixed size, and linked list have dynamic size.
- Array insertion and deletion is expensive, and linked lists are less expensive comparatively.
- Arrays allow random access, and linked lists do not.
- Arrays have better cache locality.
- Linked Lists required extra memory space for a pointer.

