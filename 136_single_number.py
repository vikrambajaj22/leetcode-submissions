class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cannot use dict/Counter since O(1) space complexity is needed
        # d = {}
        # for num in nums:
        #     if num not in d:
        #         d[num] = 1
        #     else:
        #         d[num] += 1
        # for num in d:
        #     if d[num] == 1:
        #         return num

        # freq = Counter(nums)
        # for item in freq.items():
        #     if item[1] == 1:
        #         return item[0]

        # cannot use count for each element, that would be O(n2) time complexity
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num

        # math solution (also needs O(n) space for set)
        # return 2 * sum(set(nums)) - sum(nums)

        # XOR solution is the only O(1) space complexity solution, with O(n) time complexity
        # num ^ 0 = num, but num ^ num = 0

        x = 0
        for num in nums:
            x ^= num

        return x
