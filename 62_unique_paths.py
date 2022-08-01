class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dynamic programming
        # for a 3*4 grid (ex.) the number of steps to get from the start to each cell are:
        #  1 1 1 1
        #  1 2 3 4
        #  1 3 6 10
        # for the 1st row and 1st col, there's only 1 was to get to each cell from 0,0
        # for all the others, num_ways[i,j] = num_ways[i-1, j] + nums_ways[i, j-1] i.e top + left
        dp = [[1] * n for _ in range(m)]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]