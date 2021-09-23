class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ''
        
        palindrome = list(palindrome)
        
        for i in range(len(palindrome)/2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
            
        # if we reached middle and all a's so far, change last char to 'b'
        palindrome[-1] = 'b'
        
        return ''.join(palindrome)