class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        # find split index i.e. index at which order changes
        split_index = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                split_index = i
                break

        found = False

        if split_index > -1:
            if target > nums[-1] and target <= nums[split_index]:
                # look from 0 to split_index
                for i in range(0, split_index+1):
                    if nums[i] == target:
                        found = True
                        return i
            elif target >= nums[split_index+1] and target <= nums[-1]:
                # look from split_index+1 to end
                for i in range(split_index+1, len(nums)):
                    if nums[i] == target:
                        found = True
                        return i
            else:
                return -1
        else:
            # binary search since it is ordered
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (high + low) // 2
                if target > nums[mid]:
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    return mid
            return -1

        if not found:
            return -1
