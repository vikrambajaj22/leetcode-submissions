class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # strip away unwanted characters and convert to lowercase
        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        mid = len(s) / 2

        for i in range(mid):
            if s[i] == s[len(s)-i-1]:
                continue
            else:
                return False

        return True

        # return s == ''.join(reversed(s))
