class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the bitwise operation n & (n-1) knocks out the rightmost 1
        # ex. 1011 & 1010 = 1010
        # keep doing this until all 1s are knocked out (i.e. n=0) and count how many iterations it took

        count = 0
        while n:
            n = n & (n-1)
            count += 1

        return count
