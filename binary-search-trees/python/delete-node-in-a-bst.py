# 450 https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Note: No parent attribute in node

BST = [5,3,6,2,4,null,7,1]

            5
          /    \
        3       6
      /   \       \
    2       4       7
  /
1

Hibbard's Algorithm:
Case 0. Delete 7
Case 1a. Delete 6
Case 1b. Delete 2
Case 2. Delete 3


"""
# Method: Hibbard's Algorithm
def deleteNode(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    
    def find_parent(node, val, p):
        if not node or node.val == val:
            return p
        if val < node.val:
            return find_parent(node.left, val, node)
        if val > node.val:
            return find_parent(node.right, val, node)

    
    def search(node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return search(node.left, val)
        if val > node.val:
            return search(node.right, val)
        
        
    # find node
    p = search(root, key)

    if not p:
        return root

    # case 0: p has no children
    if not p.left and not p.right:
        if p == root:
            root = None
            return root

        parent = find_parent(root, p.val, None)
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

        parent = find_parent(root, p.val, None)

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

        parent = find_parent(root, p.val, None)

        # link p's right child as p's parent child
        if parent.left == p:
            parent.left = p.left
        else:
            parent.right = p.left

        return root

    # case 2. node has two children
    # find successor of p
    # note: succ(p) has no left child
    if not p.right.left:

        # right node of p is the successor
        p.val = p.right.val
        p.right = p.right.right
        return root

    succ = p.right
    succParent = p

    # find successor node of p

    while succ.left:
        succParent = succ
        succ = succ.left

    p.val = succ.val
    succParent.left = succ.right

    return root