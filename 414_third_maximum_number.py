class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = list(set(nums))
        if len(unique) < 3:
            return max(unique)
        return sorted(unique)[len(unique)-3]
