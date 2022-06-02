class Solution(object):
    def process_backspaces(self, s):
        stack = []
        
        for ch in s:
            if ch != '#':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                
        return ''.join(stack)
        
        
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.process_backspaces(s) == self.process_backspaces(t)