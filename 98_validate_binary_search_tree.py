# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # idea: inorder traversal must be sorted in increasing order
        if not root:
            return True
        traversal = []
        self.inorder(root, traversal)

        for i in range(len(traversal)-1):
            if traversal[i] >= traversal[i+1]:
                return False

        return True

    def inorder(self, root, traversal):
        if root.left:
            self.inorder(root.left, traversal)
        traversal.append(root.val)
        if root.right:
            self.inorder(root.right, traversal)
