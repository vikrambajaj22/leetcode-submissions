class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # implemented after looking at discussions
        res = []
        visited = set()
        self.backtrack(nums, visited, [], res)
        return res

    def backtrack(self, nums, visited, subset, res):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(nums, visited, subset+[nums[i]], res)
                visited.remove(i)  # for next permutation
