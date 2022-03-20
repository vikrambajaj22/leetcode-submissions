class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # use count sort since the numbers are in a fixed range
        counts = [0, 0, 0]  # counts for 0, 1 and 2
        
        for num in nums:
            counts[num] += 1
            
        i = 0
        
        # replace numbers in nums with 0, 1, and 2 based on counts
        for count_index in {0, 1, 2}:
            while counts[count_index] > 0:
                nums[i] = count_index
                i += 1
                counts[count_index] -= 1
                