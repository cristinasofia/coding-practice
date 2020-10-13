#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    ans = []
    def helper(root):
        
        if not root:
            return 0
        
        l = max(helper(root.left), 0)
        r = max(helper(root.right), 0)
        
        path = root.val + l + r
        
        ans.append(path)
        
        return root.val + max(l, r)

    helper(root)

    return max(ans)