class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # assumption: len(s) == len(t)
        s_counts = {}
        for ch in s:
            if ch not in s_counts:
                s_counts[ch] = 1
            else:
                s_counts[ch] += 1
                
        steps = 0
        
        for ch in t:
            if ch in s_counts and s_counts[ch] > 0:
                # ch match found in s, so decrement count of that ch
                s_counts[ch] -= 1
            else:
                # ch not in s or count of ch in s exceeded, replace ch
                steps += 1
                
        return steps