# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        if root == p or root == q:
            return root

        # try finding p and q in left and right sub-trees of current node
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # both p and q were found in left and right sub-trees of current node
            # return current node as LCA
            return root
        else:
            # either p or q was found in left or right sub-tree of current node
            # ex. p found in left sub-tree, right sub-tree returned None,
            # so q is somewhere below node where p was found; we dont need to search all the way,
            # because node where p was found is LCA
            return left or right
