class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        mid = len(s) / 2
        for i in range(mid):
            # swap s[i] with s[len(s)-1-i]
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp

        return s
