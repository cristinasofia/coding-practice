# 98 https://leetcode.com/problems/validate-binary-search-tree/

def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    def helper(root, l, r):
        if not root:
            return True
        
        if not l < root.val < r:
            return False
        
        return helper(root.left, l, root.val) and helper(root.right, root.val, r)
            
    return helper(root, float("-inf"), float("inf"))

def isValidBST_recursive(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    def helper(root, l, r):
        if not root:
            return True
        if root.left:
            if root.left.val < root.val and root.left.val > l:
                pass
            else:
                return False
        if root.right:
            if root.right.val > root.val and root.right.val < r:
                pass
            else:
                return False
        return helper(root.left, l, root.val) and helper(root.right, root.val, r)
            
    return helper(root, float("-inf"), float("inf"))

def isValidBST_iterative(root):
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