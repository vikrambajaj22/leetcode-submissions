class Solution(object):
    def rotateArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # every len(nums) rotations will return the original array
        k = k % len(nums)  # only rotate the remainder times

        nums[:] = nums[-k:] + nums[:-k]  # [:] will update in-place
