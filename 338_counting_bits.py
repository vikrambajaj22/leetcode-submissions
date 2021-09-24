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


# alternate solution using dynamic programming
class Solution2(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]

        # logic: any even number x will have the same number of 1s as x/2,
        # since multiplying with 2 just adds a 0 at the end;
        # ex. 2->10, 4->100, 8->1000
        # any odd number x will have one more 1 than x/2
        # ex. 2->10, 5->101; 3->11, 7->111

        # using dynamic programming
        for i in range(1, n+1):
            if i % 2 == 0:
                ans.append(ans[i/2])
            else:
                ans.append(ans[i/2] + 1)

        return ans
