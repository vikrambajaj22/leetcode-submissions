class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
#         s = list(s)  # strings are immutable, convert to list
#         i = 0
#         n = len(s)-1

#         while i < n:
#             if s[i:i+k] == [s[i]]*k:
#                 # k elements including element at i are all duplicates
#                 # remove them
#                 s = s[:i] + s[i+k:]

#                 # decrement i and n by k
#                 # decrementing by k allows to check for newly-obtained duplicates from the back
#                 i = max(0, i-k)
#                 n = max(0, n-k)
#             else:
#                 i += 1

#         return ''.join(s)

        # using a stack
        stack = []  # stores [ch, count] items

        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                # stack[-1][0] == ch
                ch_count = stack[-1][1]
                if ch_count == k-1:
                    # this occurrence of ch is the kth consecutive occurrence
                    # remove ch from stack
                    stack.pop()
                else:
                    stack[-1][1] += 1

        res = ''
        while stack:
            ch, count = stack.pop()
            res = ch * count + res

        return res
