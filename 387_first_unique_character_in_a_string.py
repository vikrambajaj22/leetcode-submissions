class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = OrderedDict()
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        for ch in d:
            if d[ch] == 1:
                return s.index(ch)

        return -1
