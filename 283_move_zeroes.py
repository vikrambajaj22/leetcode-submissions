class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums = nums[:i] + nums[i+1:] + [0]
        # output prints correct result but leetcode doesn't accept this

        n = len(nums) - 1
        i = 0

        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1
