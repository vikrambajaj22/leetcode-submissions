class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        product = 1

        while n:
            r = n % 10
            n = n / 10
            s += r
            product *= r

        return product-s
