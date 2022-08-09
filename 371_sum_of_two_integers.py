class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # bit manipulation
        # a ^ b gives the result if there is no carry
        # (a & b) << 1 is the carry, add it to the ^ result till there is no carry
        
        while b:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
            
        return a