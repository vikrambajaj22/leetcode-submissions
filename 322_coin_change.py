class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # helpful video: https://www.youtube.com/watch?v=H9bfqozjoqs
        dp = [float('inf')] * (amount+1)
        dp[0] = 0  # dp[i] = min num of coins to sum to i
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    
        return dp[amount] if dp[amount] != float('inf') else -1