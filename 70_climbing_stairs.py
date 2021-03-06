class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # will be n-1'th element of fibonacci series
        fib = [1, 2]  # when n=1, #ways=1; when n=1, #ways=2
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
            
        return fib[n-1]