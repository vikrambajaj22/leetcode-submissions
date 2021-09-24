class Solution(object):
    def num_one_bits(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            ans.append(self.num_one_bits(i))

        return ans
