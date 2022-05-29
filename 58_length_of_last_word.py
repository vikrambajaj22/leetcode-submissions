class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [x for x in s.split(' ') if len(x)]
        return len(s[-1])