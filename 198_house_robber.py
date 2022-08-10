class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        two_before, one_before = 0, 0
        
        # [two_before, one_before, n, n+1, ...]        
        for n in nums:
            curr = max(n + two_before, one_before)
            two_before = one_before
            one_before = curr
            
        return curr