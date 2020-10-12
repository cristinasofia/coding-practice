# 700 https://leetcode.com/problems/search-in-a-binary-search-tree/

def search_recursive(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    
    def search(node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return search(node.left, val)
        if val > node.val:
            return search(node.right, val)
    
    return search(root, val)

def search_iterative(root, val):

    if not root:
        return None

    node = root
    
    while node:
        if val == node.val:
            return node
        if val < node.val:
            node = node.left
        else: # val > node.val
            node = node.right
    
    return node

def search_iterative_duplicates(root, val):
    
    if not root:
        return None

    node = root
    
    while node:
        if val < node.val:
            node = node.left
        else: # val >= node.val
            node = node.right
    
    return node