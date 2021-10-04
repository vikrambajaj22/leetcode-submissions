class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        from math import factorial as fact

        good_pairs = 0

        for num in counts:
            count = counts[num]
            if count > 1:
                good_pairs += fact(count) / (fact(2) *
                                             fact(count-2))  # countC2

        return good_pairs
