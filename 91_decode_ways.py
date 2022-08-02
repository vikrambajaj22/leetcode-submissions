class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0": return 0
        
        num_ways = [0] * (len(s) + 1)
        num_ways[0] = 1  # extra val needed for rest of dp
        num_ways[1] = 1  # num ways to decode s[0:1]
        
        # ex. '123'
        # num ways to decode 1: 1
        # num ways to decode 12: 2 ("1 2" and "12")
        # num ways to decode 123: 3 ("1 2 3", "12 3", "1 23") ...
        
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i-1:i]) <= 9:
                num_ways[i] += num_ways[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                num_ways[i] += num_ways[i-2]
                
        return num_ways[-1]