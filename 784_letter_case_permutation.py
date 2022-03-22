class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = ['']

        for ch in s:
            if ch.isalpha():
                res = [substr+x for substr in res for x in [ch.upper(), ch.lower()]]
            else:
                res = [substr+ch for substr in res]

        return res
