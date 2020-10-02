#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def inorderSuccessor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    
    node = root
    min_node = None
    while node:
        if node.val > p.val:    # if current node value is greater
            min_node = node     # current node is the successor
            node = node.left    # go left
        else:
            node = node.right   # go right

    return node