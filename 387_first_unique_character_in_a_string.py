class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}

        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        for i, ch in enumerate(s):
            if d[ch] == 1:
                return i

        return -1
