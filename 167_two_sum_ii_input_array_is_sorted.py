class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # # dictionary two-sum
        # d = {}
        # for i, n in enumerate(numbers):
        #     m = target - n
        #     if m in d:
        #         return [d[m]+1, i+1]
        #     d[n] = i

        # two-pointer based, using non-decreasing property
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                # left number too small
                left += 1
            else:
                # right number too big
                right -= 1
