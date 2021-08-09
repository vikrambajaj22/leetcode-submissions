class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_squares = n
        mem = set()  # store unique sums
        while sum_squares != 1:
            sum_squares = self.compute_sum_of_squares(sum_squares)
            if sum_squares in mem:
                return False  # sum of squares recurs endlessly
            else:
                mem.add(sum_squares)

        return True

    def compute_sum_of_squares(self, n):
        sum = 0
        while n > 0:
            r = n % 10
            n = n / 10
            sum += r ** 2
        return sum
