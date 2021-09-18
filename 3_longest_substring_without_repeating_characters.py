class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

#         # brute force
#         max_len = 0

#         for i, ch in enumerate(s):
#             sub = set()
#             substr_count = 0
#             for c in s[i:]:
#                 if not c in sub:
#                     substr_count += 1
#                     sub.add(c)
#                 else:
#                     break
#             if substr_count > max_len:
#                 max_len = substr_count

#         return max_len

        # sliding window
        left = 0
        last_seen = {}  # store last-seen indices of characters
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen:
                # if ch was last-seen at/ahead of left, move left forward
                # if ch was last-seen prior to left, keep left where it is
                # do not move left backward
                # ex. in 'abbac' when we get to second a, left will be at second b,
                # don't move it back to first b, keep left at second b
                left = max(last_seen[ch] + 1, left)
            max_len = max(max_len, right-left+1)
            last_seen[ch] = right

        return max_len
