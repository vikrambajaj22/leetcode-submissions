# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.traversalImplementer(root, result)
        return result

    def traversalImplementer(self, root, result):
        result.append(root.val)
        if root.left:
            self.traversalImplementer(root.left, result)
        if root.right:
            self.traversalImplementer(root.right, result)
