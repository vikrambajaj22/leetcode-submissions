class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = max(nums)
        curr_min, curr_max = 1, 1
        
        # for each num, keep track of curr_min and curr_max prior to it
        # if num is zero, simply reset curr_min and curr_max to 1
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
                continue
                
            temp = curr_min
            curr_min = min(n*curr_min, n*curr_max, n)  # n*curr_min will be lowest if either one is negative, same for n*curr_max, and if both prev values end up being positive and n is negative, then n is the lowest
            curr_max = max(n*temp, n*curr_max, n)  # using temp because we need the prev value of curr_min; logic for curr_max is same as curr_min: n*temp is highest if both are positive or both are negative, same for n*curr_max, and if both prev values end up being negative and n is positive, then n is the highest
            max_product = max(max_product, curr_max)
            
        return max_product
