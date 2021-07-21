class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)

        return len([i for i in range(len(expected)) if expected[i] != heights[i]])
