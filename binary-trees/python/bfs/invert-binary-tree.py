# 226 https://leetcode.com/problems/invert-binary-tree/

def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    if not root:
        return root
    
    q = [root]
    while q:
        n = q.pop(0)
        n.left, n.right = n.right, n.left
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
            
    return root