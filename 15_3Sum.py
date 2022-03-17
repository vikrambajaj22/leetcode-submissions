class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(
            nums)  # we don't need to return indices, just the numbers themselves, so we can sort
        sol = set()  # unique tuples

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1  # two pointer

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0:
                    # left element was too small
                    l += 1
                elif three_sum > 0:
                    # right element was too big
                    r -= 1
                else:
                    # using tuple because list is not hashable
                    sol.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return sol
