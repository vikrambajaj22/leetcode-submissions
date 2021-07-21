class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        elif target <= nums[0]:
            return 0
        else:
            low = 0
            high = len(nums) - 1
            mid = (low + high) // 2

            while low <= high:
                mid = (low + high) // 2
                if target > nums[mid]:
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                elif target == nums[mid]:
                    return mid

            # target wasn't found
            return low
