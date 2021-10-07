class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False

        # return sorted(list(s)) == sorted(list(t))  # O(nlogn)
        # below is O(n) i.e. checking character frequencies

        t_dict = {}
        s_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1

            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1

        return s_dict == t_dict
