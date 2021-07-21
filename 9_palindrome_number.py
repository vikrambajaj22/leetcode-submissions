class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        num = x
        rev = 0

        while(x > 0):
            rev = rev * 10 + x % 10
            x = x / 10

        return rev == num
