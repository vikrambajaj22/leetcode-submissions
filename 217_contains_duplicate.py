class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(set(nums)) != len(nums)
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return True
        return False
