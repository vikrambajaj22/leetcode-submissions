class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1/x

        res = self.myPow(x, n//2)  # recursively solve upto half of n

        if n % 2 == 0:
            return res * res
        else:
            return res * res * x
