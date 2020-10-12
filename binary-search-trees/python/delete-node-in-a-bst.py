# 450 https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Note: No parent attribute in node

BST = [5,3,8,2,4,6,9,1,null,null,null,null,7]

            5
          /    \
        3         8
      /   \     /   \
    2      4   6       9
  /             \
1               7

Hibbard's Algorithm:
Case 0. Delete node with no children 
ex. Delete 7
Remove node from tree.

Case 1. Delete node with child
Case 1(a) Delete node with only right child 
ex. Delete 6
Remove node and replace with its child.

Case 1(b) Delete node with only left child 
ex. Delete 2
Remove node and replace with its child.

Case 2. Delete node with 2 children
Set "succ" node to right subtree

    (a) If succ has no left child
    ex. Delete 3
    4 has no left child, therefore 
    i. switch 3 and 4 values
    ii. assign 4's right tree as 3's right subtree

    (b) else
    ex. Delete 5
    i. Look for succ (6) and succ's parent (8)
    ii. switch 5 and 6 values
    iii. assign 6's right tree as 8's right subtree (7)

"""
# Method: Hibbard's Algorithm
def deleteNode(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
        
    # find node and its parent
    p = root
    parent = root

    while p:
        if p.val == key:
            break
        elif key < p.val:
            parent = p
            p = p.left
        else: # key > p.val
            parent = p
            p = p.right

    # not found, return BST
    if not p:
        return root

    # case 0: p has no children
    if not p.left and not p.right:
        if p == root:
            root = None
            return root

        # delete p from p's parent
        if parent.left == p:
            parent.left = None
        else:
            parent.right = None

        return root

    # case 1a. p has (1) right child
    if not p.left:
        if p == root:
            root = root.right
            return root

        # link p's right child as p's parent child
        if parent.left == p:
            parent.left = p.right
        else:
            parent.right = p.right

        return root

    # case 1b. p has (1) left child
    if not p.right:
        if p == root:
            root = root.left
            return root

        # link p's right child as p's parent child
        if parent.left == p:
            parent.left = p.left
        else:
            parent.right = p.left

        return root

    # case 2. node has two children
    succ = p.right
    if not succ.left: # successor of p has no left child
        p.val = succ.val # p replaced by successor
        p.right = succ.right # p's right subtree is replaced by succ's right subtree
    else: # find successor of p
        succParent = p # track successor parent
        while succ.left:
            succParent = succ
            succ = succ.left
            
        p.val = succ.val # p replaced by successor
        succParent.left = succ.right # successor parent's left subtree is replaced by successor's right subtree

    return root