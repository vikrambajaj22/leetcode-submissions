# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # saving preorder
        preorder = []
        
        def helper(root, preorder):
            if not root:
                return
            preorder.append(str(root.val))
            helper(root.left, preorder)
            helper(root.right, preorder)
            
        helper(root, preorder)
        
        return ' '.join(preorder)  # serializing
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = [int(d) for d in data.split()]
        inorder = sorted(preorder)  # BST property (inorder is in asc order)
        
        # reconstructing tree using preorder and inorder (#105)
        def reconstruct(preorder, inorder):
            root = None
            if inorder:
                root_val = preorder.pop(0)
                index = inorder.index(root_val)
                root = TreeNode(root_val)
                root.left = reconstruct(preorder, inorder[:index])
                root.right = reconstruct(preorder, inorder[index+1:])
                
            return root
         
        return reconstruct(preorder, inorder)
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans