class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(list(s)) == sorted(list(t))  # O(nlogn)

        # below is O(n)
        s_dict = {}
        t_dict = {}

        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 1
            else:
                s_dict[ch] += 1

        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 1
            else:
                t_dict[ch] += 1

        return s_dict == t_dict
