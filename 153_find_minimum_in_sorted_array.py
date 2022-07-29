class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since O(log n) time complexity is needed, using binary search
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1
        
        if nums[low] < nums[high]:
            # array is sorted in asc order, so it was either not rotated or rotated a multiple of len(nums) times
            return nums[low]
        
        # array was rotated n times such that n % len(nums) != 0, so there is an inflection point, and the number after the inflection point is the lowest
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid+1]:
                # mid is the inflection point
                return nums[mid+1]
            
            if nums[mid-1] > nums[mid]:
                # mid-1 is the inflection point
                return nums[mid]
            
            if nums[mid] > nums[0]:
                # inflection point is after mid
                low = mid + 1
            else:
                # inflection point is before mid
                high = mid - 1