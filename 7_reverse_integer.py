class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        is_neg = False

        if x < 0:
            is_neg = True
            x = x * -1

        while(x > 0):
            rem = x % 10
            x = x / 10
            rev = rev * 10 + rem

        if abs(rev) > 2**31:
            return 0

        if is_neg:
            rev = -rev

        return rev
