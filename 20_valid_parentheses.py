class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        brackets = {'}': '{', ']': '[', ')': '('}

        stack = []

        for ch in s:
            if ch in {'{', '(', '['}:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[ch] == top:
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
