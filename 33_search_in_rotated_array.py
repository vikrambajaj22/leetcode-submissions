class Solution(object):
    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        change_index = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                change_index = i
                break

        if change_index != -1:
            change = nums[change_index]

            if target > change:
                return -1

            if nums[0] <= target <= change:
                return self.binary_search(nums[:change_index+1], target)
            else:
                index = self.binary_search(nums[change_index+1:], target)
                if index != -1:
                    return (change_index+1) + index
                else:
                    return index

        else:
            # perform normal binary search since there was no rotation
            return self.binary_search(nums, target)
