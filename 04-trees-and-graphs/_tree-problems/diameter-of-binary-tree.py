#

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = []
        def helper(root):
            
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            
            path = l + r
            
            ans.append(path)
            
            return 1 + max(l, r)
        
        helper(root)
        return max(ans)