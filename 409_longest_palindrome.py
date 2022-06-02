class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1
                
        total = 0
        odd_counts = 0
        
        for ch in counts:
            if counts[ch] % 2 == 0:
                total += counts[ch]
            else:
                odd_counts += 1
                total += counts[ch] - 1
          
        if odd_counts:
            total += 1  # for the center character of a palindrome
            
        return total