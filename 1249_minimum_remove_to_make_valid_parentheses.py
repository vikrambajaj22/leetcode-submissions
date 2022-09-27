class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(s)
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    # invalid closing parenthesis
                    s[i] = ''
            
        while stack:
            # if stack is not empty, we have extra opening parentheses
            # replace their indices in s with ''
            s[stack.pop()] = ''
            
        return ''.join(s)