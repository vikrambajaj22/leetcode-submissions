class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profit = float('inf'), 0

        for price in prices:
            min_price, max_profit = min(min_price, price), max(
                max_profit, price-min_price)

        return max_profit
