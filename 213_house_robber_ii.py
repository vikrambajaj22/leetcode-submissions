class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def house_robber(nums):
            # simple house robber solution (#198)
            two_before, one_before = 0, 0
            
            for n in nums:
                curr = max(two_before + n, one_before)
                two_before = one_before
                one_before = curr
                
            return curr
        
        # house 0 and house n-1 cannot be robbed since they are adjacent
        # so we just have to return the max of house_robber(nums[1:]) and house_robber(nums[:-1]) i.e. robbing non-adjacent houses from house 1 to n-1 or robbing adjacent houses from 0 to n-2
        if len(nums) == 1:
            return nums[0]
        
        return max(house_robber(nums[:-1]), house_robber(nums[1:]))