class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [None] * len(s)
        j = 0

        for i in indices:
            res[i] = s[j]
            j += 1

        return ''.join(res)
