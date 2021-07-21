class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # rsums = [nums[0]]
        # for i in range(1, len(nums)):
        #     rsums.append(rsums[i-1] + nums[i])
        if len(nums) == 1:
            return nums
        total = sum(nums)
        rsums = [total]
        for i in range(1, len(nums)):
            rsums.append(rsums[i-1]-nums[len(nums)-i])

        rsums.reverse()

        return rsums
