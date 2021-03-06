# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # BST inorder traversal is in ascending order
        # so the kth value in the traversal is the result
        
        traversal = []
        self.inorder(root, traversal)
        return traversal[k-1]  # since k is 1-indexed
        
    
    def inorder(self, root, traversal):
        if root.left:
            self.inorder(root.left, traversal)
        traversal.append(root.val)
        if root.right:
            self.inorder(root.right, traversal)
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class AlternateSolution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # BST inorder traversal is in ascending order
        # performing inorder traversal till k nodes are traversed
        
        self.res = None
        self.k = k
        self.inorder(root)
        return self.res
        
    
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        if root.right:
            self.inorder(root.right)
            