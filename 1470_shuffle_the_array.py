class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return nums

        res = []
        # res.extend([y for x in zip(nums[:n], nums[n:]) for y in x])

        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
