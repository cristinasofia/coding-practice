# Binary Search Tree
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

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
      <td>Binary Search Tree</td>
      <td align="center" colspan="4" style="color:#9acd32">O(log(n))</td>
      <td align="center" colspan="5" style="color:#CCCC00">O(n)</td>
    </tr>
</tbody>
</table>

## Binary Search Tree Traversal
- In-Order: Retrieves keys in ascending order.
- Reverse in-order: Retrieves keys in descending order.
- Pre-Order: Topological sort, because a parent node is process before any of its child nodes.
- Post-Order

## Search

## Insert

## Delete


## BFS with Queue
Pop from left, then go left, then go right
```python
if not root:
    return False

q = [root]
while q:
    # pop left
    n = q.pop(0)
    if not n.left and not n.right:
        return True
    if n.left:
        # left conditions
        q.append(n.left)
    if n.right:
        # right conditions
        q.append(n.right)

return False
```
Good for:
- Validating a BST

## DFS Recursive
```python
res = []

def dfs(root):
    if root:
        if not root.left and not root.right:
            res.append(True)
        if root.left:
            dfs(root.left)
        if root.right:
            dfs(root.right)

dfs(root)
return res
```

## DFS with Stack
Pop from right, then go right, then go left
```python
if not root:
    return False

s = [root]
while s:
    # pop right
    n = s.pop()
    if not n.left and not n.right:
        return True
    if n.right:
        # right conditions
        s.append(n.right)
    if n.left:
        # left conditions
        s.append(n.left)

return False
```
Good for:
- Depth of binary tree
- Finding a path sum

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
        <td><a href="http://en.wikipedia.org/wiki/AVL_tree">AVL Tree</a></td>
        <td align="center" colspan="8" style="color:#9acd32">O(log(n))</td>
        <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Red-black_tree">Red-Black Tree</a></td>
      <td align="center" colspan="8" style="color:#9acd32">O(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</tbody>
</table>

## Balanced
### AVL
Stores in each node the height of the subtrees rooted at this node.
Check if height balanced: height of left subtree and height of right subtree differ by 1:
```
  balance(n) = n.left.height - n.right.height
```

**Inserts**
Upon insertion, balance might change to -2 or 2.
- If balance is 2: rotate Left, rotate Right
- If balance is -2: rotate Right, rotate Left

**Pros:** Frequent data lookup queries.
**Cons:** Frequent insertions and deletions.

### Red-Black Trees
1. Every node is red or black.
2. The root is black.
3. The leaves (NULL nodes) are black.
4. Every red node must have two black children (red node cannot have black children, nlack node can have black children).
5. Every path from node to its leaves must have the same number of black children.

**Pros:** Less memory, can rebalance faster (faster insertion/deletions), used in situations where tree will be modified frequently.
**Cons:** Lookups aren't as good as Hashtables.

### Minimum Spanning Trees
In a **weighted, connected, undirected graph**, a spanning tree is a tree that connects all the vertices. The minimum spanning tree is the spanning tree with minimum weight. There are various algorithms to do this.

### B-Trees
A self-balancing search tree (not a binary search tree) that is commonly used on disks or other storage devices. It is similar to a red-black tree, but uses fewer I/O operations.

### Interval Trees
An extension of a balanced binary search tree, but storing intervals (low -> high ranges) instead of simple values. A hotel could use this to store a list of all reservations and then effiCiently detect who is staying at the hotel at a particular time. 