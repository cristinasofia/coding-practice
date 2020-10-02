# Trees

## Tree
- Each tree has a root node
- Root node has 0 or more child nodes
- Each child node has zero (called a leaf) or more child nodes

## Binary Tree
- Each node has up to 2 children

## Binary Search Tree
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
      <td><a href="http://en.wikipedia.org/wiki/Binary_search_tree">Binary Search Tree</a></td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</tbody>
</table>

## Balanced
### AVL
Stores in each node the height of the subtrees rooted at this node. <br>
Check if height balanced: height of left subtree and height of right subtree differ by 1:<br>
```
  balance(n) = n.left.height - n.right.height
```

**Inserts** <br>
Upon insertion, balance might change to -2 or 2. <br>
- If balance is 2: rotate Left, rotate Right
- If balance is -2: rotate Right, rotate Left
<br>

**Pros:** Frequent data lookup queries <br>
**Cons:** Frequent insertions and deletions <br>

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
        <td><a href="http://en.wikipedia.org/wiki/AVL_tree">AVL Tree</a></td>
        <td style="color:#9acd32">Θ(log(n))</td>
        <td style="color:#9acd32">Θ(log(n))</td>
        <td style="color:#9acd32">Θ(log(n))</td>
        <td style="color:#9acd32">Θ(log(n))</td>
        <td style="color:#9acd32">O(log(n))</td>
        <td style="color:#9acd32">O(log(n))</td>
        <td style="color:#9acd32">O(log(n))</td>
        <td style="color:#9acd32">O(log(n))</td>
        <td style="color:#CCCC00">O(n)</td>
        </tr>
    </tbody>
</table>

### Red-Black Trees
1. Every node is red or black.
2. The root is black.
3. The leaves (NULL nodes) are black.
4. Every red node must have two black children (red node cannot have black children, nlack node can have black children).
5. Every path from node to its leaves must have the same number of black children.

**Pros:** Less memory, can rebalance faster (faster insertion/deletions), used in situations where tree will be modified frequently <br>
**Cons:** Lookups aren't as good as Hashtables <br>
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
      <td><a href="http://en.wikipedia.org/wiki/Red-black_tree">Red-Black Tree</a></td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</tbody></table>


## Complete Binary Tree
- Every level of tree is filled, except for perhaps the last level.
- Filled form left to right.

## Full Binary Tree
- Every node has either 0 or 2 children (no node has only 1 child).

## Perfect Binary Tree
- Both **complete** and **full**.
- All leaf nodes will be at the same level. This level will be the maximum number of nodes.
- Number of nodes where k is the number of levels:
$$2^k - 1 $$

## Traversal
- In-Order: Left, Root, Right
- Pre-Order: Root, Left, Right
- Post-Order: Left, Right, Root


```python
def hasPathSum1(self, root, sum):
    res = []
    self.dfs(root, sum, res)
    return any(res)
    
def dfs(self, root, target, res):
    if root:
        if not root.left and not root.right and root.val == target:
            res.append(True)
        if root.left:
            self.dfs(root.left, target-root.val, res)
        if root.right:
            self.dfs(root.right, target-root.val, res)

# DFS with stack
def hasPathSum2(self, root, sum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == sum:
            return True
        if curr.right:
            stack.append((curr.right, val+curr.right.val))
        if curr.left:
            stack.append((curr.left, val+curr.left.val))
    return False
    
# BFS with queue
def hasPathSum(self, root, sum):
    if not root:
        return False
    queue = [(root, sum-root.val)]
    while queue:
        curr, val = queue.pop(0)
        if not curr.left and not curr.right and val == 0:
            return True
        if curr.left:
            queue.append((curr.left, val-curr.left.val))
        if curr.right:
            queue.append((curr.right, val-curr.right.val))
    return False
```

## Traversing Nodes
```python
    while node:
        if current node > target node:
            go left
        if current node < target node:
            go right
```
Good for:
- Lowest common ancestor of binary search tree
- Inorder successor

## Counting Nodes
```python
    def helper(root):
        # identify here if we are searching for all nodes, internal, leaves, etc. 
        count = 1

        # visit left then right
        if root.left:
            count += helper(root.left)
        if root.right:
            count += helper(root.right)
        return count

    
    total = 0
    if root:
        total = helper(root)
    return total
```

## BFS with Queue
Pop from left, then go left, then go right
```python
    if not root:
        return True
    
    q = [root]
    while q:
        # pop left
        n = q.pop(0)
        if n.left:
            # left conditions
            q.append(n.left)
        if n.right:
            # right conditions
            q.append(n.right)
    
    return True
```
Good for:
- Validating a BST

## DFS with Stack
Pop from right, then go right, then go left
```python
    if not root:
        return True
    
    s = [root]
    while s:
        # pop right
        n = s.pop()
        if n.right:
            # right conditions
            s.append(n.right)
        if n.left:
            # leftt conditions
            s.append(n.leftt)
    
    return True
```
Good for:
- Depth of binary tree
- Finding a path sum

### Minimum Spanning Trees
In a weighted, connected, undirected graph, a spanning tree is a tree that connects all the vertices. The minimum spanning tree is the spanning tree with minimum weight. There are various algorithms to do this.
### B-Trees
A self-balancing search tree (not a binary search tree) that is commonly used on disks or other storage devices. It is similar to a red-black tree, but uses fewer I/O operations.

### Interval Trees
An extension of a balanced binary search tree, but storing intervals (low -> high ranges) instead of simple values. A hotel could use this to store a list of all reservations and then effiCiently detect who is staying at the hotel at a particular time. 