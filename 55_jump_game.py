class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            # if you can reach end from i, all you need to do is reach i
            if i + nums[i] >= end:
                end = i
                
        return end == 0