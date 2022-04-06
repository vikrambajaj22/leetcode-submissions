class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         nums = sorted(list(set(nums)))  # O(nlogn) and using set because duplicates are not counted as consecutive

#         max_len = 1
#         curr_len = 1

#         if len(nums) <= 1:
#             return len(nums)

#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1] + 1:
#                 curr_len += 1
#                 max_len = max(max_len, curr_len)
#             else:
#                 curr_len = 1  # reset

#         return max_len

        # O(n) solution
        unique = set(nums)
        max_len = 0

        for num in unique:
            if num-1 not in unique:
                curr_len = 1
                while num + curr_len in unique:
                    curr_len += 1
                max_len = max(max_len, curr_len)

        return max_len
