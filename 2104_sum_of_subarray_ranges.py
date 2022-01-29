class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        range_sum = 0
        for i in range(len(nums)):
            l, r = nums[i], nums[i]
            for j in range(i+1, len(nums)):
                l = min(l, nums[j])
                r = max(r, nums[j])
                range_sum += r-l

        return range_sum
