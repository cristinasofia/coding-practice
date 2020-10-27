# 637 https://leetcode.com/problems/average-of-levels-in-binary-tree/

def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    levels = []
    if not root:
        return levels
    
    lsum = []
    lcount = []
    
    def helper(node, level):
        if len(lsum) == level:
            lsum.append(0)
        if len(lcount) == level:
            lcount.append(0)
        
        lsum[level] += node.val
        lcount[level] += 1
        
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
            
    helper(root, 0)
    
    return [float(s)/float(c) for s, c in zip(lsum,lcount)]