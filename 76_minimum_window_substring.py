# may TLE for some cases but returns the correct output, and is readable
# can find a more efficient way of checking is_valid by adding and removing/updating character counts from s_count while sliding, instead of recomputing s_count every time
class Solution(object):
    def is_valid(self, substring, t_counts):
        s_counts = Counter(substring)
        return all(ch in s_counts and s_counts[ch]>=t_counts[ch] for ch in t_counts)
        
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(t) > len(s):
            return ''
        
        # sliding window: start with l and r at 0, keep increasing r until all characters of t are found in s[l:r+1]
        # then, start minimizing the window (by increasing l) until the window becomes invalid (no longer contains all characters of t), keeping track of the minimum valid window/substring
        # then, continue this till the end of the string
        
        t_counts = Counter(t)
        
        l, r = 0, 0
        min_window = ''
        
        for r in range(len(s)):
            if not self.is_valid(s[l:r+1], t_counts):
                continue
            
            window = s[l:r+1]
            if not min_window: min_window = window
            
            # reduce window size till window is invalid
            while self.is_valid(s[l:r+1], t_counts):
                l += 1
            
            if len(min_window) > (r-(l-1)+1):  # l-1 because window became invalid at l
                min_window = s[l-1:r+1] 
                
        return min_window