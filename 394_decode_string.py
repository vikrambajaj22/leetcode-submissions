class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Input: s = "3[a21[cd]]s"

        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                repeating_substr = ''
                while stack and stack[-1] != '[':
                    repeating_substr = stack.pop() + repeating_substr
                # pop [
                stack.pop()
                # extract k (can have multiple digits)
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # append repeating substring to stack
                stack.append(repeating_substr * int(k))

        return ''.join(stack)
