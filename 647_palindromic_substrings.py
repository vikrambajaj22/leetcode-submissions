class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # there can be 2n-1 palindromic centers for an array of length n
        # i.e. 0, between 0 and 1, 1, between 1 and 2, ..., n-1, between n-1 and n, n
        
        # at each center, expand leftwards and rightwards
        
        count = 0
        
        for i in range(2*len(s)-1):
            left = i // 2
            right = (i + 1) // 2

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
                
        return count
