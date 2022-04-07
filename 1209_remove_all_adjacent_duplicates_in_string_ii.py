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
            if not stack:
                stack.append([ch, 1])
            else:
                top, count = stack[-1]
                if ch == top:
                    if count == k-1:
                        # this is the kth occurrence, remove ch from stack
                        stack.pop()
                    else:
                        # increment consecutive count
                        stack[-1][1] += 1
                else:
                    # top != ch
                    stack.append([ch, 1])

        # all k-len duplicates have been removed
        # combine remaining characters using their counts
        return ''.join(s[0]*s[1] for s in stack)
