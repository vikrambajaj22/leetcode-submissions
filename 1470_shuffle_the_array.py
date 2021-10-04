class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
#         # O(n) space
#         res = []
#         for i in range(n):
#             res.append(nums[i])
#             res.append(nums[n+i])

#         return res

        # O(1) space
        for i in range(n):
            nums[i] = [nums[i], nums[n]]
            nums.pop(n)  # pop element at nth index

        # flatten nums
        nums = [x for sublist in nums for x in sublist]

        return nums
