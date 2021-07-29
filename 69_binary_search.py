class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x

        # use binary search to find sqrt
        l = 0
        h = x

        while l <= h:
            m = (l+h)//2
            if m*m <= x < (m+1)*(m+1):
                return m
            elif x < m*m:
                h = m - 1
            else:
                l = m + 1
