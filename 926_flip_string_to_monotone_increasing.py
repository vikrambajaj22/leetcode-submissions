class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        one_count = 0
        flip_count = 0

        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1
                continue

            flip_count += 1  # try flipping a 0
            # if there are less 1s, flip 1s instead
            flip_count = min(flip_count, one_count)

        return flip_count
