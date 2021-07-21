class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        total_sum = n*(n+1)//2
        
        return total_sum - sum(nums)