class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute force is to square all and then sort
        # or sort using abs values and then square

        # two-pointer approach
        left = 0
        right = len(nums) - 1

        squares = [None] * len(nums)  # store final result

        for i in range(len(nums)-1, -1, -1):
            # backwards from len(nums)-1 to 0
            if abs(nums[left]) > abs(nums[right]):
                # the square of the left is larger
                squares[i] = nums[left] * nums[left]
                left += 1
            else:
                # the square of the right is larger
                squares[i] = nums[right] * nums[right]
                right -= 1

        return squares
