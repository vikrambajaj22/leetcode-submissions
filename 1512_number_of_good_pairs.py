import math


class Solution(object):

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        if len(nums) == 1 or len(set(nums)) == len(nums):
            return count

        num_dict = {}

        for i, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1

        f = math.factorial

        for num in num_dict:
            num_count = num_dict[num]
            if num_count > 1:
                count += f(num_count) / f(2) / f(num_count-2)

        return count
