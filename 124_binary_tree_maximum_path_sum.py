# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -float('inf')
        self.dfs(root)
        return self.max_sum
    
    
    def dfs(self, root):
        if not root: return
        
        left_sum = max(0, self.dfs(root.left))
        right_sum = max(0, self.dfs(root.right))
        
        self.max_sum = max(self.max_sum, root.val+left_sum+right_sum)
        
        return root.val + max(left_sum, right_sum)