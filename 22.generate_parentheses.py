class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # use backtracking
        # start with an open parenthesis and add more as long as we don't excced n
        # add closing parentheses if # closing < # opening

        res = []

        def backtrack(opening, closing, s):
            if opening == closing == n:
                res.append(s)

            if opening < n:
                backtrack(opening+1, closing, s+'(')
            if closing < opening:
                backtrack(opening, closing+1, s+')')

        backtrack(0, 0, '')

        return res
