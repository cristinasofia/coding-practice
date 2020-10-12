# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 102 https://leetcode.com/problems/binary-tree-level-order-traversal/

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels
    
    def helper(node, l):
        if len(levels) == l:
            levels.append([])
            
        levels[l].append(node.val)
        
        if node.left:
            helper(node.left, l+1)
        if node.right:
            helper(node.right, l+1)
    
    helper(root, 0)
    return levels

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

def levelOrder2(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels
    
    def helper(node, l):
        if len(levels) == l:
            levels.append([])
            
        levels[l].append(node.val)
        
        if node.left:
            helper(node.left, l+1)
        if node.right:
            helper(node.right, l+1)
    
    helper(root, 0)
    return levels