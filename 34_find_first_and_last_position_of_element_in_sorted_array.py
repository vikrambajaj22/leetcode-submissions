# solution 1: two binary searches for the same target
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_index():
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low + high) // 2
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        def last_index():
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low+high) // 2
                if target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        
        first = first_index()
        last = last_index()
        if first <= last: return [first, last]
        else: return [-1, -1]

# solution 2: binary search the target (to get first occurrence) and target + 1 (to get last occurrence)
class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_index(x):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if x > nums[mid]:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        # find first occurrence of target
        # then find first occurrence of the next number greater than target to get last occurrence of target, since array is sorted
        first, last = first_index(target), first_index(target+1)-1
        
        if first <= last: return [first, last]
        else: return [-1, -1]