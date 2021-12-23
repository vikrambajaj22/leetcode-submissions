class Solution(object):
    def count(self, num):
        counter = {str(i): 0 for i in range(10)}
        digits = list(str(num))

        count = []
        current_digit = digits[0]
        for d in digits:
            if d == current_digit:
                counter[d] += 1
            else:
                count.append((current_digit, counter[current_digit]))
                counter[current_digit] = 0
                current_digit = d
                counter[d] += 1

        count.append((current_digit, counter[current_digit]))

        say = ''

        for item in count:
            say += str(item[1]) + item[0]

        return say

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ['1']
        for i in range(1, n):
            res.append(self.count(res[i-1]))

        return res[-1]
