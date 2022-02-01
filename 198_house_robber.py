class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming: at every step, choose max of (curr_house+2_houses_before) and prev_house
        if len(nums) == 1:
            return nums[0]

        two_before, prev = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr_max = max(nums[i]+two_before, prev)
            two_before = prev
            prev = curr_max

        return prev  # stores the accumulated max
