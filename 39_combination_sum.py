class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(candidates, 0, target, [], res)
        
        return res
    
    
    def backtrack(self, nums, index, target, subset, res):
        if target < 0:
            return  # backtracking
        
        if target == 0:
            # found a combination
            res.append(subset)
            
        for i in range(index, len(nums)):
            # we pass i to index instead of i+1 because the same number can be used multiple times in the combination
            self.backtrack(nums, i, target-nums[i], subset+[nums[i]], res)
        