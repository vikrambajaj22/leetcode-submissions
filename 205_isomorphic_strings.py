class Solution(object):
    def mapper(self, s):
        counter = 1
        s_map = {}
        res = ''
        
        for ch in s:
            if ch in s_map:
                res += s_map[ch]
            else:
                res += str(counter)
                s_map[ch] = str(counter)
                counter += 1
        
        return res
        
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # replacing characters with numbers
        # ex. paper = 12134, title = 12134 (use same number if character was seen before, next num otherwise)
        
        return self.mapper(s) == self.mapper(t)