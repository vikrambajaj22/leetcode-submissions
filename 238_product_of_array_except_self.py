class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre, suf = 1, 1
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
            
            res[-1-i] *= suf
            suf *= nums[-1-i]
            
        return res