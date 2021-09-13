class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if the single number would be present 3 times, sum will be 3*sum(set(nums))
        # but since it's present only once, we can obtain 2*single_number by subtracting sum(nums) from above
        # and finally get single number by diving by 2

        # O(n) space complexity because of set
        return (3 * sum(set(nums)) - sum(nums)) / 2

        # O(n) space complexity can be done using Counter or simple dictionary counts also,
        # O(1) space complexity needs bit manipulation
