# 103 https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    levels = []
    if not root:
        return levels
    
    def helper(node, l):
        if not node:
            return
        if len(levels) == l:
            levels.append([])
            
        if l % 2 == 0:    
            levels[l] = levels[l] + [node.val]
        else:
            levels[l] = [node.val] + levels[l]
            
        if node.left:
            helper(node.left, l + 1)
        if node.right:
            helper(node.right, l + 1)
            
    helper(root, 0)
    return levels