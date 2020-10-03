# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    
    s = [(root, 1)]
    max_depth = 1
    while s:
        n, v = s.pop()
        max_depth = max(max_depth, v)
        if n.right:
            s.append((n.right, v + 1))
        if n.left:
            s.append((n.left, v + 1))
    
    return max_depth

def maxDepth_recursive(root):

    def helper(root):
        l_count, r_count = 1, 1
        if root.left:
            l_count += helper(root.left)
        if root.right:
            r_count += helper(root.right)
        return max(l_count, r_count)

    
    total = 0
    if root:
        total = helper(root)
    return total