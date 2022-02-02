class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums[:]
        self.original = nums[:]  # copies without reference

    def reset(self):
        """
        :rtype: List[int]
        """
        self.array = self.original[:]  # reset array to original
        return self.array

    def shuffle(self):
        """
        :rtype: List[int]
        """
        for i in range(len(self.array)):
            # new random index in range [i, n)
            new_index = random.randint(i, len(self.array)-1)
            # the fact that the new_index can be i gives every index an equal probability
            self.array[i], self.array[new_index] = self.array[new_index], self.array[i]

        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
