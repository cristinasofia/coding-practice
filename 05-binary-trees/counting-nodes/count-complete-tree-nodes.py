# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# COUNTING ALL NODES
def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    def helper(root):
        count = 1
        if root.left:
            count += helper(root.left)
        if root.right:
            count += helper(root.right)
        return count

    total = 0
    if root:
        total = helper(root)
    return total

# COUNTING LEAF NODES
def countLeafNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def helper(root):
        count = 0
        if not root.left and not root.right:    # is a leaf
            count = 1
        else:                                   # else, find leaf
            if root.left:
                count += helper(root.left)
            if root.right:
                count += helper(root.right)
        return count

    total = 0
    if root:
        total = helper(root)
    return total
    
# COUNTING INTERNAL NODES
def countInternalNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    

    def helper(root):
        count = 0
        if root.left or root.right:             # is an internal node
            count = 1                           # no else because the count will be 0 if root is a leaf
            if root.left:
                count += helper(root.left)
            if root.right:
                count += helper(root.right)
        return count

    total = 0
    if root:
        total = helper(root)
    return total