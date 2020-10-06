#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    
    q = [root]
    while q:
        n = q.pop(0)
        if n.left:
            if n.val <= n.left.val:
                return False
            q.append(n.left)
        if n.right:
            if n.val >= n.right.val:
                return False
            q.append(n.right)
    
    return True