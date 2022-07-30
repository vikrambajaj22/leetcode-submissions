# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = None
        if inorder:
            # root will be first element in preorder
            # get its index in the inorder traversal
            # everything to its left in the inorder traversal is the left subtree and
            # everything to its right in the inorder traversal is the right subtree
            
            # assumption: unique node values
            root_val = preorder.pop(0)
            index = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            
        return root