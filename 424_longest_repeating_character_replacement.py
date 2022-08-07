class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        freq = {}  # character frequencies
        max_freq = 0
        max_len = 0
        
        for right, ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
                
            max_freq = max(max_freq, freq[ch])
            
            # if window size - max_feq > k, cannot perform enough replacements
            # so, remove ch at left from window, decrement its freq, and move the window forward
            if (right-left+1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            else:
                # can perform enough replacements
                max_len = max(max_len, right-left+1)
                
        return max_len