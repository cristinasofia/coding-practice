# Binary Trees

## Tree
- Each tree has a root node
- Root node has 0 or more child nodes
- Each child node has zero (called a leaf) or more child nodes

## Binary Tree
- Each node has up to 2 children

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

## Binary Tree Traversal
### In-Order: Left, Root, Right
```python
# 94 https://leetcode.com/problems/binary-tree-inorder-traversal/

def inorder_iterative(self, root):

    res = []
    if not root:
        return res
    
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        res.append(root.val)
        root = root.right
    
    return res

def inorder_recursive_(self, root):

    def inorder(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    return inorder(root)
```

### Pre-Order: Root, Left, Right
```python
# 144 https://leetcode.com/problems/binary-tree-preorder-traversal/

def preorder_iterative(self, root):

    res = []
    if not root:
        return res
    
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    
    return res

def preorder_recursive(self, root):

    def preorder(root):
        return [root.val] + preorder(root.left) + preorder(root.right) if root else []
    return preorder(root)
```

### Post-Order: Left, Right, Root
```python
# 145 https://leetcode.com/problems/binary-tree-postorder-traversal/

def postorder_iterative_(self, root):

    res = []
    if not root:
        return res
    
    stack = [root]
    while stack:
        root = stack.pop()
        res = [root.val] + res
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    
    return res

def postorder_recursive(self, root):

    def postorder(root):
        return postorder(root.left) + postorder(root.right) + [root.val] if root else []
    return postorder(root)
```

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

## DFS
### Recursive
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

### Iterative (Stack)
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

### Post Order
1. Visit the children
2. Visit myself

Traverses tree in post-order:
        1
      /   \
    2       3
  /   \
4       5

Path: 4, 5, 2, 3, 1

Example:
Count and return the number of nodes where its value is greater than or equal to the values of all of its descendants.

1. 4 compared to null and null
   - If 4 is the max, answer increases by 1
   - Return the max of the subtree
2. 5 compared to null and null
3. 2 compared to 4's and 5's subtree maximums
4. 3 compared to null and null
5. 1 compared to 2's and 3's subtree maximums

```python
ans = []

def helper(root):
    if not root:
        return 0
    
    l = helper(root.left)
    r = helper(root.right)
    
    path = # addition/comparison between root, left and right children
    
    ans.append(path)
    # ans.append(1) if counting
        
    return # comparison between root, left and right children
            # to be compared by the parent of the root

helper(root)
return # max/sum(ans)
```

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