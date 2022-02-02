class Solution(object):
    def count_ones(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1

        return count

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.count_ones(x ^ y)  # XOR will be 1 when the bits are different, and 0 otherwise
