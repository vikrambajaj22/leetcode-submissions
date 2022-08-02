class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        # dp[i] is True if s[:i] is segmentable into words in dictionary
        dp[0] = True  # base case since s[:0] i.e. '' is segmentable
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    # if s[:j] is segmentable and s[j:i] is in wordDict, s[:i] is segmentable
                    dp[i] = True
                    break
                    
        return dp[len(s)]  # i.e. checking if s[:len(s)] i.e. s is segmentable