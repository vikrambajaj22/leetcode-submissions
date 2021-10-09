class Solution(object):
    def sum_squares(self, n):
        s = 0
        while n:
            r = n % 10
            n = n / 10
            s += r**2

        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = set()  # store unique sums
        while n != 1:
            n = self.sum_squares(n)
            if n in prev:
                # it will go on endlessly
                return False
            prev.add(n)

        return True
