class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # sort by length
        strs = sorted(strs, key=lambda s: len(s))

        for i in range(len(strs[0])):
            prefix_count = 0
            prefix = strs[0][:len(strs[0])-i]
            for s in strs:
                if s[:len(prefix)] == prefix:
                    prefix_count += 1
            if prefix_count == len(strs):
                return prefix

        # no longest-comment prefix found
        return ''
