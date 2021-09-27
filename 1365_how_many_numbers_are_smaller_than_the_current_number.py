class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute force is O(n^2)
        # below is O(nlogn)

        sorted_nums = sorted(nums)
        index = {}  # first index of each unique num after sorting

        for i, num in enumerate(sorted_nums):
            if num not in index:
                index[num] = i

        res = []
        for num in nums:
            # sorted index = number of elements that were less than num
            res.append(index[num])

        return res
