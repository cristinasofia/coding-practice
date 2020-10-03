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
- In-Order: Left, Root, Right

```python
# 94 https://leetcode.com/problems/binary-tree-inorder-traversal/
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
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
```

- Pre-Order: Root, Left, Right

```python
# 144 https://leetcode.com/problems/binary-tree-preorder-traversal/
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
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
```

- Post-Order: Left, Right, Root

```python
# 145 https://leetcode.com/problems/binary-tree-postorder-traversal/
def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

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