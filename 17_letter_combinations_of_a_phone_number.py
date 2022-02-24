class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = []
            
        def backtrack(substr):
            if len(substr) == len(digits):
                res.append(substr)
                return
            
            next_num = digits[len(substr)]
            for letter in letter_map[next_num]:
                backtrack(substr + letter)
            
        backtrack('')
        
        return res