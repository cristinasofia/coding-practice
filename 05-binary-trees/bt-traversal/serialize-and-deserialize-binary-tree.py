# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# PREORDER
class Codec_Preorder:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []
                
        return " ".join(map(str,preorder(root)))


    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(l, r):
            if not data:
                return None
            if not l<= data[0] <= r:
                return None
            
            v = data.pop(0)
            root = TreeNode(v)
            root.left = helper(l, v)
            root.right = helper(v, r)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
        
        return helper(float('-inf'), float('inf'))
        
# POSTORDER  
class Codec_Postorder:
    
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
                
        return " ".join(map(str,postorder(root)))


    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(l, r):
            if not data:
                return None
            if not l <= data[-1] <= r:
                return None
            
            v = data.pop()
            root = TreeNode(v)
            root.right = helper(v, r)
            root.left = helper(l, v)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
      
        return helper(float('-inf'), float('inf')) 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))