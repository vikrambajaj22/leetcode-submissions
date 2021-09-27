# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter, _ = self.depth(root)
        return diameter

    def depth(self, node):
        if not node:
            return 0, 0

        left_diameter, left_depth = self.depth(node.left)
        right_diameter, right_depth = self.depth(node.right)

        diameter = max(left_diameter, right_diameter, left_depth + right_depth)

        return diameter, 1 + max(left_depth, right_depth)
