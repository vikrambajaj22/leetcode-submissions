class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        s1_sorted = sorted(s1)

        # checking all contiguous substrings of length len(s1) in s2
        # to see if they have the same characters

        for i in range(len(s2)-len(s1)+1):
            substr = s2[i:i+len(s1)]
            if sorted(substr) == s1_sorted:
                return True

        return False
