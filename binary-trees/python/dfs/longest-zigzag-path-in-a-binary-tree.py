# 1372 https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

def longestZigZag(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    if not root:
        return 0
    
    res = []
    
    def helper(root, is_right):
        
        if not root:
            return 0
        
        l = helper(root.left, False)
        r = helper(root.right, True)
        
        path = max(l, r)
        res.append(path)

        return l + 1 if is_right else r + 1
            
    
    helper(root, False) # go left
    helper(root, True) # go right
    
    return max(res)