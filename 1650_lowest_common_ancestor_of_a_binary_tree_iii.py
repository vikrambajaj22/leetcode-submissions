"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def get_depth(self, node):
        depth = 0
        while node:
            node = node.parent  # upward pointer move
            depth += 1
            
        return depth
        
        
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        # find depth difference
        # get the lower pointer up to the higher one
        # then move both pointers up in parallel till they meet
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)
        
        for _ in range(p_depth - q_depth):
            # p is deeper, move it upward to reach q's depth
            p = p.parent
            
        for _ in range(q_depth - p_depth):
            # q is deeper, move it upward to reach p's depth
            q = q.parent
            
        # now that p and q are at the same depth, move both upwards till they meet
        while p != q:
            p = p.parent
            q = q.parent
            
            
        return p
        