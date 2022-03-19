class Solution(object):
    def backtrack(self, nums, index, subset, res, k):
        if k == 0:
            res.append(subset)

        for i in range(index, len(nums)):
            self.backtrack(nums, i+1, subset+[nums[i]], res, k-1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []

        # same as the combinations program but finding combinations for all 0 <= k <= n
        for k in range(0, len(nums)+1):
            k_len_subsets = []
            self.backtrack(nums, 0, [], k_len_subsets, k)
            sol.extend(k_len_subsets)

        return sol
