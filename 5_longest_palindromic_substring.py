class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # based on #647
        max_len = 0
        longest = ''
        
        for i in range(2*len(s)-1):
            l = i // 2
            r = (i + 1) // 2
            
            while l >= 0 and r < len(s) and s[l] == s[r]:                    
                l -= 1
                r += 1
                
            substr = s[l+1:r]
            if len(substr) > max_len:
                max_len = len(substr)
                longest = substr
                
        return longest