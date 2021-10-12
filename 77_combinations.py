    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        index = 0
        res = []
        sub = []
        
        self.backtrack(nums, k, index, sub, res)
        
        return res
    
    
    def backtrack(self, nums, k, index, sub, res):
        if k == 0:
            res.append(sub)
            
        for i in range(index, len(nums)):
            self.backtrack(nums, k-1, i+1, sub+[nums[i]], res)