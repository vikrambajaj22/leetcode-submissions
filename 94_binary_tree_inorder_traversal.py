# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        if not root:
            return []
        self.traversalImplementer(root, traversal)
        return traversal

    def traversalImplementer(self, root, traversal):
        if root.left:
            self.traversalImplementer(root.left, traversal)
        traversal.append(root.val)
        if root.right:
            self.traversalImplementer(root.right, traversal)
