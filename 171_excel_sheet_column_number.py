class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 1
        d = {}
        for a in alpha:
            d[a] = i
            i += 1

        res = 0
        for a in columnTitle:
            res = res * 26 + d[a]

        return res
