# 701 https://leetcode.com/problems/insert-into-a-binary-search-tree/

# each method is O(log(n)) average, O(n) worst

# uses constant heap space
def insert_recursive(root, val):
        
    def insert(node, val):
        if not node:
            return TreeNode(val)
        # not needed for problem: it is guaranteed that
        # new value does not exist in BST
        # elif node.val == val:
            # return
        elif val < node.val:
            if node.left:
                insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else: # val > node.val
            if node.right:
                insert(node.right, val)
            else:
                node.right = TreeNode(val)

        return root
    
    return insert(root, val)

# uses constant stack space
def insert_iterative(root, val):
    if not root:
        return TreeNode(val)

    node = root

    while node:
        if val < node.val:
            if node.left:
                node = node.left
            else:
                node.left = TreeNode(val)
                return root
        else:
            if node.right:
                node = node.right
            else:
                node.right = TreeNode(val)
                return root
    
    return root

# reconstruct all ancestors of the inserted node; 
# any reference to the original tree root remains valid, 
# making the tree a persistent data structure:

def insertIntoBst(root, val):
    if root is None:
        return TreeNode(val, None, None)
    if val == root.val:
        return TreeNode(val, root.left, root.right)
    if val < root.val:
        return TreeNode(root.val, self.insertIntoBST(root.left, val), root.right)
    
    return TreeNode(root.val, root.left, self.insertIntoBST(root.right, val))