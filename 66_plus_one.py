class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        carry_one = True
        i = len(digits) - 1
        while i >= 0 and carry_one:
            if digits[i] == 9:
                carry_one = True
                digits[i] = 0
            else:
                if carry_one:
                    digits[i] += 1
                    carry_one = False
            i -= 1

        if carry_one:
            # reached i=-1 but carry_one is True
            return [1] + digits

        return digits
